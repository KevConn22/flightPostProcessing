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
Pre-processing on data is required. Please format the data columns in the CSV as follows, with 
column headers exactly matching the following:

time | altitude | velocity

Again, please title the columns 'time', 'altitude', and 'velocity' EXACTLY. 
No unit designation is required. Unit conversions are performed based on user input within the algorithm. 
"""

## Preliminary Inputs
# Extracts data from original CSV file and pre-processes it to correspond to proper data
flightData = dataProcessing.extractData()

## Post-Processing of Flight Data
# Post-processes flight data to determine flight characteristics
realApogee = dataProcessing.findAscentCharacteristics(flightData)[0]
realApogeeTime = dataProcessing.findAscentCharacteristics(flightData)[1]
realMaxVelocity = dataProcessing.findAscentCharacteristics(flightData)[2]


descentCharacteristics = dataProcessing.findDescentCharacteristics(flightData)
realDrogueDescent = descentCharacteristics[0]
realMainDescent = descentCharacteristics[1]
realFlightTime = descentCharacteristics[2]
realDescentTime = descentCharacteristics[3]
realImpactVelocity = descentCharacteristics[4]
realMaxKineticEnergy = descentCharacteristics[5]
realMaxDrift = descentCharacteristics[6]

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
targetDescentTime = float(input("Target Descent Time [s]: "))
targetImpactVelocity = float(input("Target Impact Velocity [ft/s]: "))
targetMaxKineticEnergy = float(input("Target Max. Kinetic Energy [ft-lbf]: "))
targetMaxDrift = float(input("Target Maximum Drift [ft]: "))

targets = [targetApogee, targetApogeeTime, targetMaxVelocity, targetDrogueDescent, targetMainDescent,
           targetFlightTime, targetDescentTime, targetImpactVelocity, targetMaxKineticEnergy, targetMaxDrift]

