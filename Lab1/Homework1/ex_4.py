from pymongo import MongoClient
from matplotlib import pyplot

url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(url)
db = client.get_default_database()

blog = db["customers"]

all_customers = blog.find()

# print(all_customers[i]) #collection là list chứa các dict con

events = 0
advertisements = 0
word_of_mouth = 0
for information in all_customers: # cho information truy cập vào từng dist trong list
     if (information["ref"] == "events"):
         events += 1
     elif(information["ref"] == "ads"):
         advertisements += 1
     elif(information["ref"] == "wom"):
         word_of_mouth += 1
print(events,advertisements,word_of_mouth)

#1. prepare Data
data = [events,advertisements,word_of_mouth]

#2. prepare Labels
field_name = ["events","advertisements","word_of_mouth"]

#3. draw pie
pyplot.pie(data,labels = field_name, autopct="%.1f%%", shadow=True, explode=[0, 0, 0.2])
pyplot.title("PERCENTAGE OF THE CUSTOMERS AQUIRE FROM REFERENCE")
pyplot.axis("equal")
#4. show
pyplot.show()
