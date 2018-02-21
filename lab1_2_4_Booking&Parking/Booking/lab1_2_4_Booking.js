var startDate = new ISODate("2017-09-01T00:00:00")
var endDate = new ISODate("2017-09-30T23:59:59")
var result = db.PermanentBookings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "New York City"}],//{city: "Torino"}, {city: "Madrid"}] ,
            init_date: { $gte: startDate, $lte: endDate}
        	}
    },
        {
        $project: { // extract position, time, duration
            _id: 0,
            moved: { $ne: [

                {$arrayElemAt: [ "$origin_destination.coordinates", 0]},

                {$arrayElemAt: [ "$origin_destination.coordinates", 1]}

                ]

            },
            duration: { $divide: [ { $subtract: ["$final_time", "$init_time"] }, 60 ] },
            hourDay: {$hour: "$init_date"},
            day: {$dayOfMonth: "$init_date"}
        }
     },

        {
         $match: {
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
    print (a["day"],a["duration"])
}