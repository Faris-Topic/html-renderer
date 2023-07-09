import requests
import time

server_url = input("Enter server URL: ")
postId = input("Enter post Id to get details: ")
numOfRuns = input("Enter number of runs: ")

long_body = " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida cursus eros, non pretium felis molestie quis. Aliquam erat volutpat. Etiam quis ex eros. In et ipsum eu leo fringilla tempor vitae sit amet turpis. Donec imperdiet magna sed rhoncus mattis. Aliquam lacinia lobortis tortor, at suscipit tortor porta non. Donec in augue nunc. Morbi pharetra pellentesque lorem in iaculis. Nunc nec ultrices felis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. \
Ut tellus elit, blandit in molestie vel, porttitor suscipit diam. Quisque in commodo augue. Integer varius sapien risus, at lobortis orci pharetra vel. Suspendisse fermentum odio ac iaculis dignissim. Vestibulum tincidunt libero est, id accumsan libero aliquet nec. Proin condimentum purus sit amet accumsan ultrices. Suspendisse potenti. In porttitor ante quis ligula pretium, at iaculis urna ornare. Pellentesque et nibh volutpat neque mattis pulvinar. Proin et velit rhoncus, luctus tellus pretium, pellentesque eros. "


def test_get_endpoints(endpoint, API_name):
    url = server_url + endpoint
    
    start_time = time.time_ns()   
    response = requests.get(url, params=None)
    end_time = time.time_ns() 
    elapsed_time = (end_time - start_time) / 1000000  
    payload_size = len(response.content)

    # Print the results
    print('Function {name}: API Call Time: {time:.2f} milliseconds'.format(name=API_name, time=elapsed_time))
    print('Function {name}: Payload Size: {size} bytes'.format(name=API_name ,size=payload_size))
    
    return elapsed_time, payload_size

def test_post_endpoints(endpoint, payload, API_name):
    url = server_url + endpoint
    
    start_time = time.time_ns() 
    response = requests.post(url, params=payload)
    end_time = time.time_ns() 
    elapsed_time = (end_time - start_time) / 1000000  
    payload_size = len(response.content)
    payload_str = str(payload)

    # Get the size of the payload in bytes
    request_size = len(payload_str.encode('utf-8'))

    # Print the results
    print('Function {name}: API Call Time: {time:.2f} milliseconds'.format(name=API_name, time=elapsed_time))
    print('Function {name}: Payload Size: {size} bytes'.format(name=API_name ,size=payload_size))
    return elapsed_time, payload_size, request_size


# Test HomePage
homePageResults = []
for i in range(int(numOfRuns)):
    homePageResults.append(test_get_endpoints('/', 'HomePage'))
average_time = sum([x[0] for x in homePageResults]) / len(homePageResults)
average_size = sum([x[1] for x in homePageResults]) / len(homePageResults)
print('Function HomePage: Average API Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function HomePage: Average Payload Size: {size} bytes\n\n'.format(size=average_size))

# Test GetNewPostPage
newPostPageResults = []
for i in range(int(numOfRuns)):
    newPostPageResults.append(test_get_endpoints('/new-post', 'GetNewPostPage'))
average_time = sum([x[0] for x in newPostPageResults]) / len(newPostPageResults)
average_size = sum([x[1] for x in newPostPageResults]) / len(newPostPageResults)
print('Function GetNewPostPage: Average API Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function GetNewPostPage: Average Payload Size: {size} bytes\n\n'.format(size=average_size))

# Test GetPostDetails
postDetailsResults = []
for i in range(int(numOfRuns)):
    postDetailsResults.append(test_get_endpoints('/post-details/{postId}'.format(postId=postId), 'GetPostDetails'))
average_time = sum([x[0] for x in postDetailsResults]) / len(postDetailsResults)
average_size = sum([x[1] for x in postDetailsResults]) / len(postDetailsResults)
print('Function GetPostDetails: Average API Call Time: {time:.2f} milliseconds'.format(time=average_time))
print('Function GetPostDetails: Average Payload Size: {size} bytes\n\n'.format(size=average_size))

# Test CreateNewPost
#postPostResults = []   
#for i in range(int(numOfRuns)):
#    postPostResults.append(test_post_endpoints('/new-post', {'title': 'Test Title', 'body': long_body}, 'CreateNewPost'))
#average_time = sum([x[0] for x in postPostResults]) / len(postPostResults)
#average_size = sum([x[1] for x in postPostResults]) / len(postPostResults)
#print('Function CreateNewPost: Average API Call Time: {time:.2f} milliseconds'.format(time=average_time))
#print('Function CreateNewPost: Average Request Size: {size} bytes'.format(size=average_request_size))
#print('Function CreateNewPost: Average Payload Size: {size} bytes\n\n'.format(size=average_size))
    
 
