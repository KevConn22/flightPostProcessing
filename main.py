import math
import numpy as np
import pandas as pd

targets = []

# Define targets for flight
targetApogee = float(input("Target Apogee [ft]: "))
targetApogeeTime = float(input("Target Time to Apogee [s]: "))
targetMaxVelocity = float(input("Target Max. Velocity [ft/s]: "))

targetDrogueDescent = float(input("Target Drogue Descent Rate [ft/s]: "))
targetMainDescent = float(input("Target Main Descent Rate [ft/s]: "))
targetMainDeployment = float(input("Target Main Deployment Altitude [ft]: "))