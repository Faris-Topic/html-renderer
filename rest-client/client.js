import axios from 'axios'

const serverAddress = "http://localhost:3000/";

function renderResponse(message) {
    document.getElementById('parent_html').innerHTML = message;

    var script = document.createElement("script");
    script.src = "./dist/main.js";

    document.body.appendChild(script)

    registerListeners();
}

function homePage() {
    const start = Date.now();
    console.log("Start time of call 'getHomePage': " + start);

    axios.get(serverAddress)
        .then(
            data => {
                const end = Date.now();
                console.log("End time of call 'getHomePage': " + end);

                renderResponse(data.data);
                console.log("Difference: " + (end - start));
            }
        ).catch(error => { console.log(error) });
}

function getPostDetails(postId) {
    const start = Date.now();
    console.log("Start time of call 'getPost': " + start);

    axios.get(serverAddress + "post-details/" + postId)
        .then(
            data => {
                const end = Date.now();
                console.log("End time of call 'getPost': " + end);

                renderResponse(data.data);
                console.log("Difference: " + (end - start));
            }
        ).catch(error => { console.log(error) });
}

function getNewPostForm() {
    const start = Date.now();
    console.log("Start time of call 'getNewPostPage': " + start);

    axios.get(serverAddress + "new-post")
    .then(
        data => {
            const end = Date.now();
            console.log("End time of call 'getNewPostPage': " + end);

            renderResponse(data.data);
            console.log("Difference: " + (end - start));
        }
    ).catch(error => { console.log(error) });
}

window.onload = function () {
    homePage();
};

function createNewPost(form) {
    const start = Date.now();
    console.log("Start time of call 'createNewPost': " + start);

    const formData = new FormData(form);
    const title = formData.get("post_title");
    const body = formData.get("post_body");

    axios.post(serverAddress + "new-post", {
        title: title,
        body: body
    })
    .then(
        data => {
            const end = Date.now();
            console.log("End time of call 'createNewPost': " + end);

            renderResponse(data.data);
            console.log("Difference: " + (end - start));
        }
    ).catch(error => { console.log(error) });
}

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
