package repository

import "github.com/Faris-Topic/html-renderer/internal/grpc/proto"

type PostDetails struct {
	Id    string `bson:"_id"`
	Title string `bson:"title"`
	Body  string `bson:"body"`
}

type CreatePost struct {
	Title string `bson:"title" json:"title"`
	Body  string `bson:"body" json:"body"`
}

func CreatePostFromProto(p *proto.CreatePostRequest) *CreatePost {
	return &CreatePost{
		Title: p.Title,
		Body:  p.Body,
	}
}
