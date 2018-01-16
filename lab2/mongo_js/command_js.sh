#!/bin/bash
#echo $1
#echo $2
#echo $3

#file_out_b='torino.dat'
#file_out_b_nf='torino_nf.dat'
#file_out_p='torino2.dat'
#file_out_p_nf='torino2_nf.dat'

city='Madrid'
file_out_b='MA.dat'
file_out_b_nf='MA_nf.dat'
file_out_p='MA2.dat'
file_out_p_nf='MA2_nf.dat'

echo 'Working on Enjoy...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing enjoy.js > enjoy.csv 
echo 'Done'

echo 'Working on Car2Go...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing car2go.js > car2go.csv
echo 'Done'

#python3 plot.py

