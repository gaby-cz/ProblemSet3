#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: 

# Task 4: Lists, dictionaries, string manipulation, and iteration
#   Create a dictionary listing the attributes of each vessel listed 
#       in the transshipment_vessels_2018723.csv file
#   Loop through the records in the loitering_events_2018723.csv file,
#       and for each vessel observed within a defined geographic region, print information about the vessel.
# Task 5: Scripting task
#    Use the GFW “loitering event” dataset. This dataset contains 
#    location and movement data of vessels classified as moving idly, 
#    as opposed to steaming to a certain destination. 
#    We want to write some Python code that scans these data for 
#    particular records, namely those loitering events that cross the 
#    equator and originated within a certain longitudinal band. 
#    And if any records are found, it prints out the MMSI of the vessel 
#    and its fleet - using the dictionary created above to tell us.
#
# Author: Gaby Czarniak (gabriella.czarniak@duke.edu)
# Date:   October 2024
#--------------------------------------------------------------

#%% Task 4.1 - Edit code to print as requested

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)
#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)
# %%
