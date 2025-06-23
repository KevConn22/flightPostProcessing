import math
import numpy as np
import pandas as pd
import flightResults

filepath = 'C:/Users/gator/Downloads/pdfFiltBaroFixed.csv'
flightData = flightResults.extractData(filepath)

# Define targets for flight
targets = []

targetApogee = float(input("Target Apogee [ft]: "))
targetApogeeTime = float(input("Target Time to Apogee [s]: "))
targetMaxVelocity = float(input("Target Max. Velocity [ft/s]: "))

targetDrogueDescent = float(input("Target Drogue Descent Rate [ft/s]: "))
targetMainDescent = float(input("Target Main Descent Rate [ft/s]: "))
targetMainDeployment = float(input("Target Main Deployment Altitude [ft]: "))