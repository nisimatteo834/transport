import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import msvcrt as m
import pylab

if __name__ == '__main__':

    fileName = "Torino_walking_Duration.txt"
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

    bins = np.arange(0, 140, 5)
    fig1 = plt.figure(1)
    plt.figure(figsize = (10,5))
    plt.title(city +" Rentals given the Duration of Walking In September 2017")
    plt.xlabel("Walking Duration[min]")
    plt.ylabel("Number of Bookings")
    plt.grid(True)
    plt.hist(pt_duration, bins)
    fig1.show()

    pylab.show()
    m.getch()