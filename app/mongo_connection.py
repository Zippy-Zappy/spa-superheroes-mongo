import pymongo

class SuperheroesDatabase:
    _client = None
    _db = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            CONNECTION_STRING = "mongodb://localhost:27017/"    
            cls._client = pymongo.MongoClient(CONNECTION_STRING)
        return cls._client
    
    @classmethod
    def get_db(cls):
        if cls._db is None:
            cls._db = cls.get_client()["superheroes"]
        return cls._db
