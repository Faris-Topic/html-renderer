package main

import (
	"encoding/json"
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

type PostRequest struct {
	Title string `json:"post_title"`
	Body  string `json:"post_body"`
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

	err = http.ListenAndServe(":3000", server.router)
	log.Fatal(err)
}

func (s *RESTServer) registerRequestsHandler() {
	// Preflight requests
	s.router.OPTIONS("/", s.preflightHandler)
	s.router.OPTIONS("/new-post", s.preflightHandler)
	s.router.OPTIONS("/post-details/:id", s.preflightHandler)

	s.router.GET("/", s.homePageHandler)
	s.router.GET("/new-post", s.getNewPostPageHandler)
	s.router.GET("/post-details/:id", s.postDetailsHandler)
	s.router.POST("/new-post", s.postNewPostHandler)
}

func setHeaders(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
	(*w).Header().Set("Access-Control-Allow-Methods", "GET, POST, PATCH, PUT, DELETE, OPTIONS'")
	(*w).Header().Set("Access-Control-Allow-Headers", "Origin, Content-Type")
}

func (s *RESTServer) homePageHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	posts, err := s.dbClient.ListAllPosts()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	setHeaders(&w)
	html.HomePage(w, html.HomePageParams{Posts: posts})
}

func (s *RESTServer) getNewPostPageHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	p := html.NewPostDetails{}
	setHeaders(&w)
	html.NewPost(w, p)
}

func (s *RESTServer) postNewPostHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	newPost := &repository.CreatePost{}
	decoder := json.NewDecoder(r.Body)
	if err := decoder.Decode(newPost); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	newId, err := s.dbClient.InsertPost(newPost)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	setHeaders(&w)
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

	setHeaders(&w)
	html.ShowPostDetails(w, postDetails)
}

func (s *RESTServer) preflightHandler(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	setHeaders(&w)
	w.WriteHeader(http.StatusOK)
}
