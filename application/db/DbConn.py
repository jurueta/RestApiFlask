import mysql.connector as connectDb
import os
import sys

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
            sys.exit("Error while connect to BD") 

    def query(self, query: str):
        """ Make a query and obtain result """
        try:
            cursor = self.conDb.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            count = cursor.rowcount
            cursor.close()
            return {'error': 0, 'data': result, 'count':count}
        except Exception as error:
            return {'error': 1, 'message': f"An error was generated when executing the query ({error})."}

    def insert(self, insert, data_insert):
        """ Insert into DB """
        try:
            cursor = self.conDb.connection.cursor()
            cursor.execute(insert, data_insert)
            cursor.connection.commit()
            cursor.close()
        except Exception as error:
            return f"An error was generated when executing the insert ({error})."