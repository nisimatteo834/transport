//System utilization over time: aggregate rentals per hour of the day,
var startDate = new ISODate("2017-09-01T00:00:00")
var startUnixTime = startDate.getTime() /1000
var endDate = new ISODate("2017-09-30T23:59:59")
var endUnixTime = endDate.getTime() / 1000


var range = 3600
var result = db.PermanentParkings.aggregate([
    {
        $match: { // filter here what you want first
            $or: [ {city: "Torino"}],//{city: "Madrid"}, {city: "New York City"}] ,
            init_time: { $gte: startUnixTime, $lte: endUnixTime}
            //init_date: { $gte: startDate, $lte: endDate}
        	}
    },
        {
        $project: { // extract position, time, duration
            _id: 0,
            city: 1,
            //duration: { $divide: [ { $subtract: ["$final_time", "$init_time"] }, 60 ] },
            //dayofWeek: {$dayOfWeek: "$init_date"},
            hourDay: {$hour: "$init_date"},
            monthDay: {$concat: [{$substr: [{$month: "$init_date"},0,2]},"-",{$substr: [{$dayOfMonth: "$init_date"},0,2]}]},
            //dayU: {$floor: {$divide: ["$init_time", range]}},
            init_time: 1,
            monthDay: {$month: "$init_date"},
            day: {$dayOfMonth: "$init_date"},
            init_date:1
        }
        
     },
{
    $group:
    {
        _id:{monthDay : "$monthDay", day:"$day", hourDay: "$hourDay", city:"$city"},
        //_id: {city:"$city", day: "$dayU"},
        total_parking: {$sum: 1}
    }
},
{
   $sort:{
         //"_id.city":-1,"_id.monthDay":1,"_id.day":1,"_id.hourDay":1
       "_id.day":1,
       "_id.hourDay":1
        }
    }
 ])
        
while(result.hasNext()) {
    a = result.next()
    //print (a)
    var str = (a["_id"]["day"].toString()).concat('-')
    var str2 = str.concat(a["_id"]["hourDay"].toString())
    print (a["_id"]["city"],a["_id"]['monthDay'],a["_id"]['day'],a["_id"]["hourDay"],a["total_parking"], str2)
    //var hours = date.getHours();
// Minutes part from the timestamp
    //var minutes = "0" + date.getMinutes();

// Will display time in 10:30:23 format
    //var formattedTime = hours; //+ ':' + minutes.substr(-2) ;//+ ':' + seconds.substr(-2);
      
    //print (a["_id"]["city"],a["_id"][""]a["_id"]["day"],a['total_parking'],formattedTime,new Date (a["_id"]["day"]*1000))
}
