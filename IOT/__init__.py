import sys
#from OpenSSL import SSL
from flask import Flask, render_template
from index import index
app = Flask(__name__,template_folder="templates",static_url_path="")
app.register_blueprint(index, url_prefix = "/")

if __name__ == "__main__":
     #app.run(host="192.168.1.9", port=5000, ssl_context=('cert.pem', 'key.pem'))
     app.run()
