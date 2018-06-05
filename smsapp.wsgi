#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/sms-app/")

from src import app as application
application.secret_key = 'u'
