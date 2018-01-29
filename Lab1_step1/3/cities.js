var a = db.getCollection('ActiveBookings').distinct("city",{},{city:1,_id:0})
var b = db.getCollection('PermanentBookings').distinct("city",{},{city:1,_id:0})
print (a,b)