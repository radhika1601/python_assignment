import mysql.connector

cnx = mysql.connector.connect(
	host="localhost",
	user="radhika",
	passwd="Rg@756831")

cursor = cnx.cursor()
cursor.execute("use python_assignment")
