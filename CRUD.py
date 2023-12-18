#MongoDB CRUD Class
#Developer: Daulton Truett

"""
Updated on Sat Dec 12 15:27:18 2023

@author: daultontruett_snhu
CS-340: Client/Server Development
Southern New Hampshire University
"""

from pymongo import MongoClient
from bson.objectid import ObjectId


class CRUD:
    """CRUD for animals collection in MongoDB""" 
    def __init__(self, username, password, host, port, db, collection):
        self.USER = username;
        self.PASS = password;
        self.HOST = host;
        self.PORT = port;
        self.DB = db;
        self.COLLECTION = collection;

        self.client = MongoClient(f'mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}');
        self.database = self.client[self.DB];
        self.collection = self.database[self.COLLECTION];
    
    
    def create(self, insertData):
        """Insert a document into the DB"""
        if insertData is not None:
            self.collection.insert_one(insertData);
            return True;
        else:
            raise Exception("Unable to insert data with 'None' type into the DB.");


    def read(self, queryData):
        """Read documents from the DB"""
        animals = list(self.collection.find(queryData));
        
        if len(animals) < 1:
            print('Entry not found.');
            return animals;
        else:
            return animals;
            

    def update(self, queryData, updateData):
        """Update a document, or documents, in the DB"""
        if queryData is not None and updateData is not None:
            animalsCursor = self.read(queryData);
            
            for key, value in queryData.items():
                updateFilter = {key:value};
                
            for key, value in updateData.items():
                newValues = {"$set": {key:value}}
                
            if len(animalsCursor) == 1:
                result = self.collection.update_one(updateFilter, newValues);
                return result.modified_count;
                
            elif len(animalsCursor) > 1:
                result = self.collection.update_many(updateFilter, newValues);
                return result.modified_count;


    def delete(self, queryData):
        """Delete a document, or documents, from the DB"""
        if queryData is not None:
            animalsCursor = self.read(queryData);
    
            for key, value in queryData.items():
                deleteFilter = {key:value};
                
            if len(animalsCursor) == 1:
                result = self.collection.delete_one(deleteFilter);
                return result.deleted_count;
            
            elif len(animalsCursor) > 1:
                result = self.collection.delete_many(deleteFilter); 
                return result.deleted_count;

