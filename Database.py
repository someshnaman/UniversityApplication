import mysql.connector as connection
class DBconnectivity:

    def __init__(self,host,user,passwd,database):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.database=database

    def connect(self): # this Funtion is used to maintain the cusor in database
        mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
        self.cursor = mydb.cursor()
        print('Connection Establisted')

    def execute(self,query):
        self.cursor.execute(query)
        for i in self.cursor.fetchall():
            print(i)

some=DBconnectivity("localhost","root","mysql","somesh")
some.connect()
some.execute('use somesh')

