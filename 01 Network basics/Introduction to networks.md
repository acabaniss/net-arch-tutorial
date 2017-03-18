# Introduction to Networks

Networks are representations of systems 

## Terms
There are many different ways of describing networks in the social sciences, largely dependent on when and from where networks entered the field. 

* Network (graph) - A relational entity, or topology, that describes the connections between parts.

* Node (vertex) - These are the entities connected by a network. Nodes can have their own attributes, e.g. names of cities or geographic coordinates.

* Edge (link) - These are the entities that connect nodes. Edges can be __weighted__ or __unweighted__, i.e. they can have a numberical value that determines how strong or weak the connection is. Edges can also be __directed__ or __undirected__. Directed edges have a source and a destination: Athens may trade pots with Knossos, but Knossos might not trade pots with Athens. Undirected edges do not have an orientation: the ceramic assemblages of Athens and Knossos may be similar by some metric regardless of whether you compare Athens with Knossos or Knossos with Athens.

* Neighborhood/neighbors - the nodes connected to a given node.

* Triangle - Any three nodes connected to each other.
 
* Clique - Any N nodes where all N nodes are connected to their N-1 neighbors.

* Community - A group of nodes more connected to each other than to other nodes. There are many ways to define and describe communities; this process is called __community detection__.

* Component - A set of nodes where every node is reachable from every other node. A network may include multiple components.

In a lot of archaeological applications, nodes are sites, locations, or people, although they could also be objects. Edges are often describing connections between these locations (distances, similarity in ceramic consumption, membership in a common league) but they may also describe flows (trade, money, people).

## Representations

There are many structures one can use to represent a network. Two of the most common ones are adjacency lists and adjacency matrices.

* Adjacency list - provides the connections between nodes in list format. E.g. {A,B,1; B,C,1} might describe a network with three nodes (A, B, and C) and two edges (connecting A to B and B to C).

* Adjacency matrix - provides the connections between nodes in the form of a matrix. All possible connections are indicated, often with a 1 for presence and a 0 for absence. E.g.:

| |A|B|C|
|--|--|--|--|
|A|-|1|0|
|B|1|-|1|
|C|0|1|-|

describes the same network as the list previously.

## Layouts

Visualizing networks remains a key step of network analysis. Nodes may have spatial coordinates or require a layout algorithm.

* Random layouts - shuffling nodes in spaces. Often produces cluttered graphs, but can be useful for initializing.

* Spring layouts - the most common algorithms involve assuming that links function as springs; parts of the network that are tightly connected are pulled together and drawn into the same part of the plot. Common parameters include the spring strength, the amount of time allowed to pass, and the weight of each edge.

* Spectral layouts - these are complicated, but essentially spectral layouts take some of the centrality measures (discussed below, but in particular the eigenvector centrality measure) and use them to plot the nodes of a network.

## Measures

* Degree - The number of neighbors a node has. Lots of networks are described by their _degree distribution__, or by the number of nodes that have a given degree in the network.

* Shortest path distance - The distance a given node is from another in terms of edges. Sometimes, this takes into account the weights of edges (e.g. if a weight encodes a geographic distance or a travel time.) 

* Diameter - The longest shortest path between two points. Think of this as the maximum distance any node ever has to travel to reach another nodes.

* Centrality - The importance of a node. There are many ways of identifying importance, which means there are many ways of thinking about centrality. Identifying the correct measure requires careful thought about the nature of your data and the mechanisms underlying the phenomena of interest. Some possible centrality measures include:

  * Degree centrality - importance means more neighbors. The most important city politically might be Athens because they have the most alliances with other poleis.

  * Betweenness centrality - importance means that an agent/goods/information has to go through a node to get to other nodes. E.g. the most important node on a network of trade routes may be Byzantium because of its role overlooking the Hellespont, not because it produces or consumes more than others.

  * Closeness centrality - importance means ease of access. E.g. Delos may be the most important island because it is most central to other relevant inhabited areas.

  * Eigenvector centrality - importance means that a node is connected to other important nodes. E.g. Melos may be important not because it has connections to the other major trading centers of the Mesolithic Aegean.

* Clustering coefficient- how tightly connected nodes are to each other; alternatively, how many of a nodes neighbors are connected to each other. This is measured as the number of triangles in a given node's neighborhood. The __average clustering coefficient__ of a network is the average of this across all nodes and describes how closely connected nodes are within the entire network.

## Optional: types of graphs

If you want to start testing your results and methods you will quickly need to start thinking about probability and sampling. This will include thinking about generating networks following different processes, and it may be helpful for understanding the meaning of your results to be familiar with several types of random networks.

* Random (Erdos-Renyi graph) - Take N nodes; for every possible edge, there is a _p_ probabilty that an edge connects them.

* Ring - Take N nodes; every N node is connected to 2 others to form a ring.

* Small world (Watts-Strogatz graph) - Take N nodes and connect them to M other nodes to form a ring. With probability p, rewire a given edge to a random node. Small rewiring probabilities lead to the ''small world'' effect, whereby the diameter of the network radically decreases but the average clustering coefficient remains high.

* Preferential attachment (Barabasi-Albert; Scale-free) - Take 1 node. Add one node at a time, each time connecting it to M existing nodes in the network. This results in some (the oldest) nodes having the most neighbors and thus the highest degree, while most nodes have only M edges. This leads to a power-law or scale-free distribution, which implies that these properties will hold as the network continues to grow.


## Resources

Mark Newman's standard textbook _Networks: an introduction_ has concrete examples of many types of networks and serves as a mathematical but accessible introduction to network theory from the mathematical perspective.
