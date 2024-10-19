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

# Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

# Read the entire contents into a list object
lineList = fileObj.readlines()

# Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

# Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

# Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

# Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

# List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

# Print the values
print(mmsi_idx, name_idx, fleet_idx)

#%% Task 4.3

# Create an empty dictionary
vesselDict = {}

# Iterate through all lines (except the header) in the data file:
for lineString in lineList:
    if lineString[0] in ("m"):
        continue
    #Split the data into values
    lineData = lineString.split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]
    #Extract the fleet value
    fleet = lineData[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

#%% Task 4.4
# Assign the string value 440196000 to a variable named vesselID
vesselID = '440196000'

# Use the vesselDict dictionary to look up the fleet value for 
# the vessel with the MMSI equal to the vesselID value.
vesselDict[vesselID]
# South Korea 

# Print statement
for key, value in vesselDict.items(): # the items are key value pairs so we'll pull them out into separate values
    if key == vesselID: 
        print(f"Vessel # {vesselID} flies the flag of {value}")

#%% Task 5.1
# Open .csv file
loit_fileObj = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#%% Task 5.2
# Construct list of all lines in .csv file
# Read the entire contents into a list object
loit_lineList = loit_fileObj.readlines()

# Save the contents of the first line in the list of lines to the variable "headerLineString"
loit_headerLineString = loit_lineList[0]

# Release the link to the loitering file objects 
loit_fileObj.close() 

#%% Task 5.3

# Split the headerLineString into a list of header items
loit_headerItems = loit_headerLineString.split(',')

# List the index of the mmsi, shipname, and fleet_name values
loit_mmsi_idx = loit_headerItems.index('transshipment_mmsi')
loit_start_lat_idx = loit_headerItems.index('starting_latitude')
loit_start_long_idx = loit_headerItems.index('starting_longitude')
loit_end_lat_idx = loit_headerItems.index('ending_latitude')
loit_end_long_idx = loit_headerItems.index('ending_longitude')

# Print the values
print(loit_mmsi_idx, loit_start_lat_idx, loit_start_long_idx, loit_end_lat_idx, loit_end_long_idx)

# Create empty list for keys that match the criteria
keys = []

# Loop through each data line
for loit_lineString in loit_lineList:
    if loit_lineString[0] in ("t"):
        continue

    # Split the line string into a list of data items
    loit_lineData = loit_lineString.split(',')

    # Store values in their own respective variables
    loit_mmsi = loit_lineData[loit_mmsi_idx]
    loit_start_lat = loit_lineData[loit_start_lat_idx]
    loit_end_lat = loit_lineData[loit_end_lat_idx]
    loit_start_long = loit_lineData[loit_start_long_idx]
    loit_end_long = loit_lineData[loit_end_long_idx]

    # Evaluate cross-equator criterion
    ## If it started at negative lat and ended at positive lat, it means the vessel crossed from South to North
    ## Want the boolean object to be TRUE
    lat_bool_criterion = (float(loit_start_lat) < 0) and (float(loit_end_lat) > 0)
    
    # Evaluate start longitude criterion: 
    ## If it originated within 145 to 155, it means the starting longitude has to be within that range
    long_range_criterion = 145 <= float(loit_start_long) <= 155
    
    # If both criteria are met...
    if all([lat_bool_criterion, long_range_criterion]) == True:
        # Store that mmsi
        keys.append(loit_mmsi)
        
        # Query for fleet in Task 4's dictionary
        # Use get() in case not all mmsi from loitering are in transshipment
        loit_fleet = vesselDict.get(loit_mmsi)
        # Print mmsi and fleet
        print(f"Vessel # {loit_mmsi} flies the flag of {loit_fleet}") # add key to list

# BONUS 
# Outside the loop because the keys list is defined outside of loop and keys will only be appended if criteria are met
# If no vessels meet criteria...
if len(keys) == 0:
    #  Report if no records were found
    print(f"No vessels met the criteria.")
