#Python Currency Service

This piece of code is a Flask app written in Python. The purpose of the app is to consume, and parse, the copy of the daily currency conversion values provided for free from the European Central Bank at the following URL:

http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml

There are many currency conversion API's available that are available for public consumption, but those cost money to do at scale, and we're cheap. 

##Current Functionality:
Runs via Flask
API Call to download the full XML file, parse, then return the value based on the currency route pasted to flask

##Working On:
Passing value variables into the URL to complete the currency conversion math within the service
Dockerize
K8s Manifest
