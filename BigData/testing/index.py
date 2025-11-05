# import json
# with open('dati.json', "rt") as f:
#     js = f.read()
#     arr = json.loads(js)
#     print(type(arr), len(arr))
    
import pandas as pd
    
df = pd.read_json('dati.json')
print(df.duplicated().sum())
print(df.info())
# new_df = df.drop_duplicates().copy()
# print(new_df.info())
# print(new_df.to_string())