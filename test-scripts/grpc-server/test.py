import grpc
import time

import forum_pb2
import forum_pb2_grpc

MAX_MESSAGE_LENGTH = 10485760

server_url = input("Enter grpc service URL: ")
postId = input("Enter post Id to get details: ")
numOfRuns = input("Enter number of runs: ")

long_body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida cursus eros, non pretium felis molestie quis. Aliquam erat volutpat. Etiam quis ex eros. In et ipsum eu leo fringilla tempor vitae sit amet turpis. Donec imperdiet magna sed rhoncus mattis. Aliquam lacinia lobortis tortor, at suscipit tortor porta non. Donec in augue nunc. Morbi pharetra pellentesque lorem in iaculis. Nunc nec ultrices felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. \
Ut tellus elit, blandit in molestie vel, porttitor suscipit diam. Quisque in commodo augue. Integer varius sapien risus, at lobortis orci pharetra vel. Suspendisse fermentum odio ac iaculis dignissim. Vestibulum tincidunt libero est, id accumsan libero aliquet nec. Proin condimentum purus sit amet accumsan ultrices. Suspendisse potenti. In porttitor ante quis ligula pretium, at iaculis urna ornare. Pellentesque et nibh volutpat neque mattis pulvinar. Proin et velit rhoncus, luctus tellus pretium, pellentesque eros. "


channel = grpc.insecure_channel(server_url,   options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ],)
stub = forum_pb2_grpc.ForumRendererStub(channel)

def make_grpc_call(call_name, call, request):
    start_time = time.time_ns()   
    response = call(request)
    end_time = time.time_ns() 
    elapsed_time = (end_time - start_time) / 1000000  
    response_size = len(response.SerializeToString())
    request_size = len(request.SerializeToString())

    # Print the results
    print('Function {name}: gRPC Call Time: {time:.2f} milliseconds'.format(name=call_name, time=elapsed_time))
    print('Function {name}: response Size: {size} bytes'.format(name=call_name ,size=response_size))
    print('Function {name}: request Size: {size} bytes'.format(name=call_name ,size=request_size))
    return elapsed_time, response_size, request_size


# test HomePage
homePageResults = []
for i in range(int(numOfRuns)):
    homePageResults.append(make_grpc_call('HomePage', stub.GetHomePage, forum_pb2.EmptyRequest()))
average_time = sum([x[0] for x in homePageResults]) / len(homePageResults)
average_response_size = sum([x[1] for x in homePageResults]) / len(homePageResults) 
average_request_size = sum([x[2] for x in homePageResults]) / len(homePageResults)
print('Function HomePage: Average gRPC Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function HomePage: Average request Size: {size} bytes'.format(size=average_request_size))
print('Function HomePage: Average response Size: {size} bytes\n\n'.format(size=average_response_size))

# test GetNewPostPage
newPostPageResults = []
for i in range(int(numOfRuns)):
    newPostPageResults.append(make_grpc_call('GetNewPostPage', stub.GetNewPostPage, forum_pb2.EmptyRequest()))
average_time = sum([x[0] for x in newPostPageResults]) / len(newPostPageResults)
average_response_size = sum([x[1] for x in newPostPageResults]) / len(newPostPageResults)
average_request_size = sum([x[2] for x in newPostPageResults]) / len(newPostPageResults)
print('Function GetNewPostPage: Average gRPC Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function GetNewPostPage: Average request Size: {size} bytes'.format(size=average_request_size))
print('Function GetNewPostPage: Average response Size: {size} bytes\n\n'.format(size=average_response_size))

# test GetPostDetails
postDetailsResults = []
for i in range(int(numOfRuns)):
    postDetailsResults.append(make_grpc_call('GetPostDetails', stub.GetPost, forum_pb2.GetPostRequest(id=postId)))
average_time = sum([x[0] for x in postDetailsResults]) / len(postDetailsResults)
average_response_size = sum([x[1] for x in postDetailsResults]) / len(postDetailsResults)
average_request_size = sum([x[2] for x in postDetailsResults]) / len(postDetailsResults)
print('Function GetPostDetails: Average gRPC Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function GetPostDetails: Average request Size: {size} bytes'.format(size=average_request_size))
print('Function GetPostDetails: Average response Size: {size} bytes\n\n'.format(size=average_response_size))
    
# test CreateNewPost
#postPostResults = []
#for i in range(int(numOfRuns)):
#    postPostResults.append(make_grpc_call('CreateNewPost', stub.CreateNewPost, forum_pb2.CreatePostRequest(title='Test Title', body=long_body)))
#average_time = sum([x[0] for x in postPostResults]) / len(postPostResults)
#average_response_size = sum([x[1] for x in postPostResults]) / len(postPostResults)
#average_request_size = sum([x[2] for x in postPostResults]) / len(postPostResults)
#print('Function CreateNewPost: Average gRPC Call Time: {time:.2f} milliseconds'.format(time=average_time))
#print('Function CreateNewPost: Average request Size: {size} bytes'.format(size=average_request_size))
#print('Function CreateNewPost: Average response Size: {size} bytes\n\n'.format(size=average_response_size))
