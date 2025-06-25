import math
import numpy as np
import pandas as pd
import dataProcessing
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def extractData():
    units = input("Is data represented in SI units? [Type 'Y' or 'N']: ")
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    altimeterData = pd.read_csv(file)

    if altimeterData.at[0, 'time'] < 0:
        altimeterData['time'] = altimeterData['time'] - altimeterData.at[0, 'time']
    if units == "Y" or "y":
        altimeterData['altitude'] = altimeterData['altitude'] * 3.28084
        altimeterData['velocity'] = altimeterData['velocity'] * 3.28084
    return(altimeterData)

def findAscentCharacteristics(data):
    ascentCharacteristics = []
    
    apogee = max(data['altitude'])
    ascentCharacteristics.append(apogee)

    apogeeIndex = data['altitude'].idxmax()
    apogeeTime = data.at[apogeeIndex, 'time']
    ascentCharacteristics.append(apogeeTime)

    velocity = max(data['velocity'])
    ascentCharacteristics.append(velocity)

    return(ascentCharacteristics)

def findDescentCharacteristics(data):
    descentCharacteristics = []
    
    mainAltitude = float(input("Target Main Deployment Altitude [ft]: "))
    lapse = float(input("Expected Main Deployment Lapse Time [s]: "))
    impactTimeInterval = float(input("Duration of Impact Velocity Calculation [s]: "))
    heaviestSection = float(input("Heaviest Section Mass [oz]: "))
    apogeeIndex = data['altitude'].idxmax()
    apogeeTime = data.at[apogeeIndex, 'time']

    # Determine descent rate under drogue parachute
    count = 0
    velocity = 0
    time = 0
    for i in range(len(data)):
        if data.at[i, 'time'] > apogeeTime and data.at[i, 'altitude'] > mainAltitude and data.at[i, 'velocity'] < 0:
            count = count + 1
            velocity = velocity + data.at[i, 'velocity']
            time = data.at[i, 'time']
    drogueDescentRate = velocity / count
    descentCharacteristics.append(drogueDescentRate)

    # Determine descent rate under main parachute
    count = 0
    velocity = 0
    mainDeployTime = time
    for i in range(len(data)):
        if data.at[i, 'time'] > mainDeployTime + lapse and i > 0:
            if data.at[i, 'velocity'] < 0:
                if abs(data.at[i-1, 'velocity']) < 0.50 and data.at[i, 'time'] > mainDeployTime + lapse + 1:
                    break
                elif data.at[i-1, 'altitude'] < 0 and data.at[i, 'time'] > mainDeployTime + lapse + 1:
                    break
                else:
                    velocity = velocity + data.at[i, 'velocity']
                    time = data.at[i, 'time']
                    count = count + 1
            else:
                velocity = velocity
        else:
            velocity = velocity
    mainDescentRate = velocity / count
    descentCharacteristics.append(mainDescentRate)

    # Determine total flight time
    flightTime = time
    descentCharacteristics.append(flightTime)

    # Determine descent time
    descentTime = flightTime - apogeeTime
    descentCharacteristics.append(descentTime)

    # Determine impact velocity of vehicle
    count = 0
    velocity = 0
    impactStartTime = flightTime - impactTimeInterval
    for i in range(len(data)):
        if data.at[i, 'time'] > impactStartTime and data.at[i, 'time'] < flightTime:
            velocity = velocity + data.at[i, 'velocity']
            count = count + 1
    impactVelocity = velocity / count
    descentCharacteristics.append(impactVelocity)

    # Determine maximum kinetic energy
    heaviestSection = heaviestSection / 16 / 32.174
    maxKineticEnergy = 0.5 * heaviestSection * impactVelocity ** 2
    descentCharacteristics.append(maxKineticEnergy)

    # Determine maximum vehicle drift
    maxDrift = descentTime * 20 * 5280 / 3600
    descentCharacteristics.append(maxDrift)
    return(descentCharacteristics)


def findFlightCharacteristics(data):
    print("Hello world!")
