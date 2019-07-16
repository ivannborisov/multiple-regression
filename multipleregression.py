import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

class MultipleRegression:
    def __init__(self):
        self.X = [] 
        self.Y = []
        self.w = None
        self.r2 = None

    
    def setData (self, X, Y):
        # clear data 
        self.X = [] 
        self.Y = []

        for row in X: 
            row.insert(0,1)
        self.X = X
        self.Y = Y
        
        self.calculateRegression()

    def importDataFromCsvFile (self, file, indexOfDependentVar=0, skipTitleRow = False):
        # clear data 
        self.X = [] 
        self.Y = []

        # read data from csv file       
        f = open(file)
        lines = f.readlines()
        f.close()
        
        if skipTitleRow:
            lines = lines[1:]
        for line in lines:
            variables = line.split(',')
            dependentVar = variables[indexOfDependentVar] 
            del variables[indexOfDependentVar]
            independentVars = [float(var) for var in variables]
            independentVars.insert(0,1)
             
            self.X.append(independentVars)
            self.Y.append(float(dependentVar)) 
        
        self.calculateRegression()
    
    def calculateRegression (self):
        self.X = np.array(self.X)
        self.Y = np.array(self.Y)
        self.w = np.linalg.solve(np.dot(self.X.T, self.X), np.dot(self.X.T, self.Y))

        Yhat = self.X.dot(self.w)
        d1 = self.Y - Yhat
        d2 = self.Y - self.Y.mean()
        self.r2 = 1 - d1.dot(d1) / d2.dot(d2)

    def getR2 (self):
        return self.r2

    def getParametersOfRegression (self):
        return self.w