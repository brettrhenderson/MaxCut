'''
Problem: Solve the maximum cut problem on a graph.

Partition the vertices of a graph such that the number of edges connecting veritces
in different subsets is maximized.
'''

# 1. Import packages
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector as inspector

# 2. Define the problem
# Since we're working with un-directed graphs, we can represent a graph as a set of edges,
# which are just tuples of connected nodes. To start out, we implement the graph from the
# lecture slides. Be sure not to double-count edges.
graph = {('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'F'), ('C', 'D'), ('D', 'F'), ('D', 'E'), ('E', 'F')}

# We assign variables x_i for each vertex, where the meaning is that x_i = 0 means the vertext is assigned to
# set A and x_i = 1 means it is assigned to set B. From my derivation, the contribution of each edge between
# nodes 'X', and 'Y' to the objective function is 2x_X*x_Y - x_X - x_Y. Plugging in 1 or 0 for each of x_X and
# x_Y, we see that this contribution is -1 if the two values are different and 0 if they are the same. Thus,
# we solve our problem by minimizing Sum(2x_X*x_Y - x_X - x_Y) over all edges 'XY'. We don't need to add a constraint.
Q = {}
for edge in graph:
    Q[('x' + edge[0], 'x' + edge[1])] = 2  # edges are unique
    for i in [0, 1]:
        if ('x' + edge[i], 'x' + edge[i]) in Q:  # vertices will come up again and again
            Q[('x' + edge[i], 'x' + edge[i])] -= 1
        else:
            Q[('x' + edge[i], 'x' + edge[i])] = -1

# 3. Instantiate a solver
solver = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

# 4. Solve the problem
sampleset = solver.sample_qubo(Q, chain_strength=200,  num_reads=100)

# 5. Interpret results
inspector.show(sampleset)
print(sampleset)