import math
import numpy as np
import pandas as pd
import dataProcessing
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

"""
Program is designed to post-process the results of SRM model rockets, using altimeter data.
Pre-processing on data is required. Please format the data columns in the CSV as follows, without column headers:

Time  |  Altitude  |  Velocity

No unit designation is required. Unit conversions are performed based on subsequent user input.
"""

## Preliminary Inputs
# Extracts data from original CSV file and pre-processes it to correspond to proper data
flightData = dataProcessing.extractData()
print(flightData)

## Post-Processing of Flight Data
# Post-processes flight data to determine flight characteristics
realApogee = dataProcessing.findAscentCharacteristics(flightData)[0]
realApogeeTime = dataProcessing.findAscentCharacteristics(flightData)[1]
realMaxVelocity = dataProcessing.findAscentCharacteristics(flightData)[2]

realDrogueDescent = dataProcessing.findDescentCharacteristics(flightData)
## Flight Profile Target Definition
# Subsequent user inputs define target values for in-flight performance characteristics
targets = []

print('')
print('Target Inputs:')
print('')

targetApogee = float(input("Target Apogee [ft]: "))
targetApogeeTime = float(input("Target Time to Apogee [s]: "))
targetMaxVelocity = float(input("Target Max. Velocity [ft/s]: "))

targetDrogueDescent = float(input("Target Drogue Descent Rate [ft/s]: "))
targetMainDescent = float(input("Target Main Descent Rate [ft/s]: "))
targetFlightTime = float(input("Target Total Flight Time [s]: "))
targetDescentTime = targetFlightTime - targetApogeeTime
targetMaxKineticEnergy = float(input("Target Max. Kinetic Energy [ft-lbf]: "))
targetMaxDrift = float(input("Target Maximum Drift [ft]: "))

targets = [targetApogee, targetApogeeTime, targetMaxVelocity, targetDrogueDescent, targetMainDescent,
           targetFlightTime, targetDescentTime, targetMaxKineticEnergy, targetMaxDrift]