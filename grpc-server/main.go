package main

import (
	"bytes"
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	"github.com/Faris-Topic/html-renderer/internal/html"
	"github.com/Faris-Topic/html-renderer/internal/repository"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/examples/data"

	forum_proto "github.com/Faris-Topic/html-renderer/internal/grpc/proto"
)

var (
	tls        = flag.Bool("tls", false, "Connection uses TLS if true, else plain TCP")
	certFile   = flag.String("cert_file", "", "The TLS cert file")
	keyFile    = flag.String("key_file", "", "The TLS key file")
	port       = flag.Int("port", 9090, "The server port")
)

type ForumServer struct {
	dbClient *repository.ForumClient
	forum_proto.UnimplementedForumRendererServer
}

func main() {
	dbClient, err := repository.InitClient("mongodb://localhost:27017")
	if err != nil {
		panic(err)
	}
	defer dbClient.Disconnect()

	server := ForumServer{
		dbClient: dbClient,
	}

	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	var opts []grpc.ServerOption
	if *tls {
		if *certFile == "" {
			*certFile = data.Path("x509/server_cert.pem")
		}
		if *keyFile == "" {
			*keyFile = data.Path("x509/server_key.pem")
		}
		creds, err := credentials.NewServerTLSFromFile(*certFile, *keyFile)
		if err != nil {
			log.Fatalf("Failed to generate credentials: %v", err)
		}
		opts = []grpc.ServerOption{grpc.Creds(creds)}
	}
	grpcServer := grpc.NewServer(opts...)
	forum_proto.RegisterForumRendererServer(grpcServer, &server)
	reflection.Register(grpcServer)
	err = grpcServer.Serve(lis)
	if err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

func (s *ForumServer) GetHomePage(ctx context.Context, req *forum_proto.EmptyRequest) (*forum_proto.HTMLResponse, error) {
	posts, err := s.dbClient.ListAllPosts()
	if err != nil {
		return nil, err
	}
	buffer := new(bytes.Buffer)
	err = html.HomePage(buffer, html.HomePageParams{Posts: posts})
	return &forum_proto.HTMLResponse{HtmlFile: buffer.Bytes()}, err

}

func (s *ForumServer) GetNewPostPage(
	ctx context.Context, 
	req *forum_proto.EmptyRequest)	(*forum_proto.HTMLResponse, error) {
	buffer := new(bytes.Buffer)
	err := html.NewPost(buffer, html.NewPostDetails{})
	return &forum_proto.HTMLResponse{HtmlFile: buffer.Bytes()}, err
}

func (s *ForumServer) CreateNewPost(ctx context.Context, req *forum_proto.CreatePostRequest) (*forum_proto.HTMLResponse, error) {
	createPost := repository.CreatePostFromProto(req)
	postId, err := s.dbClient.InsertPost(createPost)
	if err != nil {
		return nil, err
	}
	post, err := s.dbClient.GetPostById(postId)
	if err != nil {
		return nil, err
	}

	buffer := new(bytes.Buffer)
	err = html.ShowPostDetails(buffer, post)
	return &forum_proto.HTMLResponse{HtmlFile: buffer.Bytes()}, err
}

func (s *ForumServer) GetPost(ctx context.Context, req *forum_proto.GetPostRequest) (*forum_proto.HTMLResponse, error) {
	id := req.Id
	post, err := s.dbClient.GetPostById(id)
	if err != nil {
		return nil, err
	}
	buffer := new(bytes.Buffer)
	err = html.ShowPostDetails(buffer, post)
	return &forum_proto.HTMLResponse{HtmlFile: buffer.Bytes()}, err
}
