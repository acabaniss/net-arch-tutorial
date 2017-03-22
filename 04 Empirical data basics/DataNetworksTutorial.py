# How to work with networks from data
## There will be several stages to this process:
###  1. We will load several modules to help us out along the way (very common
####       for python scripts)
###  2. We will load the data from a spreadsheet into python
###  3. We will do some form of cleaning and comparison operations to get the 
####       data into a network format
###  4. We will put the network into NetworkX, a python package for network 
####       analysis
###  5. We will try to plot the network
###  6. We will take some basic statistics
###  7. We will plot said basic statistics on the network

#Tips for working through this tutorial:
## Run each block of code as you move through the script. This often involves selecting the text and pasting it into a python window; 
## in Enthought Canopy, you can also hit Ctrl-Shift-r and it will do that for you!

#Step 1: Loading packages

## This is a standard part of every python script; python loads packages to
### handle any non-basic functions
## I'll provide a very short description of each, but all of these are readily 
### google-able

# the handy os.chdir command enables one to CHange the DIRectory one is working
## and importing/exporting data in
import os 
# numpy provides numerical functions for python like matrices
import numpy as np 
#pandas provides the ability to easily read and write spreadsheets
import pandas as pd 
# networkx is the best networks package out there
import networkx as nx 
# matplotlib is a visualization package for making plots
import matplotlib.pyplot as plt

#Step 2: Loading data

## We will want to load our data from a spreadsheet; 
### .csv files (comma seperated value) are generally the easiest to read, 
### but you can read excel in some cases.

# Change the directory:
os.chdir('c:/users/cabaniss/documents/GitHub/net-arch-tutorial/04 Empirical data basics/')
# (you'll need to change it to where your data is)
#(This is the first FUNCTION we are calling)

# Read the spreadsheet and write the data into a variable very cleverly named 
### data
data = pd.read_csv('SampleSiteData.csv')  
#(This is the first VARIABLE we are assigning)

#You've already loaded the data! That part was easy. Let's see what it looks 
## like now.
#Let's preview the data by running a function called "head", which shows the 
## first 5 rows of the data
data.head()

#We can see that the data has three variables stored in the columns; 
## Site, ObjectID, and Type
#We can also get this by looking at the columns index of the data
data.columns

#We can look at what values exist for categorical variables like Site 
## (where each value is a text or number that frequently recurrs) by using 
## the "unique" method
pd.unique(data.Site) #One way of writing this
data.Site.unique() #Another, equivalent way

#How many different sites do we have?
# len() returns the LENgth of an object, such as a list or array
len(data.Site.unique()) 
#And how many different artifacts are in our spreadsheet?
#  shape() returns the size of a spreadsheet; rows first, then columns; 
## in this case, 33 rows, 3 columns, so (33,3)
np.shape(data)


## Step 3: Cleaning and comparing the data to make a network

# The data in this case consist of objects defined by type according to the site
## they were found at
# That means that in order to get a network of the connection between PLACES, 
## we have to be able to 1) summarize and 2) compare assemblages between sites.
# There are dozens of ways to do this, and each one will depend on exactly what
## you are trying to measure or compare

# One thing we might be interested in would be comparing the distance between 
## the ceramic distributions of each site 
# In this case, our order of operations might be:
#    1. Get the distribution for each site
#    2. Use some comparison metric to make the network

# Getting the distribution for each site is most easily done with an array, 
## where each row is a site and each column is a type of pottery
# We get a list of the sites and types present in the data
sites = data.Site.unique()
types = data.Type.unique() 

#We now create an empty array that is the right size to store our counts
#np.zeros creates an empty array to store things in
counts = np.zeros((len(sites),len(types))) 

#We can then loop through every entry in our data in order to fill in the table
for i in data.index: #for every artifact in the table 
    #(This is our first FOR LOOP)
    #i is the index in our data for the current artifact
    x = [x for x in xrange(len(sites)) if sites[x] == data.Site[i]] #Get the index number of the site
    #(This is our first LIST COMPREHENSION)
    y = [y for y in xrange(len(types)) if types[y] == data.Type[i]] #Get the index number of the type
    # Now that we know which site and which type of artifact we are using, we can add this artifact to the count
    counts[x,y] += 1. # Add 1 to the count for observing this type of artifact at this site

#We now have our data tabulated! Check it out!
counts

#We can now think of ways to compare the data. For example, we can calulate percentages according to sites:
totals = counts.sum(1) #the sum function sum according to columns (0) or rows (1)
percentages = [counts[i]/totals[i] for i in xrange(len(sites))]

#Now that we have percentages, we can apply any number of distance measures, such as a simple euclidian distance measure
def euclidian_distance(x,y): #This is the first function we are defining!
    result = 0 # Create a variable to store the result
    for i in xrange(len(x)): # For each dimension (in this case pottery types)
        result += (x[i]-y[i])**2  #get the square of the difference in each dimension
    result = result**.5 # Now take the square root
    return result # and finally return that to the user
    
#We then take this function and can apply it to each distribution in turn:
distances = np.zeros((len(sites),len(sites)))
for i in xrange(len(sites)):
    for j in xrange(len(sites)):
        distances[i,j] = euclidian_distance(percentages[i],percentages[j])

#We now have a matrix of the distances between sites based on the similarity of their pottery
distances
#Note that the distance between an assemblage and itself is 0, which makes some intuitive sense since thats the comparison of two identical things!
#We can use this to build our network


