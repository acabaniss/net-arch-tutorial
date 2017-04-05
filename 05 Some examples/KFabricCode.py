import numpy as np
import os
import pandas as pd
import networkx as nx

os.chdir('C:/users/cabaniss/documents/github/net-arch-tutorial/05 Some examples')

# The following function requires the 'xlrd' module to be installed already
# Make sure it is by going to package manager and searching for it in the 
## available packages

#Step 0: Load the data
data = pd.read_excel('KFabricData.xlsx','Sheet1')

data.columns #See what columns exist

data.ix[0] #See what one row looks like

data.head() # See what the first 5 rows look like

# Step 1: Clean the data

#Do any fields need to be cleaned or altered?
# Need to replace blank values with 0?
cleaned_data = data.replace(np.nan,0)

# Need to check that site names are correctly spelled?



# Step 2: build a matrix


# Step 3: build a network


# Step 4: Run network metrics