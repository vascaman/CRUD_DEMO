#!/usr/bin/python
from flask import Flask
from flask import redirect
from flask import request
from DB_Manager import DBManager
from listView import ListView
from bson.objectid import ObjectId
from user import checkUserDict

DEBUG = True

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/operation', methods=['GET', 'POST'])
def operation():
	action = request.args["action"]
	args = request.args.to_dict()
	args.pop("action")
	request.args = args
	
	#if checkUserDict(args) == False:
	#	return redirect("/viewlist")

	if action == "Create":
		create()
	
	if action == "Delete":
		delete()

	if action == "Update":
		update()

	return redirect("/viewlist")	
	
@app.route('/create', methods=['GET', 'POST'])
def create():
	requestDict={}
	
	if checkUserDict(request.args) == False:
		return "malformed requessst";

	for key in request.args.keys():
		requestDict[key] = request.args[key]
	dbManager = DBManager()
	returnValue = dbManager.insert("Users", requestDict)
	return str(returnValue.inserted_id);

@app.route('/update')
def update():

	if checkUserDict(request.args) == False:
		return "malformed request";	

	dbManager = DBManager()
	requestDict = request.args
	returnValue = dbManager.update("Users", requestDict)
	return str(returnValue.modified_count);

@app.route('/delete')
def delete():
	
	if "_id" in request.args == False:
		return "malformed request";

	dbManager = DBManager()
	requestDict = {"_id":ObjectId(request.args["_id"])}
	returnValue = dbManager.delete("Users", requestDict)
	return str(returnValue.deleted_count);

@app.route('/find')
def find():
	
	if "_id" in request.args == False:
		return "malformed request";

	dbManager = DBManager()
	requestDict = {"_id":ObjectId(request.args["_id"])}
	returnValue = dbManager.find("Users", requestDict)
	return str(returnValue);

@app.route('/list')
def list():
	dbManager = DBManager()
	returnValue = dbManager.findAll("Users")
	x = []
	for row in returnValue:
		x.append(row)
	print(x)
	return str(x)

@app.route('/viewlist')
def viewList():
	l = ListView("Users")
	return l.getHTML()