#Step 4: Putting the network into NetworkX
#Now that we have our distance matrix, we can create a network in NetworkX
network = nx.from_numpy_matrix(distances)
#Your nodes currently have integer labels; it is pretty easy to add attributes to each of them, however
for i in xrange(len(sites)):
    network.node[i]['Site Name'] = sites[i]

#As it is, the "weight" of each edge is the distance; in some cases, having the 
## inverse distance is better, as it is then smaller for closer things
for i in xrange(len(sites)):
    for j in xrange(len(sites)):
        if j in network.edge[i].keys(): #If i and j are connected
            #Create a new edge attribute, similarity, which is the inverse of the distance
            network.edge[i][j]['similarity'] = 1/network.edge[i][j]['weight'] 
        
    
#Step 5: Plotting the network
# NetworkX makes plotting easy (comparatively)
# You just need to decide your layout and then play around with the parameters of it
# The basic function you'll use each time is nx.draw
nx.draw(network) #Draw the network without fiddling with anything 
# This is our first plot! (This will probably open in a new window)

#One thing you can try is different layouts:
positions = nx.spring_layout(network,weight='similarity',iterations=50,scale=3)
#Create a dictionary with labels 
labels = {}
for i in xrange(len(sites)): #For every site
    labels[i] = sites[i] # add it  to the list as an integer and the name of the site
nx.draw_networkx(network,positions,True,labels=labels)

# We now have the graph plotted, but you may notice that everything is connected to everything
# People often only consider particular edges that are particularly strong; to do this, we need to look at the network statistics

# Step 6: Getting statistics

#Edge distribution
## One place to start would be by getting a graph of how strong the relations
### are between different sites.

## Since network.edges is just a dictionary, this means we can get the 
### similarity of every edge using for loops
edge_similarity_list = []
for i in xrange(len(sites)):
    for j in xrange(len(sites)):
        # We have a double for loop now, but remember our network has no self-edges
        if i!=j:
            edge_similarity_list.append(network.edge[i][j]['similarity'])
## We now have a list of the weight of every edge
## We can visualize this using the matplotlib.pyplot package we imported earlier
### as plt
plt.hist(edge_similarity_list)

#

#You may notice that there are very few similarities above about 1; let's use 
## that as an arbitrary threshold for now
k = 1

#Let's now a) find all of the edges that are below this threshold and b) remove
## them from the network

edges_to_remove = []
for i in xrange(len(sites)):
    for j in xrange(len(sites)):
        # We have a double for loop now, but remember our network has no self-edges
        if i!=j:
            if network.edge[i][j]['similarity'] < k:
                #Remove edges that are too small
                edges_to_remove.append( (i,j) )
# We can now remove edges from the network.
network.remove_edges_from(edges_to_remove)

#Let's see our new network
positions = nx.spring_layout(network,weight='similarity',iterations=50,scale=3)
#Create a dictionary with labels 
labels = {}
for i in xrange(len(sites)): #For every site
    labels[i] = sites[i] # add it  to the list as an integer and the name of the site
nx.draw_networkx(network,positions,True,labels=labels,size=network.degree())

# Our graph is now a little better! While ideally you'd like to use a more 
## refined approach to find your threshold, this will do for the purpose
## of looking at our data as a network.

# We can now run some basic network statistics.
# This is where things get very nice very quickly.

#Degree:
network.degree()
# You now have a dictionary where the key is the site and the value is the degree
# BOOM WASNT THAT EASY!?!
# Do you want is as a histogram? You want it as a histogram. All your friends
## published a histogram of their degree distribution.

plt.hist(network.degree().values())

#OMFG YOU HAVE A HISTOGRAM IN LITERALLY ONE LINE OF CODE FROM MAKING YOUR NETWORK
# (This is a lot less impressive if you didn't have to write functions to do this
# at some point)

#Ok, you're wowed I know, but now you're jaded and want to see what else 
## NetworkX can do. 

#Centrality measures
## There are a range of centrality measures one can use in analyzing a network
## Here we will take a look at Betweenness centrality, which is related to the
### number of paths that cross through a given node

#Calculate the betweenness centrality of the network

central = nx.centrality.betweenness.betweenness_centrality(network,weight='similarity')

# There we go! No need to code your own; NetworkX has you covered.
# Let's take a look at it 

print(central)

#We can see that it gave us a dictionary with the values.
# If we want to plot the nodes by how central they are, say by changing the
## size of each node, we will want to convert to a different number
# The help documentation indicates that the default value for size is 300 units,
## whatever those might be, so let's aim for a mean size of around that.
# We can figure out what conversion factor we need by dividing 300 by the mean
## centrality
print(300./mean(central.values()))
conversion = 300./mean(central.values())

# So we need to multiply by the centrality by around 2600
# You may have also noticed that some of the nodes have a centrality of 0
# To still plot those, we may want to have some minimum size (let's say 10)
## for every node 

# Let's start by defining a new dictionary to store the size of each node
size = {}

# Let's fill it by going through each value of the centrality and 1) multiplying
## it by the conversion factor and then 2) adding 10 just to be sure that all
## nodes have some size
for i in central.keys():
    size[i] = central[i]*conversion+10
    
# We can now put this into our plotting function from above by finding the
## proper parameter
nx.draw_networkx(network,positions,True, #Change this to true if you want labels
labels=labels,node_size=size.values(),axis=False)

# Some other options include: 
central = nx.centrality.closeness.closeness_centrality(network,distance='distance')
central = nx.centrality.eigenvector_centrality(network,weight='similarity')




