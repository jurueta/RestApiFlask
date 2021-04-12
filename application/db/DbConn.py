import mysql.connector as connectDb
import os
import json

class DbConn():

    def __init__(self):
        """ Instace a DB with data in .env """
        try:
            self.conDb = connectDb.connect(
                host = os.getenv("MYSQL_HOST"),
                port = os.getenv("MYSQL_PORT"),
                user = os.getenv("MYSQL_USER"),
                passwd = os.getenv("MYSQL_PASSWORD"),
                database = os.getenv("MYSQL_DB")
            )
        except Exception as error:
            raise(error)

    def query(self, query: str, data: list=()):
        """ Make a query and obtain result """
        try:
            cursor = self.conDb.cursor(dictionary=True)
            cursor.execute(query, data)
            result = cursor.fetchall()
            count = cursor.rowcount
            cursor.close()
            return {'error': 0, 'data': result, 'count':count}
        except Exception as error:
            raise(error)

    def insert(self, insert: str, data_insert: list=()):
        """ Insert into DB """
        try:
            cursor = self.conDb.cursor()
            cursor.execute(insert, data_insert)
            self.conDb.commit()
            id_insert = cursor.lastrowid
            cursor.close()
            return {'error': 0, "id" : id_insert}
        except Exception as error:
            raise(error)

    def update(self, update: str, data_update: list=()):
        try:
            cursor = self.conDb.cursor()
            cursor.execute(update, data_update)
            self.conDb.commit()
            count = cursor.rowcount
            cursor.close()
            return {'error': 0, 'count': count }
        except Exception as error:
            raise(error)