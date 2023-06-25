const { EmptyRequest, GetPostRequest, CreatePostRequest } = require('./forum_pb.js')
const { ForumRendererClient } = require('./forum_grpc_web_pb.js')

var forumService = new ForumRendererClient('http://localhost:8080');

function renderResponse(message) {
    var decodedStringB64 = atob(message);
    document.getElementById('parent_html').innerHTML = decodedStringB64;

    var script = document.createElement("script");
    script.src = "./dist/main.js";
    
    document.body.appendChild(script)

    registerListeners();
}

function homePage() {
    forumService.getHomePage(new EmptyRequest(), {}, (err, response) => {
        if (err != null) {
            console.log(err);
        }
        message = response.getHtmlfile_asB64();
        renderResponse(message);
    });
}

function getPostDetails(postId) {
    getPostRequest = new GetPostRequest();
    getPostRequest.setId(postId);

    forumService.getPost(getPostRequest, {}, (err, response) => {
        if (err != null) {
            console.log(err);
        }
        message = response.getHtmlfile_asB64();
        renderResponse(message);
    });
}

window.onload = function () {
    homePage();
};

function registerListeners() {

    var card = document.querySelectorAll(".post-list");
    if (card != null) {
        card.forEach((c) => {
            c.addEventListener("click", () => {
                getPostDetails(c.id);
            });
        });
    }

    var homePageLink = document.getElementById("homeLink");
    if (homePageLink != null) {
        homePageLink.addEventListener("click", (e) => {
            e.preventDefault();
            homePage();
        });
    }

    var form = document.getElementById("new-post-form");
    if (form != null) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();

            const formData = new FormData(form);
            const title = formData.get("post_title");
            const body = formData.get("post_body");

            newPostRequest = new CreatePostRequest();
            newPostRequest.setTitle(title);
            newPostRequest.setBody(body);

            forumService.createNewPost(newPostRequest, {}, (err, response) => {
                if (err != null) {
                    console.log(err);
                }
                message = response.getHtmlfile_asB64();
                renderResponse(message);
            });
        });
    }

    var newPostLink = document.getElementById("newPostLink");
    if (newPostLink != null) {
        newPostLink.addEventListener("click", (e) => {
            e.preventDefault();
            forumService.getNewPostPage(new EmptyRequest(), {}, (err, response) => {
                if (err != null) {
                    console.log(err);
                }
                message = response.getHtmlfile_asB64();
                renderResponse(message);
            });
        });
    }
};
