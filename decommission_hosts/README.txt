INTRODUCTION:
------------

This module contains script files to decommission hosts.


REQUIREMENTS:
------------

This module requires the following modules:

 * Python 2.7.x
   Libraries
  * requests
  * sys
  * json
  * time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.


PREREQUSITES:
--------------

The following data is required

FQDN of each host

The host must not be assigned to a domain i.e "status" must be "UNASSIGNED_USEABLE".

TIP
Refer to: Get the Hosts to fetch the hosts with the required "status"

USAGE:
-----

 Usage:	python decommission_hosts.py <hostname> <username> <password> <fqdn1> <fqdn2> ..