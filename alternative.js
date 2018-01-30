var start_date = new Date("2017-10-01")  
var start = start_date.getTime()/1000+1*60*60 - 24*60*60   
var end = start + 24*60*60   
db.PermanentBookings.aggregate([    
{$match:    
    {   
        "walking.duration":{$ne:-1},   
        $or:[   
            {city:"Torino"},   
            {city:"Madrid"},             
            {city:"New York City"}            
             ]   
     }  
 },    
{$group:{    
    _id:"$city",    
    bookings:{$sum:1}    
}},    
{$sort:    
    { _id:1}}])   