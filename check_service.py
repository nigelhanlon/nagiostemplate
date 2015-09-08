#!/usr/bin/python

import sys

#
# Nagios needs a keyword returned as well as exit status.
#
# When writing a plugin, all you really need are these:
#
def ok(message):
    """
        Standard reply. All good :)
    """
    print "OK - %s" % (message)
    sys.exit(0)

def warning(message):
    """
        Flag warning in Nagios
    """
    print "WARNING - %s" % (message)
    sys.exit(1)

def critical(message):
    """
        Flag critical in Nagios
    """
    print "CRITICAL - %s" % (message)
    sys.exit(2)

def unknown(message):
    """
        Called when options missing or config error.
    """
    print "UKNOWN - %s" % (message)
    sys.exit(3)


if __name__ == "__main__":
    # Put whatever logic you need here to check service state and
    # then call one of the above functions like so:
    if True == True:
        ok("My service is running ok")
