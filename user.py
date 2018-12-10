#!/usr/bin/python
class User:
	def __init__(self, objectDict):
		self.name = objectDict["name"]
		self.surname = objectDict["surname"]
		try:
		    self.age = int(objectDict["age"])
		except (ValueError, TypeError):
			print("age not valid")
	
	def __init__(self, name, surname, age):
		self.name = name
		self.surname = surname
		self.age = 0
		try:
		    self.age = int(age)
		except (ValueError, TypeError):
			print("age not valid")
	
	def checkParams(self):
		if len(self.name.strip()) == 0:
			return False
		if len(self.surname.strip()) == 0:
			return False
		if self.age == 0:
			return False
		return True

	def myfunc(self):
	    print("Hello my name is " + self.name)
	def save(self):
		print("save")
	def getDict(self):
		returnDict = {"name":self.name, "surname":self.surname, "age":self.age}
		return returnDict

def checkUserDict(rawDict):
	userDict={}
	userDict["name"] = rawDict["name"]
	userDict["surname"] = rawDict["surname"]
	userDict["age"] = rawDict["age"]
	if "_id" in rawDict:
		userDict["_id"] = rawDict["_id"]
	
	if "name" in rawDict == False:
		return False

	if len(userDict["name"].strip()) == 0:
		return False

	if "surname" in rawDict == False:
		return False

	if len(userDict["surname"].strip()) == 0:
		return False

	if "age" in rawDict == False:
		return False

	try:
		age = int(userDict["age"])
		if age == 0:
			return False
		userDict["age"] = age
	except (ValueError, TypeError):
		return False
	
	return True

