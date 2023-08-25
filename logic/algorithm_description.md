# Angklung Allocation Algorithm
Version 1.0.0<br>
Last updated 26 August 2023 by Jason Christopher

Main Reference: <br>
Salindeho, B. M., &amp; Baskoro, E. T. (2019). Graph coloring for determining angklung distribution. 
Journal of Physics: Conference Series, 1277(1), 012033. https://doi.org/10.1088/1742-6596/1277/1/012033 

## Algorithm Overview

Based on the paper by Salindeho and Baskoro (2019), the allocation of angklungs in a piece music can be modelled as a k-coloring problem on a graph. Each node represents a musical note, and an edge connecting notes u and v represents a clash between notes u and v. This clash exists if u and v are within the same beat interval.

The algorithm proceeds to find:
- The minimum number of colours required to allocate the angklungs (`min_num`)
- The recommended allocation of angklungs given a specified number of people (`n`), where `n > min_num`

## Graph Modelling

The problem can now be modelled as an unweighted, undirected graph, whose nodes are the musical notes, and edges represent an overlap in the musical notes.

Since we are dealing with dense graphs (small num of notes but potentially large number of edges), hence an adjacency matrix is preferred over an adjacency list. This ensures an O(1) access time when checking for neighbours, and O(V) time to loop through all neighbours instead of O(E) time, given that E might be much greater than V.

## Minimum Number of Colours Required

Finding the minimum number of colours is considered a graph coloring problem, and is an NP-hard in general. Hence in this case, where optimisation is not a huge consideration, version 1.0.0 will implement a more heuristic-based greedy approximation approach. In particular, the **Welsh-Powell algorithm**  will be used.

The Welsh Powell Algoirthm is considered an iterative greedy approach to the graph coloring problem. The algorithm consists of the following steps:

1. Find the degree of each vertex
2. List the vertices in the order of descending degrees
3. Colour the first vertex with color 1.
4. Move down the list and color all the vertices not connected to the coloured vertex, with the same color.
5. Repeat step 4 on all uncolored vertices with a new color, in descending order of degrees until all the vertices are colored.

By starting with the highest degree, we make sure that the vertex with the highest number of conflicts can be taken care of as early as possible.

Reference:<br>
https://www.geeksforgeeks.org/welsh-powell-graph-colouring-algorithm/

## Load balancing algorithm?

(TBA)