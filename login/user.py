import uuid
from database.cassandradatabase import Database
import database.constants as constant_queries
from database.logger import Logs

logs = Logs()


class User:
    def __init__(self):
        self.id = None
        self.email = None
        self.password = None
        self.username = None

    def __init__(self, email, password, username):
        self.id = uuid.uuid4()
        self.email = email
        self.password = password
        self.username = username


class UserDbQueries:
    def findUserByEmail(self, email):
        try:
            database_object = Database()
            email_result = database_object.executeSpecific([email], constant_queries.query_find_user_by_email)
            user = User(email_result[0].email, email_result[0].password, email_result[0].username)
            return user
        except Exception as e:
            logs.exception(e)


x = UserDbQueries()

x.findUserByEmail('namanayo5@gmail.com')
