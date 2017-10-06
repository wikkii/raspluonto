import MySQLdb

def connection():

	#Insert your actual values here
	conn = MySQLdb.connect(host="localhost",
							user="username",
							passwd="password",
							db="nuotiovahti")
							
	c = conn.cursor()
	
	return c, conn
							