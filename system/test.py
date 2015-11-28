__author__ = 'Red_C0der'


import modulemanager as ml
import sys
import os


debug = 1


#import output
#output.colorPrint("test 12345", fgc=430, debug=debug)


import console

console.newconsole("root", "azurite", "TestConsole")








# Changing mode of file path
#m = ml.loadmodules(["filemanager"], debug=debug)
#file = m[0]
#dir = file.dir()
#dir.chmod("test", 777, debug=debug)


# Loading modules from list (modules must be activated in sys.xml)
#modules = ml.loadmodules(["module1", "module2"], debug=debug)


# Add attribute
#cfg.addattrib("values/test/value", "new", "New attrinute!!", debug=debug)


# Removing attribute
#cfg.delattrib("values/test/value", "second", debug=debug)


# Setting value of attribute
#cfg.setattrib("values/test/value", "val", "Text changed!", debug=debug)


# Getting value of attribute
# cfg.getattrib("values/test/value", "val", debug=debug)