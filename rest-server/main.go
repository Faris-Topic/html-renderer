package main

import (
	"log"
	"net/http"

	"github.com/Faris-Topic/html-renderer/internal/html"
	"github.com/Faris-Topic/html-renderer/internal/repository"
	"github.com/julienschmidt/httprouter"
)

type RESTServer struct {
	dbClient *repository.ForumClient
	router   *httprouter.Router
}

func main() {
	router := httprouter.New()
	forumClient, err := repository.InitClient("mongodb://localhost:27017")
	if err != nil {
		log.Fatal(err)
	}
	defer forumClient.Disconnect()

	server := RESTServer{
		dbClient: forumClient,
		router:   router,
	}
	server.registerRequestsHandler()

	err = http.ListenAndServe(":8080", server.router)
	log.Fatal(err)
}

func (s *RESTServer) registerRequestsHandler() {
	s.router.GET("/", s.homePageHandler)
	s.router.GET("/new-post", s.getNewPostPageHandler)
	s.router.GET("/post-details/:id", s.postDetailsHandler)
	s.router.POST("/new-post", s.postNewPostHandler)
}

func (s *RESTServer) homePageHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	posts, err := s.dbClient.ListAllPosts()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	
	html.HomePage(w, html.HomePageParams{Posts: posts})
}

func (s *RESTServer) getNewPostPageHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	p := html.NewPostDetails{}
	html.NewPost(w, p)
}


func (s *RESTServer) postNewPostHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	err := r.ParseForm()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	postTitle := r.PostFormValue("post_title")
	postBody := r.PostFormValue("post_body")

	newPost := repository.CreatePost{
		Title: postTitle,
		Body:  postBody,
	}

	newId, err := s.dbClient.InsertPost(newPost)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	http.Redirect(w, r, "/post-details/"+newId, http.StatusSeeOther)
}

func (s *RESTServer) postDetailsHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	id := ps.ByName("id")
	if id == "" {
		http.Error(w, "missing id", http.StatusBadRequest)
		return
	}

	postDetails, err := s.dbClient.GetPostById(id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	html.ShowPost(w, postDetails)
}
