from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_default_database()

blog = db["posts"]

post ={
'title':'REP C4E',
'author':'Dattran',
'content':'''Trẻ không chơi già đổ đốn !
                             <<-quote->>'''
}

blog.insert_one(post)
