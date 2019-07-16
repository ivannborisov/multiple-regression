from multipleregression import MultipleRegression

regression = MultipleRegression()

regression.importDataFromCsvFile('example_data.csv',2)
print('Parameters of regression:')
print(regression.getParametersOfRegression())
print('R2:')
print(regression.getR2())