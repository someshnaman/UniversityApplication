from cassandra.auth import PlainTextAuthProvider
# from views.api import api
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask

from course.coursemodel import Course
from database.congifugration import Config

KEYSPACE = "test"


def create_app():
    app = Flask(__name__)

    app.debug = True
    # app.register_blueprint(api)
    config_object = Config()
    bundle_file_path = config_object.getConfig("database", "cassandra_bundle_path")
    cloud_config = {'secure_connect_bundle': bundle_file_path}
    client_id = config_object.getConfig("database",
                                        "client_id")  # Bringing client_id from config.ini
    client_secret = config_object.getConfig("database",
                                            "client_secret")  # Bringing client_secret from config.ini
    auth_provider = PlainTextAuthProvider(username=client_id,
                                          password=client_secret)
    cluster = Cluster(cloud=cloud_config,
                      auth_provider=auth_provider, protocol_version=3,
                      connect_timeout=30,
                      control_connection_timeout=10.0)
    connection.setup(hosts=["e7817872-8b68-4aaa-811f-48c32d99d0fe-us-east-1.db.astra.datastax.com"],
                     default_keyspace="test", lazy_connect=False, protocol_version=3)
    sync_table(Course)
    session = cluster.connect()
    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)
    session = cluster.connect(keyspace=KEYSPACE)

    return app


app = create_app()
