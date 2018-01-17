#!/bin/bash

echo 'Working on Enjoy WorkingD...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing enjoy_wd.js > enjoy_wd.csv 
echo 'Done'

echo 'Working on Car2Go WorkingD...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing car2go_wd.js > car2go_wd.csv
echo 'Done'


