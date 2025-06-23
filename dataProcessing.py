import pandas as pd
import numpy as np
import math

def extractData(filepath):
    # units = input("Define Units (I for SI, C for Customary): ")

    altimeterData = pd.read_csv(filepath)
    return(altimeterData)