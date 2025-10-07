import pandas as pd 
df = pd.read_csv('file.csv')

print(df.to_string())

"""
Bad data could be

-   Empty cells
-   Data in wrong format
-   Wrong data
-   Duplicates

Empty cells can potentially give you a wrong result when you analyze data.
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""
print("-------------------------------------------")
new_df = df.dropna()
print(new_df.to_string())

#if you want change original DataFrame use inplace = True
#df.dropna(inplace = True)

"""
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
"""

print("-------------------------------------------")
fill_df = df.fillna(130)
print(fill_df.to_string())

#or for specific column
print("-------------------------------------------")
fill_df = df.fillna({"Calories":130})
print(fill_df.to_string())

"""
WRONG FORMAT
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, 
or convert all cells in the columns into the same format.
"""
print("-------------------------------------------")

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())
"""
As you can see from the result, the date in row 26 was fixed, 
but the empty date in row 22 got a NaT (Not a Time) value, 
in other words an empty value. 
One way to deal with empty values is simply removing the entire row. 
"""
print("-------------------------------------------")
new_df = df.dropna(subset=['Date'])
print(new_df.to_string())

"""
WRONG DATA
does not have to be "empty cells" or "wrong format", it can just be wrong, 
like if someone registered "199" instead of "1.99".
Sometimes you can spot wrong data by looking at the data set, 
because you have an expectation of what it should be.
If you take a look at our data set, you can see that in row 7, 
the duration is 450, but for all the other rows the duration is between 30 and 60.
It doesn't have to be wrong, but taking in consideration that this is 
the data set of someone's workout sessions, 
we conclude with the fact that this person did not work out in 450 minutes.

We replace wrong data, in this case the value should be '45' instead of '450',
and we could just insert '45' in row 7
"""

print("-------------------------------------------")
new_df.loc[7, 'Duration'] = 45
print(new_df.to_string())

"""
For small data sets you might be able to replace the wrong data one by one, 
but not for big data sets.
"""
print("-------------------------------------------")
print(new_df.index)
