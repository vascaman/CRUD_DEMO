#!/usr/bin/python
from flask import Flask
from flask import redirect
from flask import request
from DB_Manager import DBManager
from listView import ListView
from frontend import FrontEnd
from bson.objectid import ObjectId
from user import checkUserDict
import urllib2
import json

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
	return str(returnValue.inserted_id)

@app.route('/update')
def update():
	print("updating")
	
	if checkUserDict(request.args) == False:
		print "malformed request"
		return "malformed request"	
	print("updating")
	dbManager = DBManager()
	requestDict = request.args
	returnValue = dbManager.update("Users", requestDict)
	return str(returnValue.modified_count)

@app.route('/delete')
def delete():
	
	if "_id" in request.args == False:
		return "malformed request";

	dbManager = DBManager()
	requestDict = {"_id":ObjectId(request.args["_id"])}
	returnValue = dbManager.delete("Users", requestDict)
	return str(returnValue.deleted_count)

@app.route('/find')
def find():
	
	if "_id" in request.args == False:
		return "malformed request";

	dbManager = DBManager()
	requestDict = {"_id":ObjectId(request.args["_id"])}
	returnValue = dbManager.find("Users", requestDict)
	return str(returnValue)

@app.route('/list')
def list():
	returnObject=[]
	dbManager = DBManager()
	returnValue = dbManager.findAll("Users")
	for record in returnValue:
		recordDict={}
		for key in record.keys():	
			if key == "_id":
				recordDict[key] = str(ObjectId(record[key]))
			else:
				recordDict[key] = record[key]
		returnObject.append(recordDict)
		
	jsonList = json.dumps(returnObject)
	return jsonList

@app.route('/viewlist')
def viewList():
	l = ListView("Users")
	return l.getHTML()

@app.route('/frontend', methods=['GET', 'POST'])
def frontend():
	args = request.args.to_dict()
	
	if "action" in args:
		action = args["action"]
		args.pop("action")
		request.args = args

		if action == "Create":
			callCreate(args)
		
		if action == "Delete":
			callDelete(args)

		if action == "Update":
			callUpdate(args)

		return redirect("/frontend")

	frontEnd = FrontEnd()
	return frontEnd.getHTML()

def callUpdate(requestDict):
	callRemoteAPI("update", requestDict)

def callCreate(requestDict):
	callRemoteAPI("create", requestDict)

def callDelete(requestDict):
	callRemoteAPI("delete", requestDict)

def callRemoteAPI(operation, requestDict):
	remoteServer = "http://localhost:5000/"
	args="?"
	for key in requestDict:
		args+=key+"="+requestDict[key]+"&"
	completeRequest = remoteServer+operation+args
	response = urllib2.urlopen(completeRequest)


