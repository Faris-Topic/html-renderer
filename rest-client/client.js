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
    axios.get(serverAddress)
        .then(
            data => {
                renderResponse(data.data);
            }
        ).catch(error => { console.log(error) });
}

function getPostDetails(postId) {
    axios.get(serverAddress + "post-details/" + postId)
        .then(
            data => {
                renderResponse(data.data);
            }
        ).catch(error => { console.log(error) });
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
            console.log("data is" + formData)
            axios.post(serverAddress + "new-post", {
                title: formData.get("post_title"),
                body: formData.get("post_body")
            })
            .then(
                data => {
                    renderResponse(data.data);
                }
            ).catch(error => { console.log(error) });
        });
    }

    var newPostLink = document.getElementById("newPostLink");
    if (newPostLink != null) {
        newPostLink.addEventListener("click", (e) => {
            e.preventDefault();
            axios.get(serverAddress + "new-post")
                .then(
                    data => {
                        renderResponse(data.data);
                    }
                ).catch(error => { console.log(error) });
        });
    }
};
