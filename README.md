# Alertify
A Notification Alert for Linux System


## Features ##
* Allows you to set notification alert after given minutes
* Enable or Disable counter to display on your terminal

## Requirements ##
* python2 only

## Installation ##
``sudo python setup.py install``
[Make sure you are using python2]

## Usage ##
### Alert with Timer ###
``alertify time message``

time - denotes the minutes which can be any integer value
message - the message to display

### Alert without Timer
``alertify time message --no-counter``

### Example ###
``alertify 1 Time is up``

Alert after 1 minute (Timer runs on the terminal)

``alertify 2 Time is up --no-counter``

Alert after 2 minutes (Timer does not run on the terminal)



**NOTE:** Works on Linux only.
