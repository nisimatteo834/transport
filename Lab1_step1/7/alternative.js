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