#!/usr/bin/python
from DB_Manager import DBManager

class ListView:
	def __init__(self, tableName):
		self.tableName = tableName
		self.dbManager = DBManager()
		
	def getHTML(self):
		HTMLString = ""
		HTMLString += "<table style=\"width:50%\">"
		HTMLString+="<tr>"
		HTMLString+="<th> Name </th>"
		HTMLString+="<th> Surname </th>"
		HTMLString+="<th> Age </th>"
		HTMLString+="<th> Actions </th>"
		HTMLString+="</tr>"
		resultDict = self.dbManager.findAll(self.tableName)
		for result in resultDict:
			HTMLString+="<tr><form action=\"/operation\">"
			HTMLString+="<input name=\"_id\" type=\"hidden\" value ="+ str(result["_id"]) +">"			
			HTMLString+="<td><input name=\"name\" type=\"text\" value ="+ result["name"] +"></td>"
			HTMLString+="<td><input name=\"surname\" type=\"text\" value ="+ result["surname"] +"></td>"
			HTMLString+="<td><input name=\"age\" type=\"text\" value ="+ str(result["age"]) +"></td>"
			HTMLString+="<td><input name = \"action\" type=\"submit\" value =\"Update\">"
			HTMLString+="<input name = \"action\" type=\"submit\" value =\"Delete\"></td>"
			HTMLString+="</form></tr>"
		
		HTMLString+="<tr><form action=\"/operation\">"
		HTMLString+="<td><input name=\"name\" type=\"text\"></td>"
		HTMLString+="<td><input name=\"surname\" type=\"text\"></td>"
		HTMLString+="<td><input name=\"age\" type=\"text\"></td>"
		HTMLString+="<td colspan=\"2\"><input name = \"action\" type=\"submit\" value =\"Create\" style=\"width:100%\"></td>"
		HTMLString+="</form></tr>"
		HTMLString += "</table>"
		return HTMLString

#l = ListView("Users")
#print(l.getHTML())
		
