from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

from database.congifugration import Config
from database.logger import Logs

logs = Logs()


class Course(Model):
    __keyspace__ = "test"
    course_id = columns.Integer(primary_key=True)
    course_code = columns.Text()
    course_name = columns.Text()
    course_desc = columns.Text()
    course_imageUrl = columns.Text()
    course_duration = columns.Integer()


class DB:
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
            connection.setup('test', cluster, auth_provider)

        except Exception as e:
            logs.error(e)


n = DB()
sync_table(Course)
x = Course.objects.all()
print(x)
