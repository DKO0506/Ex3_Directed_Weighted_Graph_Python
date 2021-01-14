# Directed & Weighted Graph Data Structure 
**Authors: David Kokiashvili & Omer Shalom**


## Introduction

**This repository is part of OOP exercises, in which the task is to implement a Directed Weighted Graph Data Structure in python programming language.**

**Click [Here](https://github.com/DKO0506/Ex3_Directed_Weighted_Graph_Python/archive/master.zip) to download this project.**

**More information regarding the project will be listed below.**






***


## Definition
** A graph is an ordered pair G = (V,E) where:**
-   **V is a set of vertices (nodes) of the graph**
-  **E is a set of the directed and weighted edges (arcs) of the graph**

![s](https://upload.wikimedia.org/wikipedia/commons/b/bc/CPT-Graphs-directed-weighted-ex1.svg)






***
  # Project Description
  
 **Package: src**


Class   |  Interface
---------- |  -------------------
Digraph    |  GraphInterface
GraphAlgo  | GraphAlgoInterface





- Digraph implements the GraphInterface methods and its characteristics.

- GraphAlgo implements the GraphAlgoInterface methods and its characteristics.


***
## Digraph 

**This class represents an implementation of Directed Weighted Graph in python.**

**There are several methods which describe the data structure applications.** 
  

**Method**   | Parameters |    **Description**
--------- | ---------------------| -------------------
**add_node** | **node_id**     | **Adds a node to the graph using the node_id as an integer variable**
**add_edge** | **id1,id2,weight** | Adds an edge from **id1** to **id2** with a given **weight** . **If such edge already exists then the method simply does nothing**
**remove_node**| **node_id** | Removes a node with a spesific **id** (**node_id**) **from the graph**.  If the operation was successfull then the function will return a boolean value **True**, otherwise **False** . 
**remove_edge** |  **id1,id2** | Removes an edge between **(id1,id2)** , if the mentioned edge doesn't exist then the function will do nothing.
**get_all_v** |                | Returns a dictionary of all the nodes in the Graph, each node is represented using a pair **(node_id, node_data)**
**all_in_edges_of_node** | **id1** |   Returns a dictionary of all the nodes connected to (into) node_id, each node is represented using a pair **(node_id, weight)**
**all_out_edges_of_node** | **id1** | Returns a dictionary of all the nodes connected from (into) node_id, each node is represented using a pair **(node_id, weight)**
**v_size** |                            | Returns the **number of vertices** in this graph
**e_size** |                             |Returns the **number of edges** in this graph
**get_mc** |                                |   Returns the **number of changes** that have been made in the graph 


                              
                              
                              
                            
***

## GraphAlgo 

**GraphAlgo** class implements the **GraphAlgoInterface** interface. This class uses the **Digraph** data structure to implement a number of key algorithms related to **Directed & Weighted Graphs**, such as: **Finding the shortest path between every pair of nodes in the graph** or **Check whether a given graph is Strongly Connected or Not**.

***


**The description** of the algorithms will be listed below, **Stay Tuned** 



***

### GraphAlgo Functions Description:

- **get_graph** - This method simply returns the **Directed Graph** on which the **algorithms** are implemented on .

- **load_from_json** - This method loads a **graph** from a json file.

- **save_to_json** - This method saves our data as a **JSON file** .

***

### Dijkstra's Shortest path algorithm

**Dijkstra’s algorithm finds a shortest path tree from a single source node, by building a set of nodes that have minimum distance from the source.**

**The graph has the following:**

- **vertices** denoted in the algorithm by **id1** and **id2** .

- **weighted edges** that connect two nodes: **(id1,id2)** denotes an edge, and 
**w(id1,id2)** denotes it's weight. In the diagram below, the weight for each edge is written in gray.

***
![g](https://user-images.githubusercontent.com/73295803/104609269-8a8ef680-568b-11eb-97fc-6fc99a30349d.png)

***




**This is done by initializing three values:**

- **distances**, a list of distances from source node **s** to each node in the graph, initialized  the following way: **distance(s)=0.**   for all other nodes **v**, **distance(v)=∞.** This is done at the beginning because as the algorithm proceeds, the distance from the source to each node v in the graph will be recalculated and finalized when the shortest distance to v is found.

- **Q**, a queue of all node in the graph. At the end of the algorithm's progress, **Q** will be empty.

- **S**, an empty **set**, to indicate which nodes the algorithm has visited.


***
**The algorithm proceeds as follows:**

- While **Q** is not empty, pop the node **v**, that is not already in **S**, from **Q** with the smallest **distance(v)**.  In the first run the source node **s** will be chose because **distance(v)** was initialized to **0**. In the next run, the next node with the smallest **distance value**  is chosen .

- Add node **v** to **S**, to indicate that **v** has been visited

- Update **distance** values of adjacent nodes of the current node v as follows: **for each new adjacent node u:**
    - if **distance(v) + weight(u,v) < distance(u)** , there is a new minimal distance found for **u**, so update **distance(u)** to the new minimal distance value .
    - **otherwise**, no updates are made do **distance(u).**
    
    

***


## Tarjan's Algorithm for Strongly Connected Components

- Set both v.index, v.low to a global variable “t”.

- ++t

- Push v into the stack **S**. 

- Traverse every vertex directly reachable from v.
    - If vertex w is unvisited, run Tarjan(w). Then set v.low = min{v.low, w.low}. 
    
    - If vertex w is visited, v.low = min{v.low, w.low}

- After the loop above, we can get the index of the oldest ancestor reachable from v (a.k.a. v.low). 

- If (v.low == v.index), v is the root of the SCC. 

- Pop the items in stack out until v is popped out. 

- Those vertices compose a SCC. 

***

### plot_graph method

**This method plots the graph, if the nodes have a position, then they will be placed there**.

** Otherwise the nodes will be given random positions**.
    

    

    
