#!/usr/bin/python
import pymongo
from bson.objectid import ObjectId

class DBManager:
	def __init__(self):
		self.client = pymongo.MongoClient("mongodb://localhost:27017/")
		self.DB = self.client["CRUD_DEMO_DB"]

	def setTable(self, _tableName):
		self.tableName = tableName
		self.mycol = self.DB[self.tableName]

	def insert(self, tableName, objectDict):
		table = self.DB[tableName]
		print(objectDict)
		result = table.insert_one(objectDict)
		return result

	def printTable(self, tableName):
		table = self.DB[tableName]
		for resultDict in table.find():
			print(resultDict)
	
	def update(self, tableName, _objectDict):
		objectDict = _objectDict.copy()
		table = self.DB[tableName]
		myquery = { "_id": ObjectId(objectDict["_id"]) }
		objectDict.pop("_id")
		newvalues = { "$set": objectDict }
		returnResult = table.update_one(myquery, newvalues)
		return returnResult
		
	def delete(self, tableName, objectDict):
		table = self.DB[tableName]
		return table.delete_one(objectDict)

	def find(self, tableName, _objectDict):
		objectDict = _objectDict.copy()
		objectDict["_id"] = ObjectId(objectDict["_id"])
		table = self.DB[tableName]
		return table.find_one(objectDict)

	def findAll(self, tableName):
		table = self.DB[tableName]
		return table.find()
