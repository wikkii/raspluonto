#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/nuotiovahti/public_html/nuotiovahti/")

from nuotiovahti import app as application
application.secret_key = 'Add your secret key'
