from pymongo import MongoClient

db_connection = input("Enter db connection: ")
docNumbers = int(input("Enter number of documents to be created: "))

client = MongoClient(db_connection)
db = client['forum_example']  
collection = db['forum_posts'] 

documents = []

for i in range(docNumbers):
    document = {"title": "Post title" + str(i), "body": "Post body" + str(i) + "\n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum diam nisl, volutpat ut sollicitudin et, tristique a risus. Duis feugiat congue ipsum, sit amet vehicula tortor gravida a. Morbi pretium cursus volutpat. Ut posuere augue et scelerisque sollicitudin. Sed interdum ligula in venenatis dapibus. Aliquam congue in arcu eget vehicula. Curabitur hendrerit vulputate tellus, quis hendrerit est. Donec a vestibulum enim. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed ultricies augue eget tortor fermentum, ut gravida elit porta. Pellentesque tincidunt at dolor eu porttitor. Duis non mauris sagittis, fermentum neque sit amet, vulputate risus. "}
    documents.append(document)

collection.insert_many(documents)

client.close()
