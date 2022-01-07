import csv
import numpy as np

def getDataSource(data_path):
    ice = []
    temp = []

    with open('Coffe.csv') as f:
        df = csv.DictReader(f)
        for row in df:
            ice.append(float(row["Coffee in ml"]))
            temp.append(float(row["sleep in hours"]))
    
    return{"x":temp, "y":ice}

def findCorr(datasource):
    correaltion = np.corrcoef(datasource["x"], datasource["y"])
    print("CORREALTION IS  ", correaltion[0,1])

def setup():
    data_path = "Coffe.csv"
    datasource = getDataSource(data_path)
    findCorr(datasource)

setup()