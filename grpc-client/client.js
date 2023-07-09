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
    const start = Date.now();
    console.log("Start time of call 'getHomePage': " + start);
    forumService.getHomePage(new EmptyRequest(), {}, (err, response) => {
        if (err != null) {
            console.log(err);
        }
        const end = Date.now();
        console.log("End time of call 'getHomePage': " + end);
        
        message = response.getHtmlfile_asB64();
        renderResponse(message);
        console.log("Difference: " + (end - start));
    });
}

function getPostDetails(postId) {
    const start = Date.now();
    console.log("Start time of call 'getPost': " + start);

    getPostRequest = new GetPostRequest();
    getPostRequest.setId(postId);

    forumService.getPost(getPostRequest, {}, (err, response) => {
        if (err != null) {
            console.log(err);
        }

        const end = Date.now();
        console.log("End time of call 'getPost': " + end);

        message = response.getHtmlfile_asB64();
        renderResponse(message);

        console.log("Difference: " + (end - start));
    });
}

function getNewPostForm() {
    const start = Date.now();
    console.log("Start time of call 'getNewPostPage': " + start);

    forumService.getNewPostPage(new EmptyRequest(), {}, (err, response) => {
        if (err != null) {
            console.log(err);
        }
        const end = Date.now();
        console.log("End time of call 'getNewPostPage': " + end);

        message = response.getHtmlfile_asB64();
        renderResponse(message);
        console.log("Difference: " + (end - start));
    });
}

function createNewPost(form) {
    const start = Date.now();
    console.log("Start time of call 'createNewPost': " + start);

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
        const end = Date.now();
        console.log("End time of call 'createNewPost': " + end);

        message = response.getHtmlfile_asB64();
        renderResponse(message);
        console.log("Difference: " + (end - start));
    });
}

window.onload = function () {
    console.log("Window loaded");
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
            createNewPost(form);
        });
    }

    var newPostLink = document.getElementById("newPostLink");
    if (newPostLink != null) {
        newPostLink.addEventListener("click", (e) => {
            e.preventDefault();
            getNewPostForm();
        });
    }
};
