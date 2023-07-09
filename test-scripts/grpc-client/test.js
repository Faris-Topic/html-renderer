const { EmptyRequest, GetPostRequest, CreatePostRequest } = require('./forum_pb.js')
const { ForumRendererClient } = require('./forum_grpc_web_pb.js')

var forumService = new ForumRendererClient('http://localhost:8080');
const NUMBER_OF_CALLS = 100;
const ID = "649e94a76363182f0f83120e";

let totalElapsedTime = 0;
let totalPayloadSize = 0;

const title = "Test title";
const body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida cursus eros, non pretium felis molestie quis. Aliquam erat volutpat. Etiam quis ex eros. In et ipsum eu leo fringilla tempor vitae sit amet turpis. Donec imperdiet magna sed rhoncus mattis. Aliquam lacinia lobortis tortor, at suscipit tortor porta non. Donec in augue nunc. Morbi pharetra pellentesque lorem in iaculis. Nunc nec ultrices felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. \
Ut tellus elit, blandit in molestie vel, porttitor suscipit diam. Quisque in commodo augue. Integer varius sapien risus, at lobortis orci pharetra vel. Suspendisse fermentum odio ac iaculis dignissim. Vestibulum tincidunt libero est, id accumsan libero aliquet nec. Proin condimentum purus sit amet accumsan ultrices. Suspendisse potenti. In porttitor ante quis ligula pretium, at iaculis urna ornare. Pellentesque et nibh volutpat neque mattis pulvinar. Proin et velit rhoncus, luctus tellus pretium, pellentesque eros. ";

function TestHomePageTime() {
    return new Promise((resolve, reject) => {
        const startTime = performance.now();

        forumService.getHomePage(new EmptyRequest(), {}, (err, response) => {
            if (err) {
                reject(err);
            } else {
                const endTime = performance.now();
                const elapsedTime = endTime - startTime;
                totalElapsedTime += elapsedTime;

                const responseSize = JSON.stringify(response.toObject()).length;
                totalPayloadSize += responseSize;

                // Print individual API call time
                //console.log(`API call took ${elapsedTime} milliseconds`);
                //console.log(`Response payload size: ${responseSize} bytes`);

                resolve(response);
            }
        });
    });
}


function TestNewPostFormTime() {
    return new Promise((resolve, reject) => {
        const startTime = performance.now();

        forumService.getNewPostPage(new EmptyRequest(), {}, (err, response) => {
            if (err) {
                reject(err);
            } else {
                const endTime = performance.now();
                const elapsedTime = endTime - startTime;
                totalElapsedTime += elapsedTime;

                const responseSize = response.getHtmlfile().length;
                totalPayloadSize += responseSize;

                // Print individual API call time
                //console.log(`API call took ${elapsedTime} milliseconds`);
                //console.log(`Response payload size: ${responseSize} bytes`);

                resolve(response);
            }
        });
    });
}


function TestGetPostDetailsTime() {
    return new Promise((resolve, reject) => {
        getPostRequest = new GetPostRequest();
        getPostRequest.setId(ID);

        const startTime = performance.now();
        forumService.getPost(getPostRequest, {}, (err, response) => {
            if (err) {
                reject(err);
            } else {
                const endTime = performance.now();
                const elapsedTime = endTime - startTime;
                totalElapsedTime += elapsedTime;

                const responseSize = response.getHtmlfile().length;
                totalPayloadSize += responseSize;

                // Print individual API call time
                //console.log(`API call took ${elapsedTime} milliseconds`);
                //console.log(`Response payload size: ${responseSize} bytes`);

                resolve(response);
            }
        });
    });
}

function TestCreateNewPostTime() {
    return new Promise((resolve, reject) => {
        newPostRequest = new CreatePostRequest();
        newPostRequest.setTitle(title);
        newPostRequest.setBody(body);

        const startTime = performance.now();
        forumService.createNewPost(newPostRequest, {}, (err, response) => {
            if (err) {
                reject(err);
            } else {
                const endTime = performance.now();
                const elapsedTime = endTime - startTime;
                totalElapsedTime += elapsedTime;

                const responseSize = response.getHtmlfile().length;
                totalPayloadSize += responseSize;

                // Print individual API call time
                //console.log(`API call took ${elapsedTime} milliseconds`);
                //console.log(`Response payload size: ${responseSize} bytes`);

                resolve(response);
            }
        });
    });
}

function measureAllRequestsTime(call) {
    const promises = [];

    for (let i = 0; i < NUMBER_OF_CALLS; i++) {
        promises.push(call());
    }

    return Promise.all(promises)
        .then(() => {
            const averageTime = totalElapsedTime / NUMBER_OF_CALLS;
            const averagePayloadSize = totalPayloadSize / NUMBER_OF_CALLS;

            // Print average API call time
            console.log(`Average API call time: ${averageTime} milliseconds`);
            console.log(`Average response payload size: ${averagePayloadSize} bytes`);
        })
        .catch(err => {
            console.error('API calls failed:', err);
        });
}

measureAllRequestsTime(TestHomePageTime);
//measureAllRequestsTime(TestNewPostFormTime);
//measureAllRequestsTime(TestGetPostDetailsTime);
//measureAllRequestsTime(TestCreateNewPostTime);