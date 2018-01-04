#!/bin/bash
#echo $1
#echo $2
#echo $3

#file_out_b='torino.dat'
#file_out_b_nf='torino_nf.dat'
#file_out_p='torino2.dat'
#file_out_p_nf='torino2_nf.dat'

file_out_m='ma.dat'
file_out_t='to.dat'
file_out_ny='ny.dat'
total="total.dat"

echo 'Working on query...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_booking_nofilter.js > $total
echo 'Done'

echo 'Working on Madrid...'
cat $total | grep Madrid > $file_out_m
#cut -d" " -f5- temp.dat > $file_out_m
head $file_out_m
echo 'Done'

echo 'Working on Torino...'
cat $total | grep Torino > $file_out_t
#cut -d" " -f5- temp.dat > $file_out_t
head $file_out_t
echo 'Done'

echo 'Working on NYC...'
cat $total | grep New | cut -d " "  -f 1,4,5 | awk '{print "NYC", $2, $3}' > $file_out_ny
#cut -d" " -f7- temp.dat > $file_out_ny
head $file_out_ny
echo 'Done'


#python3 plot.py

