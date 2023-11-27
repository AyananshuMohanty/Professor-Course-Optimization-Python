from Course_Input import *
from Professor_Input import *
import networkx as nx

G = nx.Graph()
print(G)

for course in courselist:
    G.add_node(course)
    
pos = nx.spring_layout(G)

for professor in professorList:
    G.add_node(professor)
    for i in range(16):
        if professor.getPriority(i)!='nan':
            G.add_edge(professor,professor.getPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor,professor.getPriority(i)): 'Priority: ' + str(i)},
                font_color='red'
            )

nx.draw(G, with_labels = True)


