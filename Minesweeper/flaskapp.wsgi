#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"C:\Program Files (x86)\Ampps\www\FlaskApp")

from FlaskApp import app as application
application.secret_key = 'your secret key. If you share your website, do NOT share it with this key.'