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
cleaned_data['No. of Sherds']
# Need to check that site names are correctly spelled?

new_counts = []
for i in cleaned_data['No. of Sherds']:
    if i == 0:
        new_counts.append(None)
    else:
        new_counts.append(i)
cleaned_data['No. of Sherds'] = new_counts

new_counts_too = [i if i != 0 else None for i in cleaned_data['No. of Sherds']]

site_names = cleaned_data['Site Name'].unique()
site_names.sort()

# Step 2: build a network

# Make a new network
net = nx.Graph()

# Add our nodes
for x in cleaned_data['Site Number']:
    net.add_node(x)
  
# OR  
for x in cleaned_data.index:    
    net.add_node(cleaned_data['Site Number'][x],{'Site Name' : cleaned_data['Site Name'][x]})
    
#See the results! This should give a dictionary with the site number as the key
## and the site name as the 
net.node

net.node[101]

# Define connections between nodes
for i in net.nodes(): # Alternatively, for i in net.node.keys(); they are the same
    for j in net.nodes():
        # i and j take on every pair of sites
        # Check that i != j AND edge[i][j] does not exist
        if i != j and j not in net.edge[i].keys():
            overlaps = 0
            wi = [x for x in cleaned_data.index if cleaned_data['Site Number'][x] == i][0]
            wj = [x for x in cleaned_data.index if cleaned_data['Site Number'][x] == j][0]
            for c in cleaned_data.columns[3:]:
                if cleaned_data[c][wi] == 1 and cleaned_data[c][wj] == 1:
                    overlaps += 1
            if overlaps > 0: # Overlaps should be greater than 0 to make an edge
                net.add_edge(i,j,{'weight' : overlaps})
                # OR net.add_edge(i,j,weight = overlaps)

# Step 3: draw the network
nx.draw(net) # It's awful!

locations = nx.layout.spring_layout(net,weight='weight',scale = 5)
nx.draw_networkx(net,locations,labels=False)

def get_components(G):
    the_big_one = []
    for x in nx.components.connected_component_subgraphs(G):
        if len(x.node) > 1:
            the_big_one.append(x)
    return the_big_one

g = the_big_one[0]

locations = nx.layout.spring_layout(g,k = .5, weight='weight',scale = 5)
nx.draw_networkx(g,locations,labels=False)

h = g.copy()

for i in h.edge.keys():
    for j in h.edge[i].keys():
        if h.edge[i][j]['weight'] <= 1:
            h.remove_edge(i,j)
            
locations = nx.layout.spring_layout(h1,k = .4, weight='weight',scale = 5)
nx.draw_networkx(h1,locations,labels=False)

d = h1.degree()
nx.draw_networkx(h1,locations,labels=False,node_color = [d[x] for x in h1.nodes()])

c = nx.centrality.eigenvector.eigenvector_centrality(h1)
nx.draw_networkx(h1,locations,labels=False,node_color = [c[x] for x in h1.nodes()])

highest_center = [c[x] for x in h1.nodes()]
highest_center.sort()
highest_center[-5]

[x for x in h1.nodes() if c[x] > .17]

# Step 4: Run network metrics


# Step 5: Save data
cleaned_data.to_