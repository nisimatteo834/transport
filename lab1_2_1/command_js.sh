#!/bin/bash

echo 'Working on parking...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_parking.js > temp1.dat
echo 'Done'
echo 'Working on booking...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_booking.js > temp2.dat
echo 'Done'
echo 'Working on booking no filter...'
mongo bigdatadb.polito.it/carsharing --ssl --sslAllowInvalidCertificates -u ictts -p 'Ictts16!' --authenticationDatabase carsharing lab1_2_1_booking_nofilter.js > temp3.dat
echo 'Done'
echo "Working with GREP..."

cat temp1.dat | grep Madrid > parking_MA.dat
cat temp1.dat | grep Torino > parking_TO.dat
cat temp1.dat | grep NYC > parking_NY.dat
cat temp2.dat | grep Madrid > booking_MA.dat
cat temp2.dat | grep Torino > booking_TO.dat
cat temp2.dat | grep NYC > booking_NY.dat
cat temp3.dat | grep Madrid > booking_nf_MA.dat
cat temp3.dat | grep Torino > booking_nf_TO.dat
cat temp3.dat | grep NYC > booking_nf_NY.dat
echo "Done"

rm temp*

#cut -d" " -f5- temp.dat > $file_out_p_nf
python3 plot.py