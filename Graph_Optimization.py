from Course_Input import *
from Professor_Input import *
import networkx as nx

G = nx.Graph()
print(G)

for course in courselist:
    G.add_node(course.getCourseCode())

for professor in professorList:
    G.add_node(professor.getID())
    for i in range(16):
        if i!=None:
            G.add_edge(professor.getName(),professor.getPriority(i))

nx.draw(G, with_labels = True)