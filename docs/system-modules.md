# All System Modules

Here you can see a short description of ALL system modules,

to know what the do.


### test.py - Just for testing

>   Theoretically we could skip this file, because essentially there is nothing special
>   in there. It's just used to test things.



### setup.py - Installing the system

#### install()

>   This function starts the installation-progress.
>   It reads each tag from the setting/setup_sequence.xml and
>   runs the corresponding action.



### logger.py - Handling logfiles

#### write(level, message, lloc="", LogFile="")

>   This function opens a logfile, if it is specified in [LogFile=""]
>   or generates a new one with the current date as filename,
>   if no name is specified in [LogFile=""].
>   Then it write's the message [message] with the
>   logging-level [level] and the current time to a new line in the file.



### none.py