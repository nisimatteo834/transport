//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-01T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-30T23:59:59")
var endUnixTime = endDate.getTime() / 1000
var range = 3600
add_time = -2*60*60
var result = db.PermanentBookings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "Torino"}],
            init_time: { $gte: startUnixTime+add_time, $lte: endUnixTime+add_time},
            "public_transport.duration":{$ne:-1}
            //"walking.duration":{$ne:-1}
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
            hourDay: {$hour: "$init_date"},
            monthDay: {$concat: [{$substr: [{$month: "$init_date"},0,2]},"-",{$substr: [{$dayOfMonth: "$init_date"},0,2]}]},
            dayU: {$floor: {$divide: ["$init_time", range]}},
            init_time: 1,
            monthDay: {$month: "$init_date"},
            day: {$dayOfMonth: "$init_date"},
            init_date:1,

            pt_duration:{$divide:["$public_transport.duration",60]}
            //walking_duration : {$divide:["$walking.duration",60]}
        }   
     },
        {
         $match: { // filter only actual bookings
             moved: true, // must have moved
             duration: {$lte: 180, $gt: 2} // must last than 3h and greater then 2m
         }
     },

{
   $sort:{
       "day":1,
       "hourDay":1
        }
    }
 ])
while(result.hasNext()) {
    a = result.next()

    print (a["duration"],a["pt_duration"])
}