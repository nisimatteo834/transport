import matplotlib.pyplot as plt
import numpy as np
import msvcrt as m
import pylab

if __name__ == '__main__':

    average = []
    median = []
    standard_deviation = []
    percentile = []
    booking = {}
    """
    # Torino
    fileName = "Torino_Booking.txt"
    city = "Torino"
    file = open(fileName,"r")
    data = file.readlines()[2:-1]
    file.close()
    for i in data:
        day, duration = [a.strip() for a in i.split(' ')]
        booking.setdefault(int(day), []).append(float(duration))
    for key in booking.keys():
        val = booking[key]
        average.append(np.mean(val))
        median.append(np.median(val))
        standard_deviation.append(np.std(val))
        percentile.append(np.percentile(val, 75))
    print(average)
    print(median)
    print(standard_deviation)
    print(percentile)
    """
    """
    #Madrid
    fileName = "Madrid_Booking.txt"
    city = "Madrid"
    file = open(fileName,"r")
    data = file.readlines()[2:-1]
    file.close()
    for i in data:
        day, duration = [a.strip() for a in i.split(' ')]
        booking.setdefault(int(day), []).append(float(duration))
    for key in booking.keys():
        val = booking[key]
        average.append(np.mean(val))
        median.append(np.median(val))
        standard_deviation.append(np.std(val))
        percentile.append(np.percentile(val, 75))
    print(average)
    print(median)
    print(standard_deviation)
    print(percentile)

    """
    # New York City
    fileName = "NewYork_Booking.txt"
    city = "New York City"
    file = open(fileName,"r")
    data = file.readlines()[2:-1]
    file.close()
    for i in data:
        day, duration = [a.strip() for a in i.split(' ')]
        booking.setdefault(int(day), []).append(float(duration))
    for key in booking.keys():
        val = booking[key]
        average.append(np.mean(val))
        median.append(np.median(val))
        standard_deviation.append(np.std(val))
        percentile.append(np.percentile(val, 75))
    print(average)
    print(median)
    print(standard_deviation)
    print(percentile)

    fig1 = plt.figure(1)
    plt.figure(figsize=(10, 5))
    plt.title(city + " Booking Statistics")
    plt.xlabel("Days")
    plt.ylabel("Duration[min]")
    plt.xlim(0.5,30.5)
    dim = np.arange(1, 31, 1);
    plt.grid(True)
    plt.plot(dim,average, label="Average")
    plt.plot(dim,median, label="Median")
    plt.plot(dim,standard_deviation, label="Std")
    plt.plot(dim,percentile, label="Percentile[75%]")
    plt.xticks(dim)
    plt.legend(loc=2)
    fig1.show()
    pylab.show()
    m.getch()
