# [<SniEndPoint: e7817872-8b68-4aaa-811f-48c32d99d0fe-us-east-1.db.astra.datastax.com:29042:c79f1d1d-55b6-4e08-a34a-0947be112cd2>, <SniEndPoint: e7817872-8b68-4aaa-811f-48c32d99d0fe-us-east-1.db.astra.datastax.com:29042:0af83368-ec1c-4116-82a0-d6a33c97c61c>
# <SniEndPoint: e7817872-8b68-4aaa-811f-48c32d99d0fe-us-east-1.db.astra.datastax.com:29042:183c2549-61c7-497a-8aa4-49f57e8a9f6d>]

from ssl import SSLContext, CERT_REQUIRED

from cassandra.auth import PlainTextAuthProvider
from flask import Flask
from flask_cqlalchemy import CQLAlchemy

auth_provider = PlainTextAuthProvider(username='jane.smith', password='jsP@ssw0rd')
ssl_context = SSLContext(PROTOCOL_TLSv1)
ssl_context.load_verify_locations("../secure-connect/ca.crt")
ssl_context.verify_mode = CERT_REQUIRED
ssl_context.load_cert_chain(
    certfile="../secure-connect/cert",
    keyfile="secure-connect/key")

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['7bb9cd7a-e49d-49a6-aa3d-be4878f974ef-us-east1.db.astra.datastax.com']
app.config['CASSANDRA_SETUP_KWARGS'] = dict(ssl_context=ssl_context, port="31575", auth_provider=auth_provider)
app.config['CASSANDRA_KEYSPACE'] = "cqlengine"
db = CQLAlchemy(app)
