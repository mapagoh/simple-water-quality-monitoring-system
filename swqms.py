## Simple Water Quality Monitoring System

import pandas as pd
import matplotlib.pyplot as plt

menu = """
¡Welcome to the Water Quality Monitoring System!

What do you want to do?

1. Record a measurement of temperature
2. View measurements of temperature
3. Calculate average measurement temperature
4. Exit

"""
measurement = []

while True:
    print(menu)
    option = int(input("Write a option: "))
    if option == 1:
        record_a_measurement = float(input("Insert a measurement of temperature "))
        measurement.append(record_a_measurement)
        print("Your measurement has been saved")
    elif option == 2:
        if len(measurement) == 0:
            print("There aren't measurements")
        else:
            for measure in measurement:
                print(measure)
    elif option == 3:
        if len(measurement) == 0:
            print("No measurements were saved")
        else:
            print("The average of the measurement of temperature is: " + str(sum(measurement)/len(measurement)))
    elif option == 4:
        exit()
    else:
        print("Incorrect option")
    
