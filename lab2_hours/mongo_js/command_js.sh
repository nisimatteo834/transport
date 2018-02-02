#!/bin/bash

echo 'Working on Enjoy...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing enjoy_aft.js > enjoy_aft.csv 
echo 'Done'

echo 'Working on Car2Go...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing car2go_aft.js > car2go_aft.csv
echo 'Done'


