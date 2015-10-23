# coding=utf-8
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Azurite                                                       |
#  |   Version: 0.0.2                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0776                                                            |
#  |   GitHub-Page: http://red-c0der.github.io/Project-Azurite                     |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/


def write(level, message, lloc="", LogFile=""):
    import logging
    if LogFile == "":
        from time import gmtime, strftime
        LogName = strftime("%d-%m-%Y", gmtime())
        LogLoc = "../logs/"
        LogF = LogLoc+LogName+".log"
    else:
        LogF = LogFile
    logging.basicConfig(filename=LogF, level=logging.DEBUG, format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
    if lloc != "":
        if level == "i":
            logging.info(lloc+message)
        if level == "w":
            logging.warning(lloc+message)
        if level == "e":
            logging.error(lloc+message)
        if level == "c":
            logging.critical(lloc+message)
        if level == "ex":
            logging.exception(lloc+message)
        if level == "d":
            logging.debug(lloc+message)
        if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
            import inspect
            logging.exception("Function " + inspect.stack()[1][3] + " tried to use logger.write() with invalid logging level " + level +  " !")
        return
    else:
        if level == "i":
            logging.info(message)
        if level == "w":
            logging.warning(message)
        if level == "e":
            logging.error(message)
        if level == "c":
            logging.critical(message)
        if level == "ex":
            logging.exception(message)
        if level == "d":
            logging.debug(message)
        if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
            import inspect
            logging.exception("Function " + inspect.stack()[1][3] + " tried to use logger.write() with invalid logging level " + level +  " !")
        return
