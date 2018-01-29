var a = "\nActiveBookings: " + db.getCollection('ActiveBookings').find({}).count()  
var b = "\nActiveParkings: " + db.getCollection('ActiveParkings').find({}).count() 
var c = "\nPermanentBookings: "+ db.getCollection('PermanentBookings').find({}).count()  
var d = "\nPtermanentParkings: " +db.getCollection('PermanentParkings').find({}).count()
print(a,b,c,d)