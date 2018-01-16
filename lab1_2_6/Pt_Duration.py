import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import msvcrt as m
import pylab

if __name__ == '__main__':

    fileName = "Torino_Pt_Duration.txt"
    city = "Torino"
    file = open(fileName, "r")
    data = file.readlines()
    file.close()
    booking = []
    pt_duration =[]

    for i in data:
        rental, pt = i.split(' ')
        booking.append(float(rental))
        pt_duration.append(float(pt))
    print(pt_duration)

    bins = np.arange(0, 100, 5)
    fig1 = plt.figure(1)
    plt.figure(figsize = (10,5))
    plt.title(city +" Rentals given the Duration of Public Transport In September 2017")
    plt.xlabel("Public Trasport Duration[min]")
    plt.ylabel("Number of Bookings")
    plt.grid(True)
    plt.hist(pt_duration, bins)
    fig1.show()
    """
    fig2 = plt.figure(2)
    plt.figure(figsize = (10,5))
    plt.title(city +" Public Trasport Duration Vs Bookings Duration In September 2017")
    plt.xlabel("Public Trasport Duration[min]")
    plt.ylabel("Bookings Duration[min]")
    plt.grid(True)
    plt.scatter(pt_duration, booking,marker="+")
    fig2.show()
    """
    pylab.show()
    m.getch()