//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-01T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-30T23:59:59")
var endUnixTime = endDate.getTime() / 1000


var range = 3600
var result = db.PermanentBookings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "Madrid"},{city: "Torino"}, {city: "New York City"}] ,
            //init_time: { $gte: startUnixTime, $lte: endUnixTime}
            init_date: { $gte: startDate, $lte: endDate}
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
            //hourDay: {$hour: "$init_date"},
            //monthDay: {$concat: [{$substr: [{$month: "$init_date"},0,2]},"-",{$substr: [{$dayOfMonth: "$init_date"},0,2]}]},
            //dayU: {$floor: {$divide: ["$init_time", range]}},
            init_time: 1,
            final_time:1,
            //monthDay: {$month: "$init_date"},
            day: {$dayOfMonth: "$init_date"}
            //init_date:1
        }
        
     },
//      {
//          $group:
//          {
//              _id:{ city:"$city",duration:"$duration",day:"$day"},
//              total:{$sum:1}
//          }
//      },
     {
         $sort:{
             "_id.city":1,

             "_id.day":1,
             "_id.duration":1
         }
     }
     
 ],

     {allowDiskUse: true})
     
while (result.hasNext())
{
    a = result.next()
    //var diffMins = Math.round(((a["_id"]["duration"] % 86400000) % 3600000) / 60000);
    //print (a["_id"]["city"],a["_id"]["day"],a["_id"]["duration"],a["total"])

    print (a["city"],a["day"],a["duration"])


    //print(a)
}
       
