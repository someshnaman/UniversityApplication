import uuid
from database.cassandradatabase import Database
import database.constants as constant_queries
from database.logger import Logs
from flask_login import UserMixin
from route import login_manager
from database import constants

logs = Logs()


@login_manager.user_loader
def load_user(user_id):
    user = UserDao()
    result = user.findUserByID(user_id)
    if result is not None:
        return result
    else:
        return None


class User(UserMixin):

    def __init__(self, id, email, password, username):
        self.id = id
        self.email = email
        self.password = password
        self.username = username


class UserDao:
    def findUserByEmail(self, email):
        try:
            database_object = Database()
            email_result = database_object.executeSpecific([email], constant_queries.query_find_user_by_email)
            user = User(email_result[0].id, email_result[0].email, email_result[0].password, email_result[0].username)
            return user
        except Exception as e:
            logs.exception(e)

    def findUserByID(self, id):
        try:
            print(uuid.UUID('88eaaf0c-a05d-4cd8-9a46-ff6ff2c77a53'))
            database_object = Database()
            email_result = database_object.executeSpecific([uuid.UUID(id)], constant_queries.query_find_user_by_id)
            user = User(email_result[0].id, email_result[0].email, email_result[0].password, email_result[0].username)
            return user
        except Exception as e:
            logs.exception(e)

    def insertUser(self, user_list):
        database_object = Database()
        return database_object.insert(constants.uery_insert_user, user_list)
