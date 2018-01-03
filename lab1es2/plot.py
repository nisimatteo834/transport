from matplotlib import pyplot
import json
import numpy as np
import os


if __name__=='__main__':
    
    city = 'MA'
    folder = os.path.dirname(os.path.abspath(__file__))
    #%% Bookings filtered
    bookings = folder + "/"+city+".dat"    
    f=open(bookings,"r")
    booking_lines=f.readlines()
    bookings = {}
    previous = int(booking_lines[0].split(' ')[1])-1
    y = []
    for l in booking_lines:
        key = l.split(' ')[1]
        value = int(l.split(' ')[0])        

        while (int(key) - previous) != 1:
            bookings[str(previous+1)] = 0
            y.append(str(0))
            previous += 1
            
        bookings[key] = value
        y.append(l.split(' ')[0])
        previous = int(key)
        
                
    
    f.close()
    
    fig = pyplot.figure(1,figsize = (20,10))
    x = np.linspace(1,30,720)    
    pyplot.plot(x,list(bookings.values()),label='Bookings')
    pyplot.xlim(0.5,30.5)
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('#Bookings')
    pyplot.title('Filtered Bookings September 2017 in ' + city)
    pyplot.legend()
    fig.savefig(folder + '/booking_'+city+'.png')
    
    #%%Bookings not filtered
    
    #Interesting to notice
    # if we put as a filter that the car has     to move we go from a max of 900 cases to less than 20
    
    
    bookings_nf = folder + "/" + city +"_nf.dat"
    f=open(bookings_nf,"r")
    booking_lines=f.readlines()
    y=[]
    y_nf = []
    bookings_nf = {}
    difference = {}
    previous = int(booking_lines[0].split(' ')[1])-1

    
    for l in booking_lines:
        key = l.split(' ')[1]
        value = int(l.split(' ')[0])   
        while (int(key) - previous) != 1:
            bookings_nf[str(previous+1)] = 0
            y_nf.append(str(0))
            previous += 1
            
        bookings_nf[key] = value
        y_nf.append(l.split(' ')[0])
        previous = int(key)
        
    for l in bookings_nf:
        if l  in bookings:
            y.append(bookings_nf.get(l)-bookings.get(l))
            difference[l] = (bookings_nf.get(l)-bookings.get(l))
        else:
            y.append(bookings_nf.get(l))
            difference[l] = bookings_nf.get(l)
            
    fig = pyplot.figure(2,figsize = (20,10))
    x = np.linspace(1,30,720)    
    nf = pyplot.plot(x,list(bookings_nf.values()),label='Not filtered')
    f = pyplot.plot(x,list(bookings.values()),label='Filtered')
    #pyplot.plot(x,list(difference.values()))
    #pyplot.plot(x,y_nf)
    pyplot.xlim(0.5,30.5)
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('Bookings')
    pyplot.title('Comparison not_Filtered-Filtered in '+ city)
    pyplot.legend()
    fig.savefig(folder + '/comparison_booking_'+city+'.png')
    
    
    fig = pyplot.figure(3,figsize = (20,10))
    x = np.linspace(1,30,720)    
    diff = pyplot.plot(x,list(difference.values()),label='Difference')
    pyplot.xlim(0.5,30.5)
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('Difference')
    pyplot.title('Difference not_Filtered-Filtered in ' + city)
    pyplot.legend()
    fig.savefig(folder + '/difference_booking_'+city+'.png')
    
    #%% Parkings filtered
    parkings = folder + "/"+city+"2.dat"    
    f=open(parkings,"r")
    parking_lines=f.readlines()
    x=[]
    y=[]
    parkings = {}
    previous = int(parking_lines[0].split(' ')[1])-1

    
    for l in parking_lines:
        key = l.split(' ')[1]
        value = int(l.split(' ')[0])   
        while (int(key) - previous) != 1:
            parkings[str(previous+1)] = 0
            y.append(str(0))
            previous += 1
            
        parkings[key] = value
        y.append(l.split(' ')[0])
        previous = int(key)
        
    f.close()
    
    fig = pyplot.figure(4,figsize = (20,10))
    x = np.linspace(1,30,720)    
    pyplot.plot(x,list(parkings.values()),label='Parkings')
    pyplot.xlim(0.5,30.5)
    pyplot.xlabel('Day of the Month')
    pyplot.ylabel('#Parkings')
    pyplot.title('Parkings September 2017 in ' + city)
    pyplot.legend()
    fig.savefig(folder + '/parkings_'+city+'.png')
    
    	
    pyplot.show()
      
        
        
    
        