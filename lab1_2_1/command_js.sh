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

echo 'Working on parking...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_parking.js > $file_out_p
cat $file_out_p | grep $city > temp.dat
cut -d" " -f5- temp.dat > $file_out_p
echo 'Done'

echo 'Working on booking...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_booking.js > $file_out_b
cat $file_out_b | grep $city > temp.dat
cut -d" " -f5- temp.dat > $file_out_b
echo 'Done'

echo 'Working on booking no filter...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_booking_nofilter.js > $file_out_b_nf
cat $file_out_b_nf | grep $city > temp.dat
cut -d" " -f5- temp.dat > $file_out_b_nf
echo 'Done'

echo 'Working on parking no filter'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_parking.js > $file_out_p_nf
cat $file_out_p_nf | grep $city > temp.dat
cut -d" " -f5- temp.dat > $file_out_p_nf

#python3 plot.py

