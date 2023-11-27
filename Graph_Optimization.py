from Course_Input import *
from Professor_Input import *
import networkx as nx

G = nx.Graph()
print(G)

pos = nx.spring_layout(G)

for course in courselist:
    G.add_node(course.getName())
    

for professor in professorList:
    G.add_node(professor.getName())
    for i in range(1,6):
        if professor.getFDCDCPriority(i)!='nan':
            G.add_edge(professor.getName(),professor.getFDCDCPriority(i).getName())
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor.getName(),professor.getFDCDCPriority(i).getName()): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,6):
        if professor.getHDCDCPriority(i)!='nan':
            G.add_edge(professor.getName(),professor.getHDCDCPriority(i).getName())
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor.getName(),professor.getHDCDCPriority(i).getName()): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,4):
        if professor.getFDELCPriority(i)!='nan':
            G.add_edge(professor.getName(),professor.getFDELCPriority(i).getName())
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor.getName(),professor.getFDELCPriority(i).getName()): 'Priority: ' + str(i)},
                font_color='red'
            )
    for i in range(1,4):
        if professor.getHDELCPriority(i)!='nan':
            G.add_edge(professor.getName(),professor.getHDELCPriority(i).getName())
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels={(professor.getName(),professor.getHDELCPriority(i).getName()): 'Priority: ' + str(i)},
                font_color='red'
            )

nx.draw(G, with_labels = True)       