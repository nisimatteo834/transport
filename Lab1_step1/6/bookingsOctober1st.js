var start_date = new ISODate("2017-10-01T00:00:00")
var start = start_date.getTime()/1000 
var end = start + (24*60*60) 
var city = ["Torino","Madrid","New York City"]
var time=[-2,-2,4]
for(i=0;i<city.length; i++){
    print(city[i])
    c = city[i]
    w = time[i]
    add_time = w*60*60
    a = db.PermanentBookings.aggregate([  
    {$match:  
        { 
            init_time:{$gte:start+add_time,$lte:end+add_time}, 
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