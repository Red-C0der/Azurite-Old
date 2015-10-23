__author__ = 'Red_C0der'


import cryptographer as cr
import configparser as cfg
import sys
import voiceparser as vp
import logger

import Ma
debug = 1


vp.listen_to_activator("jarvis", debug=debug)

# Setting Value
# cfg.setval("values/version", attrib_name="val", new_attrib_val="0.3", debug=debug)

# Getting value
# print cfg.getval("MainValues", "version", debug=debug)