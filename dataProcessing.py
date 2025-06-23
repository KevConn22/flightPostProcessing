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
    print("Hello world!")

