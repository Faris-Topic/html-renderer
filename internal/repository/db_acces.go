package repository

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"gopkg.in/mgo.v2/bson"
)

const (
	collectionName = "forum_posts"
	databaseName   = "forum_example"
)

type ForumClient struct {
	client     *mongo.Client
	collection *mongo.Collection
}

func InitClient(mongoEndpoint string) (*ForumClient, error) {
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(mongoEndpoint))
	if err != nil {
		return nil, err
	}

	postsCollection := client.Database(databaseName).Collection(collectionName)

	return &ForumClient{
		client:     client,
		collection: postsCollection,
	}, nil
}

func (fc *ForumClient) Disconnect() {
	fc.client.Disconnect(context.Background())
}

func (fc *ForumClient) InsertPost(post *CreatePost) (string, error) {

	result, err := fc.collection.InsertOne(context.TODO(), post)
	// check for errors in the insertion
	if err != nil {
		return "", err
	}

	// get the inserted id
	id, ok := result.InsertedID.(primitive.ObjectID)
	if !ok {
		return "", fmt.Errorf("could not convert inserted id to primitive.ObjectID, is of type %T", result.InsertedID)
	}

	return id.Hex(), nil
}

func (fc *ForumClient) GetPostById(id string) (PostDetails, error) {
	var post PostDetails

	// create a filter for the post id
	objectId, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return PostDetails{}, err
	}

	filter := bson.M{"_id": objectId}

	err = fc.collection.FindOne(context.TODO(), filter).Decode(&post)
	if err != nil {
		return PostDetails{}, err
	}

	return post, nil
}

func (fc *ForumClient) ListAllPosts() ([]PostDetails, error) {
	var posts []PostDetails

	// get all posts
	cursor, err := fc.collection.Find(context.Background(), bson.M{})
	if err != nil {
		return nil, err
	}

	// iterate over the cursor
	for cursor.Next(context.Background()) {
		var post PostDetails
		err := cursor.Decode(&post)
		if err != nil {
			return nil, err
		}

		posts = append(posts, post)
	}

	return posts, nil
}
