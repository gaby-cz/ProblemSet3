#-------------------------------------------------------------
# ProblemSet3_Part1.py
#
# Description: 
# Task 1: Python syntax & string manipulation
# Task 2: Lists and iteration
#
# Author: Gaby Czarniak (gabriella.czarniak@duke.edu)
# Date:   October 2024
#--------------------------------------------------------------

#%% Task 1 - Edit code to print as requested
# /*--PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = "20322" 

print (mountain + ', sometimes \ncalled "' + nickname + '",')
print ("is " + elevation + "' above sea level.")

#%% Task 2 - Lists and Iteration
# /*--PS3: Code Block 2--*/

# Subtask 2.1: Assign a variable named data_folder to the string object that prints as "W:\859_data\triangle"
data_folder = r"W:\859_data\triangle"
print(data_folder + "\n") # Added \n so that there's space between this and what is printed for Subtask 2.5

# Subtask 2.2: Create a list object called data_list containing three string objects
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

# Subtask 2.3: Assign a variable named user_item and set it to the string "roads.shp"
user_item = r"roads.shp"

# Subtask 2.4: Add user_item string to the data_list list
data_list.append(user_item)

# Subtask 2.5: Loop through each item in data_list and for each object print full Windows path of each dataset    
    # Print output and check against PSet3 instructions
for item in data_list:
    # Concatenate the data_folder string with the item in the data_list
    print(data_folder + "\\" + item)
# %%
