import pymongo
class DBconnectivity:
    __URL="mongodb+srv://test:test@cluster0.ejvnm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    __DATABASE=None
    __myconnectivity=None
    __collection=None

    @staticmethod
    def connect():
        '''
        By executing this Function we'will be able to connect with our database

        '''
        try:
            DBconnectivity.__myconnectivity = pymongo.MongoClient(DBconnectivity.__URL)
            return DBconnectivity.__myconnectivity
        except Exception as e:
            print(e)
    @staticmethod
    def db_creation(db_name):
        '''
        Used for creating the databse
        :param db_name: Database name
        :return: Database
        '''
        try:
            # First we'll verify the db_name we want to create does exicst or not
            DB_list=DBconnectivity.__myconnectivity.list_database_names()

            if db_name in DB_list:
                print(f'{db_name} already exist')
                DBconnectivity.__DATABASE= DBconnectivity.__myconnectivity[db_name]
                return DBconnectivity.__DATABASE
            else:
                DBconnectivity.__DATABASE=DBconnectivity.__myconnectivity[db_name]
                print('-'*10)
                print("Database created")
                return DBconnectivity.__DATABASE
        except Exception as e:
            print(e)
    @staticmethod
    def insert_one(collection,data):
        '''
        Used for inserting one Value into the collection
        :param collection: collection name
        :param data: *args
        :return:  Data will be inserted into the database
        '''
        try:
            DBconnectivity.__collection=collection
            Insert_object= DBconnectivity.__DATABASE[DBconnectivity.__collection].insert_one(data)
            print("Insertion Done")
            return Insert_object
        except Exception as e:
            print(e)

    @staticmethod
    def insert_many(collection, data):
        '''
        Takes Two Argumanet One is the collection where you want to put your data and
        2nd is data you want to put
        :param collection: collection name
        :param data: *args
        :return: all the Data will be inserted into the database
        '''
        try:
            DBconnectivity.__collection = collection
            Insert_object = DBconnectivity.__DATABASE[DBconnectivity.__collection].insert_many(data)
            print("All Insertion Done")
            return Insert_object
        except Exception as e:
            print(e)

    @staticmethod
    def find_all(collection):
        try:
            DBconnectivity.__collection=collection
            myfindings=DBconnectivity.__DATABASE[DBconnectivity.__collection]
            for idx,record in enumerate(myfindings.find()):
                print(idx,record)
        except Exception as e:
            print(e)

    @staticmethod
    def find_query(collection,query):
        try:
            DBconnectivity.__collection=collection
            myfindings=DBconnectivity.__DATABASE[DBconnectivity.__collection]
            for idx,record in enumerate(myfindings.find(query)):
                print(idx,record)
        except:
            print(e)

    @staticmethod

    def update_one(collection,present_data,new_data):
        '''
        This will help us to update our 1st match existing record.
        :param present_data: Presnt data available in the database
        :param new_data: new record to be updated in place of Old one
        :return: New record Updated
        ----------------------------
        for ex:
        present_data = {'courseOffered': 'Machine Learning with Deployment'}
        new_data = {"$set":{'courseOffered': 'ML and DL with Deployment'}}
        update_one(present_one,new_data)
        '''
        try:
            DBconnectivity.__collection = collection
            update=DBconnectivity.__DATABASE[DBconnectivity.__collection].update_one(present_data,new_data)
            print("Update done")
            return update

        except Exception as e:
            print(e)

    @staticmethod
    def update_many(collection,present_data, new_data):
        '''
        This will help us to update all the record where match is found.
        :param present_data: Presnt data available in the database
        :param new_data: new record to be updated in place of Old one
        :return: New record Updated
        ----------------------------
        for ex:
        present_data = {'courseOffered': 'Machine Learning with Deployment'}
        new_data = {"$set":{'courseOffered': 'ML and DL with Deployment'}}
        update_many(present_one,new_data)
        '''
        try:
            DBconnectivity.__collection = collection
            DBconnectivity.__DATABASE[DBconnectivity.__collection].update_many(present_data, new_data)
            print("Update done")

        except Exception as e:
            print(e)

    @staticmethod
    def delete_one(collection,query):
        '''
        Takes a Dictionary and find out the key and value in your reccord and delete the record
        where key and value is found
        :param query:dictionary
        :return: Updatated collection
        '''
        try:
            DBconnectivity.__collection = collection
            DBconnectivity.__DATABASE[DBconnectivity.__collection].delete_one(query)
            print("Update done")

        except Exception as e:
            print(e)










