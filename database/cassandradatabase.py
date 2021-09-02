import json

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

from database.congifugration import Config
from database.logger import Logs

logs = Logs()


class Database():
    database_section_name = "database"

    def __init__(self):
        """
        This Function will help us in the connection to the database

        """
        try:
            config_object = Config()
            bundle_file_path = config_object.getConfig(self.database_section_name, "cassandra_bundle_path")
            cloud_config = {'secure_connect_bundle': bundle_file_path}
            client_id = config_object.getConfig(self.database_section_name,
                                                "client_id")  # Bringing client_id from config.ini
            client_secret = config_object.getConfig(self.database_section_name,
                                                    "client_secret")  # Bringing client_secret from config.ini
            auth_provider = PlainTextAuthProvider(username=client_id,
                                                  password=client_secret)
            cluster = Cluster(cloud=cloud_config,
                              auth_provider=auth_provider, protocol_version=3,
                              connect_timeout=30,
                              control_connection_timeout=10.0)

            session = cluster.connect()

            db_keyspace = config_object.getConfig(self.database_section_name,
                                                  "keyspace_name")  # Setting up Keyspace
            session.execute(f"use {db_keyspace}").one()
            logs.info("Connection Established")
            self.session = session
        except Exception as e:
            logs.error(e)

    def findAll(self, table_name):
        try:
            """
            This function will fetch all the data available in the Table            
            """
            end_result = []
            result = self.session.execute(f"select json * from {table_name}")
            for i in result.all():
                end_result.append(json.loads(i[0]))
            print(end_result)

            return end_result
        except Exception as e:
            logs.exception(f"Can't find the values from the table {table_name},{e}")

    def executeSpecific(self, condition, query):
        try:
            prepare_query = self.session.prepare(query)
            binding_values = prepare_query.bind(condition)
            result = self.session.execute(binding_values)
            logs.debug(f"Executed : {binding_values}")
            return result
        except Exception as e:
            logs.exception(e)

    def insert(self, query, values):
        try:
            prepare_query = self.session.prepare(query)
            binding_values = prepare_query.bind(values)
            results = self.session.execute(binding_values)
            logs.info(f'Successfully inserted ')
            return results
        except Exception as e:
            logs.exception(e)

    def update(self, id, query, values):
        try:
            values.append(id)
            prepare_query = self.session.prepare(query)
            binding_values = prepare_query.bind(values)
            results = self.session.execute(binding_values)
            logs.info(f'Successfully update ')
            return results
        except Exception as e:
            logs.exception(e)

    def delete(self, course_id):
        try:
            self.session.execute(f"DELETE FROM course1"
                                 f"WHERE id={course_id} IF EXISTS")
        except Exception as e:
            logs.exception(e)
