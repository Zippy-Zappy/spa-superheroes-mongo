from enum import Enum
from typing import Optional
from mongo_connection import SuperheroesDatabase
from bson.objectid import ObjectId

class UserRepository:

    class House(Enum):
        DC = "dc"
        MARVEL = "marvel"

    def __init__(self, house : House):
        self.collection = SuperheroesDatabase.get_db()[house.value]
    
    def insert_hero(self, hero : str, name : str = "", 
               year : int = 0, bio : str = "", 
               items : Optional[list[str]] = None, 
               images : Optional[list[str]] = None):

        #Empty list should not be used as default values
        #as they are created when the function is defined
        #and shared when called and items is not sent,
        #therefore reusing that empty list
        #instead of creating a new one.
        if items is None:
            items = []
        if images is None:
            images = []
        
        document = {
            "hero": hero,
            "name": name,
            "year": year,
            "bio": bio,
            "items": items,
            "images": images
        }

        result = self.collection.insert_one(document)
        return result.inserted_id
    
    def get_hero_by_name(self, hero : str) -> str:
        if hero.isspace():
            return f"Must input hero name."
        result = self.collection.find_one({"hero": hero})
        return ObjectId(result["_id"])

    def get_hero_by_id(self, id : ObjectId):
        result = self.collection.find_one({"_id": id})
        return result
    
    def update_hero(self, id : ObjectId, 
                hero : str, name : str, 
               year : int, bio : str, 
               items : list[str], 
               images : list[str]):
        new_values = {"$set": {"hero": hero, "name": name, "year": year,
                      "bio": bio, "items": items, "images": images}}
        result = self.collection.update_one({"_id": id}, new_values)
        return result.acknowledged
    
    def delete_hero(self, id : ObjectId):
        result = self.collection.delete_one({"_id": id})
        return result.acknowledged