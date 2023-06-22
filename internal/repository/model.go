package repository

type PostDetails struct {
	Id    string `bson:"_id"`
	Title string `bson:"title"`
	Body  string `bson:"body"`
}

type CreatePost struct {
	Title string `bson:"title"`
	Body  string `bson:"body"`
}