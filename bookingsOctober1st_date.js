var start_date = new ISODate("2017-10-01T00:00:00")
var start = start_date.getTime()/1000 
var end = start + 24*60*60 
var end_date = new ISODate("2017-10-01T23:59:59")
var city = ["Torino","Madrid","New York City"]
for(i=0;i<city.length; i++){
    print(city[i])
    c = city[i]
    a = db.PermanentBookings.aggregate([  
    {$match:  
        { 
            init_date:{$gte:start_date,$lte:end_date}, 
            $or:[ 
            {city:c} 
            ]}
     }, 
  
    {$group:{  
        _id:"$city",  
        cars:{$sum:1}  
    }},  
    {$sort:  
        { _id:1}}])
print(a) }   