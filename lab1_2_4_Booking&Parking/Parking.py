import matplotlib.pyplot as plt
import numpy as np
import msvcrt as m
import pylab

if __name__ == '__main__':

    average = []
    median = []
    standard_deviation = []
    percentile = []
    booking = []

    counter = 0
    """
    #Torino
    fileName = "Torino_Parking.txt"
    city = "Torino"
    file = open(fileName,"r")
    data = file.readlines()
    file.close()
    for line in data:
        booking.append(int(line))
        counter +=1
        if(counter ==30):
            for i in range(77):
                booking.append(0)
    print(booking)

    """
    """
    #Madrid
    fileName = "Madrid_Parking.txt"
    city = "Madrid"
    file = open(fileName,"r")
    data =file.readlines()
    file.close()
    for line in data:
        booking.append(int(line))
        counter +=1
        if(counter ==30):
            for i in range(77):
                booking.append(0)
    print(booking)
    """

    # New York City
    fileName = "NewYork_Parking.txt"
    city = "New York City"
    file = open(fileName, "r")
    data = file.readlines()
    file.close()
    for line in data:
        booking.append(int(line))
        counter += 1
        if (counter == 24):
            for i in range(77):
                booking.append(0)
    print(booking)

    day = []
    count = 0
    j = 0
    while (j < 720):
        if (count < 24):
            day.append(booking[j])
            count += 1
            j += 1
            if (j == 720):
                print(day)
                average.append(np.mean(day))
                median.append(np.median(day))
                standard_deviation.append(np.std(day))
                percentile.append(np.percentile(day, 75))
        else:
            print(day)
            average.append(np.mean(day))
            median.append(np.median(day))
            standard_deviation.append(np.std(day))
            percentile.append(np.percentile(day, 75))
            del day[:]
            count = 0
    fig1 = plt.figure(1)
    plt.figure(figsize=(10, 5))
    plt.title(city + " Parking Statistics")
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