//System utilization over time: aggregate rentals per hour of the day
var startDate = new ISODate("2017-09-01T00:00:00")
var endDate = new ISODate("2017-09-30T23:59:59")
var result = db.PermanentParkings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "Madrid"}],//{city: "Torino"}, {city: "New York City"}] ,
            init_date: { $gte: startDate, $lte: endDate}
        	}
    },
        {
        $project: { 
            duration: { $divide: [ { $subtract: ["$final_time", "$init_time"] }, 60 ] },
            hourDay: {$hour: "$init_date"},
            day: {$dayOfMonth: "$init_date"}
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
    print (a['day'],a["duration"])
}