from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import logger
from congifugration import Config
from dbqueries import Dbqueries

logs = logger.Logs()


class Database:
    database_section_name = "database"
    session = None

    def connection(self):
        """
        This Function will help us in the connection to the database

        """
        try:
            config_object = Config()
            bundle_file_path = config_object.getConfig(self.database_section_name, "cassandra_bundle_path")
            cloud_config = {'secure_connect_bundle': bundle_file_path,
                            'init-query-timeout': 10,
                            'connect_timeout': 10,
                            'set-keyspace-timeout': 10
                            }

            client_id = config_object.getConfig(self.database_section_name,
                                                "client_id")  # Bringing client_id from config.ini
            client_secret = config_object.getConfig(self.database_section_name,
                                                    "client_secret")  # Bringing client_secret from config.ini
            auth_provider = PlainTextAuthProvider(username=client_id,
                                                  password=client_secret)
            cluster = Cluster(cloud=cloud_config,
                              auth_provider=auth_provider, )
            session = cluster.connect()
            db_keyspace = config_object.getConfig(self.database_section_name,
                                                  "keyspace_name")  # Setting up Keyspace
            session.execute(f"use {db_keyspace}").one()
            logs.info("Connection Established")
            return session
        except Exception as e:
            logs.error(e)

    def findAll(self, table_name):
        try:
            """
            This function will fetch all the data available in the Table            
            """
            db=Database()
            mysession = db.connection()
            result = mysession.execute(f"select * from {table_name}")
            return result
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


