from Course_Input import *
from Professor_Input import *
import networkx as nx
import matplotlib.pyplot as plt
plt.figure(figsize=(100, 100))
G = nx.Graph()
print(G)

pos = nx.circular_layout(G)

for course in courseList:
    G.add_node(course.getCourseCode())

for professor in professorList:
    professorID = professor.getID()
    G.add_node(professorID)

    for i in range(1, len(professor.Priority_Order_FDCDC) + 1):
        courseCode = professor.getFDCDCPriority(i).getCourseCode()
        if professor.getFDCDCPriority(i) != 'nan':
            G.add_edge(professorID, courseCode,length=100)

    for i in range(1, len(professor.Priority_Order_HDCDC) + 1):
        courseCode = professor.getHDCDCPriority(i).getCourseCode()
        if professor.getHDCDCPriority(i) != 'nan':
            G.add_edge(professorID, courseCode,length=100)

    for i in range(1, len(professor.Priority_Order_FDELC) + 1):
        courseCode = professor.getFDELCPriority(i).getCourseCode()
        if professor.getFDELCPriority(i) != 'nan':
            G.add_edge(professorID, courseCode,length=100)

    for i in range(1, len(professor.Priority_Order_HDELC) + 1):
        courseCode = professor.getHDELCPriority(i).getCourseCode()
        if professor.getHDELCPriority(i) != 'nan':
            G.add_edge(professorID, courseCode,length=100)

pos = nx.circular_layout(G)

edge_labels={}
for edge in G.edges():
    edge_priority=0
    for i in professorList:
        if str(i.getID())==edge[1]:
            for j in courseList:
                if str(j.getCourseCode())==edge[0]:
                    for key,value in i.Priority_Order_FDCDC.items():
                        if j == value:
                            edge_priority=key
                            edge_labels[edge]= 'Priority: ' + str(edge_priority)
                    for key,value in i.Priority_Order_HDCDC.items():
                        if j == value:
                            edge_priority=key
                            edge_labels[edge]= 'Priority: ' + str(edge_priority)
                    for key,value in i.Priority_Order_FDELC.items():
                        if j == value:
                            edge_priority=key
                            edge_labels[edge]= 'Priority: ' + str(edge_priority)
                    for key,value in i.Priority_Order_HDELC.items():
                        if j == value:
                            edge_priority=key
                            edge_labels[edge]= 'Priority: ' + str(edge_priority)
        
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_color='red'
)
options = {
    'node_color': 'teal',     # color of node
    'node_size': 4500,          # size of node
    'width': 1,                 # line width of edges  
    'edge_color':'black',        # edge color
}
nx.draw(G, pos, with_labels = True,**options)
plt.savefig("Graph.png")
plt.show()