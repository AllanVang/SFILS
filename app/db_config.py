import mysql.connector

def get_connection():
  return mysql.connector.connector(
    host= "127.0.0.1",
    user="root",
    password="Mimikyu49",
    database="SanFranSortedDatabase"
  )
