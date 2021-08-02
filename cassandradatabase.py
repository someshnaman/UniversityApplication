from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from logger import Logs as log


class Database:
    def __init__(self, client_id, client_secret):
        """
        This function will require for setting up our database
        """
        self.client_id = client_id
        self.client_secret = client_secret

    def database_connection(self):
        """
        This Function will help us in the connnection to the database

        """
        try:
            cloud_config = {'secure_connect_bundle': r'resources/secure-connect-mydatabase.zip',
                            'init-query-timeout': 10,
                            'connect_timeout': 10,
                            'set-keyspace-timeout': 10
                            }
            auth_provider = PlainTextAuthProvider(username=f'{self.client_id}',
                                                  password=f'{self.client_secret}')
            cluster = Cluster(cloud=cloud_config,
                              auth_provider=auth_provider,)
            session=cluster.connect()
            row = session.execute("select release_version from system.local").one()
            if row:
                log.info(f"row[0] ,Connection Established",)
            return row
        except Exception as e:
            log.error(e)

somesh=Database("FxthvapkTAzHqHmYvAfIpMmO",",xUtYFPsfmbBLdWZUr.WG4tr7NiUDeCtodpwodjdY-_zq6Xl7wc.81iQOZWOBa51rAu+jvkCfvFgaZsQXuJ3mE6.u-ehZp9k-SWr1eiw1BQ7GdbOvHrzegqr1LbgH1X8")
somesh.database_connection()



