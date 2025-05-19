from enum import Enum
from typing import Optional
from mongo_connection import SuperheroesDatabase

class UserRepository:

    class House(Enum):
        DC = "dc"
        MARVEL = "marvel"

    def __init__(self, house : House):
        self.collection = SuperheroesDatabase.get_db()[house.value]
    
    def insert(self, hero : str, name : str = "", 
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