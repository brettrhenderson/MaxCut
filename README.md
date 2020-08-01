# MaxCut
An solution of the Maximum Cut problem on a DWave quantum annealer.

One possible statement of the Max Cut problem would be: "Given an undirected graph, 
partition the vertices into two sets such that the number of edges joining 
vertices in different sets is maximized." You could think of it as wanting
to cut the edges between unlike vertices and also wanting to maximize the
 number of cuts.  

## Examples:
In this script, we set up the Max Cut problem to be solved on a DWave QPU using
the Ocean SDK. Two graphs are defined in the script, and you can toggle between
which problem you are solving by commenting/uncommenting the graph you want, 
or by defining your own. The first example is taken from the DWave Slides 
in the Introduction to Quantum Computing Models put on by TRIUMF in 
July - Aug 2020.

It solves for the following graph, and returns the solutions below it. Each
solution comes in a pair, where the colors are simply reversed, for a total
of 8 lowest energy solutions that contain 6 cuts.

<center>
 <img src="images/graph1.png", width=800 align="center">
<center>

I made another simple example just to show that the script can handle an
arbitrary input graph. The left-hand graph has two lowest-energy solutions
corresponding to the partitioning on the right.

<center>
 <img src="images/graph2.png", width=800 align="center">
<center>
 
## Defining a graph
Since our graphs are undirected, we can define them simply by creating a set
of the edges, written as tuples of the vertex names. For example, the second
graph above is defined as 

```python
graph = {('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D')}
```

The vertex names can be strings of any length.

## Solution format
The solutions are printed as a list of binary strings and associated scores.
A variable 'x<NODE>' corresponds to each node. A value of 0 means it is in
the first set of the partition, and the value 1 means it is in the second set.


## A note on Chain Strength
The chain_strength parameter when sampling the QUBO should be set to about the
same magnitude as the number of edges emanating from the most connected
vertex in the graph.  
