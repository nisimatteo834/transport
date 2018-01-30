//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-01T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-30T23:59:59")
var endUnixTime = endDate.getTime() / 1000
var cities = ["Torino","Madrid","New York City"]

var time=[-2,-2,4]


var range = 3600

for (i=0; i<cities.length; i++){
	c = cities[i]
	w = time[i]
	add_time = w*60*60
	var result = db.PermanentBookings.aggregate([
    {
        $match: { // filter here what you want first
            city: c,
			init_time: { $gte: startUnixTime+add_time, $lte: endUnixTime+add_time}
        	}
    },
        {
        $project: { // extract position, time, duration
            _id: 0,
            city: 1,
            moved: { $ne: [
                {$arrayElemAt: [ "$origin_destination.coordinates", 0]},
                {$arrayElemAt: [ "$origin_destination.coordinates", 1]}
                ]
            },
            duration: { $divide: [ { $subtract: ["$final_time", "$init_time"] }, 60 ] },
            //dayofWeek: {$dayOfWeek: "$init_date"},
            hourDay: {$hour: "$init_date"},
            monthDay: {$concat: [{$substr: [{$month: "$init_date"},0,2]},"-",{$substr: [{$dayOfMonth: "$init_date"},0,2]}]},
            dayU: {$floor: {$divide: ["$init_time", range]}},
            init_time: 1,
            monthDay: {$month: "$init_date"},
            day: {$dayOfMonth: "$init_date"},
            init_date:1
        }
        
     },

        {

         $match: { // filter only actual bookings

             moved: true, // must have moved

             duration: {$lte: 180, $gt: 2} // must last than 3h and greater then 2m

         }

     },
{
    $group:
    {
        _id:{hourDay: "$hourDay", city:"$city"},
        total_parking: {$sum: 1}
    }
},
{
   $sort:{
       "_id.hourDay":1
        }
    }
 ])
        
while(result.hasNext()) {
    a = result.next()
	if (a["_id"]["city"] == "New York City")
	{
		    print ("NYC", a["_id"]["hourDay"], a["total_parking"])
	}
		
	else 
    {
		print (a["_id"]["city"],a["_id"]["hourDay"],a["total_parking"])
	}
}
}
