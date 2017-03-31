import sys
import uuid
import sqlite3

class DBHelper:

	def __init__(self, path_database):
		self.__path_to_database = path_database

	def open(self):
		if self.__path_to_database != "":
			self.__db = sqlite3.connect(self.__path_to_database)

	def close(self):
		if self.__db != None:
			self.__db.close()

	def query(self, statement):
		cursor = None
		if self.__db != None:
			cursor = self.__db.execute(statement)
		return cursor

	def doNoneQuery(self, statement):
		self.__db.execute(statement)
		self.__db.commit()

	def insertGroup(self, title, description):
		guid=str(uuid.uuid4())
		statement = "insert into groups(id, title, description) values ('" + guid + "','" + title + "','" + description + "')"
		self.doNoneQuery(statement)

	def insertElement(self, title, description):
		guid=str(uuid.uuid4())
		statement = "insert into element(id, title, description) values ('" + guid + "','" + title + "','" + description + "')"
		self.doNoneQuery(statement)

def main():
	db = DBHelper('./connection.db')
	db.open()	
	sql_statement="select element.title, connection.goodeffect from connection inner join element on element.id=connection.point_element where connection.theme_element='3AE6939B-B0DF-776C-5D0B-C1C31A202F34'"
	cursor = db.query(sql_statement)	

	for row in cursor:
		print("Title = {0}, effect = {1}".format(row[0], row[1]))

	db.insertGroup('GDP', 'about one GDP')
	db.close()

main()