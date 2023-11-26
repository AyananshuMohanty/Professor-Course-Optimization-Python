from Course_Input import *
from Professor_Input import *
import networkx as nx

G = nx.DiGraph(directed=True)
print(G)

for course in courselist:
    G.add_node(course.getCourseCode())
    
pos = nx.circular_layout(G)

for professor in professorList:
    G.add_node(professor.getID())
    for i in range(16):
        if i!=None:
            G.add_edge(professor.getName(),professor.getPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor.getName(),professor.getPriority(i)): 'Priority: ' + i},
                font_color='red'
            )

nx.draw(G, with_labels = True)


