#!/usr/bin/python
import urllib2
import json
import array
from DB_Manager import DBManager
from bson.objectid import ObjectId

class FrontEnd:
	def __init__(self):
		self.remotes = []
		response = urllib2.urlopen('http://localhost:5000/list')
		contents = response.read()
		self.remotes = json.loads(contents)	
	
	def getHTML(self):
		HTMLString = ""
		HTMLString += "<h2>Frontend</h2>"		
		HTMLString += "<table style=\"width:50%\">"
		HTMLString+="<tr>"
		HTMLString+="<th> Name </th>"
		HTMLString+="<th> Surname </th>"
		HTMLString+="<th> Age </th>"
		HTMLString+="<th> Actions </th>"
		HTMLString+="</tr>"
		for result in self.remotes:
			HTMLString+="<tr><form action=\"/frontend\">"
			HTMLString+="<input name=\"_id\" type=\"hidden\" value ="+ str(result["_id"]) +">"			
			HTMLString+="<td><input name=\"name\" type=\"text\" value ="+ result["name"] +"></td>"
			HTMLString+="<td><input name=\"surname\" type=\"text\" value ="+ result["surname"] +"></td>"
			HTMLString+="<td><input name=\"age\" type=\"text\" value ="+ str(result["age"]) +"></td>"
			HTMLString+="<td><input name = \"action\" type=\"submit\" value =\"Update\">"
			HTMLString+="<input name = \"action\" type=\"submit\" value =\"Delete\"></td>"
			HTMLString+="</form></tr>"
		
		HTMLString+="<tr><form action=\"/frontend\">"
		HTMLString+="<td><input name=\"name\" type=\"text\"></td>"
		HTMLString+="<td><input name=\"surname\" type=\"text\"></td>"
		HTMLString+="<td><input name=\"age\" type=\"text\"></td>"
		HTMLString+="<td colspan=\"2\"><input name = \"action\" type=\"submit\" value =\"Create\" style=\"width:100%\"></td>"
		HTMLString+="</form></tr>"
		HTMLString += "</table>"
		return HTMLString

