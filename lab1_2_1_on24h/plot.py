from matplotlib import pyplot
import json
import numpy as np
import os


if __name__=='__main__':
    
    cities = ['MA','TO','NY']
    
    for city in cities:
        folder = os.path.dirname(os.path.abspath(__file__))
        #%% Bookings filtered
        bookings = folder + "/booking_"+city+".dat"    
        f=open(bookings,"r")
        booking_lines=f.readlines()
        bookings = {}
        previous = -1
        y = []
        for l in booking_lines:
            key = l.split(' ')[1]
            value = int(l.split(' ')[2])        
    
            while (int(key) - previous) != 1:
                bookings[str(previous+1)] = 0
                y.append(str(0))
                previous += 1
                
            bookings[key] = value
            y.append(l.split(' ')[2])
            previous = int(key)
            
                    
        
        f.close()
        x = np.linspace(0,23,24)
        fig = pyplot.figure(1,figsize = (20,10))
        pyplot.stem(x,list(bookings.values()),label='Bookings')
        pyplot.xticks(x)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Bookings')
        pyplot.title('Filtered Bookings September 2017 in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/Images/booking1_'+city+'.png')
        pyplot.close(fig)
        
        #%%Bookings not filtered
        
        #Interesting to notice
        # if we put as a filter that the car has     to move we go from a max of 900 cases to less than 20
        
        
        bookings_nf = folder + "/booking_nf_" + city +".dat"
        f=open(bookings_nf,"r")
        booking_lines=f.readlines()
        y=[]
        y_nf = []
        bookings_nf = {}
        difference = {}
        previous = -1
    
        
        for l in booking_lines:
            key = l.split(' ')[1]
            value = int(l.split(' ')[2])   
            while (int(key) - previous) != 1:
                bookings_nf[str(previous+1)] = 0
                y_nf.append(str(0))
                previous += 1
                
            bookings_nf[key] = value
            y_nf.append(l.split(' ')[2])
            previous = int(key)
            
        for l in bookings_nf:
            if l  in bookings:
                y.append(bookings_nf.get(l)-bookings.get(l))
                difference[l] = (bookings_nf.get(l)-bookings.get(l))
            else:
                y.append(bookings_nf.get(l))
                difference[l] = bookings_nf.get(l)
                
        fig = pyplot.figure(2,figsize = (20,10))
        x = np.linspace(0,23,24)    
        nf = pyplot.stem(list(bookings_nf.values()),'g',markerfmt = 'go',label='Not filtered')
        f = pyplot.stem(list(bookings.values()),label='Filtered')
        pyplot.xticks(x)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('Bookings')
        pyplot.title('Comparison not_Filtered-Filtered in '+ city)
        pyplot.legend()
        fig.savefig(folder + '/Images/comparison_booking_'+city+'.png')
        pyplot.close(fig)
        
        
        fig = pyplot.figure(3,figsize = (20,10))
        x = np.linspace(0,23,24)    
        diff = pyplot.stem(list(difference.values()),label='Difference')
        pyplot.xticks(x)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('Difference')
        pyplot.title('Difference not_Filtered-Filtered in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/Images/difference_booking_'+city+'.png')
        pyplot.close(fig)

        
        #%% Parkings filtered
        parkings = folder + "/parking_"+city+".dat"    
        f=open(parkings,"r")
        parking_lines=f.readlines()
        x=[]
        y=[]
        parkings = {}
        previous = -1
    
        
        for l in parking_lines:
            key = l.split(' ')[1]
            value = int(l.split(' ')[2])   
            while (int(key) - previous) != 1:
                parkings[str(previous+1)] = 0
                y.append(str(0))
                previous += 1
                
            parkings[key] = value
            y.append(l.split(' ')[2])
            previous = int(key)
            
        f.close()
        
        fig = pyplot.figure(4,figsize = (20,10))
        x = np.linspace(0,23,24)    
        pyplot.stem(list(parkings.values()),label='Parkings')
        pyplot.xticks(x)
        pyplot.xlabel('Day of the Month')
        pyplot.ylabel('#Parkings')
        pyplot.title('Parkings September 2017 in ' + city)
        pyplot.legend()
        fig.savefig(folder + '/Images/parkings_'+city+'.png')
        pyplot.close(fig)
        
        	
        #pyplot.show()
        
    
        