package html

import (
	"embed"
	"html/template"
	"io"

	"github.com/Faris-Topic/html-renderer/internal/repository"
)

//go:embed *
var files embed.FS

var (
	home        = parse("templates/home.html")
	newPost     = parse("templates/post_edit.html")
	postDetails = parse("templates/post_details.html")
)

type HomePageParams struct {
	Posts []repository.PostDetails
}

func HomePage(w io.Writer, p HomePageParams) error {
	return home.Execute(w, p)
}

type NewPostDetails struct {
	Title string
	Body  string
}

func NewPost(w io.Writer, p NewPostDetails) error {
	return newPost.Execute(w, p)
}

func ShowPost(w io.Writer, p repository.PostDetails) error {
	return postDetails.Execute(w, p)
}

func parse(file string) *template.Template {
	return template.Must(
		template.New("layout.html").ParseFS(files, "templates/layout.html", file))
}
