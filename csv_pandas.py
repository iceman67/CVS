import csv
import pandas as pd 

## open the file containing the data
data = pd.read_csv("artificial_roads_by_region.csv")
#print(data.head())


# To get the column 2011
data_2011 = data.loc[:, '2011']
#data_2011 = data['2011']

#Drop the Rows with NaN Values in Pandas DataFrame
drop_data_2011 = data_2011.dropna(axis = 0, how ='any')
after_drop_total_raws = drop_data_2011.count()
print ("count = ", after_drop_total_raws)
print (drop_data_2011[drop_data_2011.index <11])

'''
## open the file containing the data
fin = open("data/input_data/artificial_roads_by_region.csv","r",newline="")

total_roads=0
## iterate over the rows in the CSV file
print("first 10 values of the 2011 column:")
for row in reader:
    ## print out the first 10 values of 2011
    if reader.line_num <= 11:
        print(row["2011"])
    if row["2011"] != "":
        total_roads+=float(row["2011"])

print("total leangth of roads as of 2011:")
print(total_roads)
fin.close()
'''
