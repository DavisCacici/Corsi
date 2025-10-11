import pandas as pd 
df = pd.read_csv('file.csv')

print(df.to_string())
"""
For show the information about the data, you could use info() method
"""
print("-------------------------------------------")
print(df.info())


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
# df.dropna(inplace = True)

"""
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
"""

print("-------------------------------------------")
fill_df = df.fillna(130)
print(fill_df.to_string())

# #or for specific column
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
You could bulk replace large dataset with a rules 
"""
print("-------------------------------------------")

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print(df.to_string())
"""
Or you could remove all rows that contains wrong data.
"""
print("-------------------------------------------")
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
    
"""
DUPLICATES 
Duplicate rows are rows that have been registered more than one time. 

By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
To discover duplicates, we can use the duplicated() method.
"""
    
print("-------------------------------------------")
print(df.duplicated())
#For remove duplicates, use the drop_duplicates() method
final_df = df.drop_duplicates().copy()
print(final_df.to_string()) 

"""
CORRELATIONS
The corr() method calculates the relationship between each column in your data set.
The corr() method ignores "not numeric" columns.
1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.
"""

print("-------------------------------------------")
final_df.dropna(subset=['Date'], inplace=True)
x = final_df["Calories"].mean()
final_df.fillna({"Calories": x}, inplace=True)
print(final_df.to_string()) 
print(final_df.corr())
