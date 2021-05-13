import pandas as pd

def writeexternal(df1):
    df1.to_csv("outputpanda.csv", mode='a', index = False, header = False)
    
#dataframe
df = pd.read_csv("SampleData.csv")#, index_col=0)

df_header_index_col = pd.read_csv("SampleData.csv", index_col=0)

currentID = ""
oldID = ""
counter = 0
for index, row in df.iterrows():
    #this outputs the unique ID of this row: print(row[0])
    
    currentID = row[0]
    if currentID == oldID:
        counter += 1
    else:
        counter = 1
    #print(counter)
    if counter == 10:
        df1 = df.iloc[index-9:index+1,:]
        print(df1)
        writeexternal(df1)
    oldID = currentID

