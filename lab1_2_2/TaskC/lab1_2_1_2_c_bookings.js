//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-18T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-24T23:59:59")
var endUnixTime = endDate.getTime() / 1000


var range = 3600
var result = db.PermanentBookings.aggregate([
    {
        $match: { 
            $or: [ {city: "Madrid"},{city: "Torino"}, {city: "New York City"}] ,
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
            init_time: 1,
            final_time:1,
            day: {$dayOfMonth: "$init_date"}
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
    print (a["city"],a["day"],a["duration"])


    //print(a)
}
       
