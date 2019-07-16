# Multiple-regression
Multiple regression in Python 

## Usage

### Initialize object

    from multipleregression import MultipleRegression

    regression = MultipleRegression() 

### setData(X, Y) 

Set data as arrays

X parameter - multi dimentional array of independent variables
Y prameter - array of dependent variables

    X = [
     [2017, 12, 2.75, 5.3], 
     [2017, 11, 2.5, 5.3], 
     [2017, 10, 2.5, 5.3], 
     [2017, 9, 2.5, 5.3], 
     [2017, 8, 2.5, 5.4], 
     [2017, 7, 2.5, 5.6], 
     [2017, 6, 2.5, 5.5], 
     [2017, 5, 2.25, 5.5], 
     [2017, 4, 2.25, 5.5], 
     [2017, 3, 2.25, 5.6], 
     [2017, 2, 2, 5.7], 
     [2017, 1, 2, 5.9], 
     [2016, 12, 2, 6]
    ] 

    Y = [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075, 1047]

    reggression.setData(X, Y)

### importDataFromCsvFile(file [,indexOfDependentVar, skipTitleRow])

Import data from csv file

file - file path 
indexOfDependentVar - index of the column which contains the values of the dependent variables (default = 0)
skipTitleRow - skip the title line of the csv file (default=false)

    regression.importDataFromCsvFile('example_data.csv',2)


### getR2():

Return R2 of the regression

    regression.getParametersOfRegression()

### getParametersOfRegression()

Return the parameters of regression 

    regression.getR2()