import csv
import numpy as np

def getDataSource(data_path):
    ice = []
    temp = []

    with open('Marks.csv') as f:
        df = csv.DictReader(f)
        for row in df:
            ice.append(float(row["Marks In Percentage"]))
            temp.append(float(row["Days Present"]))
    
    return{"x":temp, "y":ice}

def findCorr(datasource):
    correaltion = np.corrcoef(datasource["x"], datasource["y"])
    print("CORREALTION IS  ", correaltion[0,1])

def setup():
    data_path = "Marks.csv"
    datasource = getDataSource(data_path)
    findCorr(datasource)

setup()