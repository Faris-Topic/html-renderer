package html

import (
	"embed"
	"html/template"
	"io"
)

//go:embed *
var files embed.FS

var (
	dashboard   = parse("templates/home.html")
	profileShow = parse("templates/profile/show.html")
	profileEdit = parse("templates/profile/edit.html")
)

type DashboardParams struct {
	Title   string
	Message string
}

func Dashboard(w io.Writer, p DashboardParams) error {
	return dashboard.Execute(w, p)
}

type ProfileShowParams struct {
	Title   string
	Message string
}

func ProfileShow(w io.Writer, p ProfileShowParams) error {
	return profileShow.Execute(w, p)
}

type ProfileEditParams struct {
	Title   string
	Message string
}

func ProfileEdit(w io.Writer, p ProfileEditParams) error {
	return profileEdit.Execute(w, p)
}

func parse(file string) *template.Template {
	return template.Must(
		template.New("layout.html").ParseFS(files, "templates/layout.html", file))
}
