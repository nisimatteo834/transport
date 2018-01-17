#!/bin/bash

echo 'Working on Enjoy Weekends...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing enjoy_we.js > enjoy_we.csv 
echo 'Done'

echo 'Working on Car2Go Weekends...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing car2go_we.js > car2go_we.csv
echo 'Done'


