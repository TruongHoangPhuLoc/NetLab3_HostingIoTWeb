#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")
sys.path.append("var/www/FlaskApp/IOT/Modules/View")
sys.path.append("var/www/FlaskApp/IOT/templates")
sys.path.append("var/www/FlaskApp/IOT/static")
from IOT import app as application
application.secret_key = 'something super SUPER secret'
