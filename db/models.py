from pymongo import MongoClient
from bson.objectid import ObjectId 

uri = "mongodb+srv://Faluyi:Akindele@cluster0.ozepuyt.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['Integers_Db']
Integers = db['Integers']


class Integersdb:
    def __init__(self) -> None:
        self.collection = Integers
        
    def get_integer(self):
        return self.collection.find().limit(1)
    
    def post_integer(self, integer: int):
        return self.collection.insert_one({"value": integer}).inserted_id
        
    def replace_integer(self, prev_val_id, curr_value):
        return self.collection.find_one_and_replace({"_id":ObjectId(prev_val_id)}, {"value": curr_value})