from matplotlib import pyplot
import json
import numpy as np
import os


if __name__=='__main__':
    
  
    folder = os.path.dirname(os.path.abspath(__file__))
    #%% Bookings filtered
    bookings = folder + "/torino.dat"    
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
    
    pyplot.figure(1)
    pyplot.plot(y)
    pyplot.title('Bookings')
    #%%Bookings not filtered
    
    #Interesting to notice
    # if we put as a filter that the car has     to move we go from a max of 900 cases to less than 20
    
    bookings_nf = folder + "/torino_nf.dat"
    f=open(bookings_nf,"r")
    booking_lines=f.readlines()
    y=[]
    bookings_nf = {}
    difference = {}
    previous = int(booking_lines[0].split(' ')[1])-1

    
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
        
    for l in bookings_nf:
        if l  in bookings:
            y.append(bookings_nf.get(l)-bookings.get(l))
            difference[l] = (bookings_nf.get(l)-bookings.get(l))
        else:
            y.append(bookings_nf.get(l))
            difference[l] = bookings_nf.get(l)
            
    pyplot.figure(3)
    pyplot.plot(y)
    pyplot.title('Difference not_Filtered-Filtered')
    
    #%% Parkings filtered
    parkings = folder + "/torino2.dat"    
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
    
    pyplot.figure(2)
    pyplot.plot(y)
    pyplot.title('Parkings')
    	
    	
    pyplot.show()
      
        
        
    
        