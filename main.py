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

root = Tk()
root.title("Altitude Post-Processing Tool")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)

# Define user inputs for results
ttk.Label(mainframe, text="Input Parameters:").grid(column=1, row=1, columnspan=2, sticky=N)

targetApogee = StringVar()
targetApogeeTime = StringVar()
targetMaxVelocity = StringVar()
targetDrogueDescent = StringVar()
targetMainDescent = StringVar()
targetFlightTime = StringVar()
targetDescentTime = StringVar()
targetImpactVelocity = StringVar()
targetMaxKineticEnergy = StringVar()
targetMaxDrift = StringVar()

normWidth = 15
apogeeEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetApogee)
apogeeTimeEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetApogeeTime)
maxVelocityEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetMaxVelocity)
drogueDescentEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetDrogueDescent)
mainDescentEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetMainDescent)
flightTimeEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetFlightTime)
descentTimeEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetDescentTime)
impactVelocityEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetImpactVelocity)
maxKineticEnergyEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetMaxKineticEnergy)
maxDriftEntry = ttk.Entry(mainframe, width=normWidth, textvariable=targetMaxDrift)

apogeeEntry.grid(column = 2, row = 4, sticky=(N))
apogeeTimeEntry.grid(column=2, row = 5, sticky = N)
maxVelocityEntry.grid(column=2, row = 6, sticky=N)
drogueDescentEntry.grid(column=2, row = 7, sticky=N)
mainDescentEntry.grid(column=2, row=8, sticky = N)
flightTimeEntry.grid(column=2, row=9, sticky=N)
descentTimeEntry.grid(column=2,row=10,sticky=N)
impactVelocityEntry.grid(column=2,row=11,sticky=N)
maxKineticEnergyEntry.grid(column=2, row = 12, sticky=N)
maxDriftEntry.grid(column=2, row=13, sticky=N)

ttk.Label(mainframe, text="Apogee [ft]:").grid(column=1, row = 4, sticky=N)
ttk.Label(mainframe, text="Maximum Velocity [ft/s]:").grid(column=1, row = 5,  sticky=N)
ttk.Label(mainframe, text="Time to Apogee [s]:").grid(column=1, row=6, sticky=N)
ttk.Label(mainframe, text="Drogue Descent Rate [ft/s]:").grid(column=1, row=7, sticky=N)
ttk.Label(mainframe, text="Main Descent Rate [ft/s]:").grid(column=1, row=8, sticky=N)
ttk.Label(mainframe, text="Total Flight Time [s]:").grid(column=1, row = 9, sticky=N)
ttk.Label(mainframe, text="Descent Time [s]:").grid(column=1, row = 10, sticky=N)
ttk.Label(mainframe, text="Impact Velocity [ft/s]:").grid(column=1, row = 11, sticky=N)
ttk.Label(mainframe, text="Maximum Kinetic Energy [ft-lbf]:").grid(column=1, row = 12, sticky= N)
ttk.Label(mainframe, text="Maximum Vehicle Drift [ft]:").grid(column=1, row = 13, sticky = N)

ttk.Label(mainframe, text="Flight Parameter:").grid(column=1, row = 3, sticky=N)
ttk.Label(mainframe, text="Targets:").grid(column=2, row = 3, sticky = N)
ttk.Label(mainframe, text="Actual:").grid(column=3, row = 3, sticky=N)

ttk.Button(mainframe, text="Select File:", command=dataProcessing.extractData).grid(column=1, row=2, sticky=N)
ttk.Button(mainframe, text="Analyze Flight Results", command=dataProcessing.findFlightCharacteristics).grid(column=3, row=2, sticky=N)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()