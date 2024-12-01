import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# myvar = pandas.DataFrame(mydataset)

# print(myvar)

# series1 = pd.Series([1,2,3,4])
# print(series1)
df = pd.DataFrame( 
     [[1, 2, 3], 
     [4, 6, 8],
     [10, 11, 12]],
     index=[1, 2, 3], 
     columns=['a', 'b', 'c'])


print(df)