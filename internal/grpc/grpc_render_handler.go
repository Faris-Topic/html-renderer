package grpc_render_handler

import (
	"bytes"

	renderer_proto "github.com/Faris-Topic/html-renderer/internal/grpc/proto"
	htmlTemplates "github.com/Faris-Topic/html-renderer/internal/html"
)

func GetHomePage(renderer_proto.EmptyRequest) (renderer_proto.HTMLResponse, error) {
	var htmlAsBytes bytes.Buffer

	htmlTemplates.HomePage(&htmlAsBytes, htmlTemplates.HomePageParams{})

	return renderer_proto.HTMLResponse{
		HtmlFile: htmlAsBytes.Bytes(),
	}, nil
}
