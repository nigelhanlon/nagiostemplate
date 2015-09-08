Simple Nagios Plugin
======
**check_service.py** is simple Nagios plugin template written in python. Simply add your own check logic and then call one of the four state functions to alert Nagios.

## Example: Monitor 5 minute load average and alert when greater than 1
```
if __name__ == "__main__":
    import os
    load = os.getloadavg()
    if load[1] > 1:
        ok("Load - %f" % load[1] )
    else:
        critical("Load - %f" % load[1] )
```


## Installation

Like most Nagios plugins you can either add it to nrpe.cfg if you are using the NRPE daemon or call it via sendnsca:
```
$ # vim /etc/nagios/nrpe.cfg
 .
 ..
 ...
 command[myservice]=/usr/lib/nagios/plugins/check_service.py
 ...
 ..
 .
$
```

## Version
* Version 1.0.0
