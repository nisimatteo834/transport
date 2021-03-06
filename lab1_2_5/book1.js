//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-01T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-30T23:59:59")
var endUnixTime = endDate.getTime() / 1000
var range = 3600
var result = db.PermanentParkings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "Torino"}],
            init_time: { $gte: startUnixTime, $lte: endUnixTime}
        	}
    },
        {
        $project: { // extract position, time, duration
            _id: 0,
            city: 1,
            duration: { $divide: [ { $subtract: ["$final_time", "$init_time"] }, 60 ] },
            hourDay: {$hour: "$init_date"},
            monthDay: {$concat: [{$substr: [{$month: "$init_date"},0,2]},"-",{$substr: [{$dayOfMonth: "$init_date"},0,2]}]},
            dayU: {$floor: {$divide: ["$init_time", range]}},
            init_time: 1,
            monthDay: {$month: "$init_date"},
            day: {$dayOfMonth: "$init_date"},
            init_date:1,
            loc:1,
            //lat:{"loc.coordinates"}
            lat: {$arrayElemAt: [ "$loc.coordinates", 1]},
            lon: {$arrayElemAt: [ "$loc.coordinates", 0]}
        }   
     },
        {
         $match: { 
             duration: {$gt: 2} // must last than 3h and greater then 2m
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
    //print (a["_id"]["city"],a["_id"]['monthDay'],a["_id"]['day'],a["_id"]["hourDay"], a["_id"]["dayU"],a["_id"]["duration"],a["_id"]["lat"],a["_id"]["lon"])
    print (a['day'],a["hourDay"],a["lat"],a["lon"])

}