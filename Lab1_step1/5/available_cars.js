var cities = ["Madrid","Torino","New York City"];

for (var i=0; i<cities.length; i++){      
    print (cities[i]);
    c = cities[i];
    a = db.getCollection('ActiveBookings').distinct("plate",{city: c});
    b = db.getCollection('ActiveParkings').distinct("plate",{city: c});
    print ('ActiveBookings',a.length + b.length);
}