from Course_Input import *
from Professor_Input import *
import networkx as nx

G = nx.Graph()
print(G)

pos = nx.spring_layout(G)

for course in courselist:
    G.add_node(course)
    

for professor in professorList:
    G.add_node(professor)
    for i in range(1,6):
        if professor.getFDCDCPriority(i)!='nan':
            G.add_edge(professor,professor.getFDCDCPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor,professor.getHDCDCPriority(i)): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,6):
        if professor.getHDCDCPriority(i)!='nan':
            G.add_edge(professor,professor.getHDCDCPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor,professor.getHDCDCPriority(i)): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,4):
        if professor.getFDELCPriority(i)!='nan':
            G.add_edge(professor,professor.getFDELCPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor,professor.getFDELCPriority(i)): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,4):
        if professor.getHDELCPriority(i)!='nan':
            G.add_edge(professor,professor.getHDELCPriority(i))
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor,professor.getHDELCPriority(i)): 'Priority: ' + str(i)},
                font_color='red'
            )

nx.draw(G, with_labels = True)       