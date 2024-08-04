import networkx as nx
import matplotlib.pyplot as plt

def Graph_Creator(localCourselist,professorList):      #not sure if putting import statements outside the function header updates the value stored in inport statements when the function is called
    
    plt.figure(figsize=(50, 50))
    G = nx.Graph()
    print(G)

    pos = nx.circular_layout(G)

    for professor in professorList:
        professorID = professor.getID()
        G.add_node(professorID)

    for course in localCourselist:
        G.add_node(course.getCourseCode())
        for professor in course.profsTakingCourse:
            G.add_edge(professor.getID(), course.getCourseCode(),length=100)
    pos = nx.circular_layout(G)

    edge_labels={}
    for edge in G.edges():
        edge_priority=0
        for i in professorList:
            if str(i.getID())==edge[1]:
                for j in localCourselist:
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
        'node_color':'#0C1844',     # color of node
        'node_size': 9000,         # size of node
        'width': 6,                 # line width of edges  
        'edge_color':'#FF6969',     # edge color
        'font_color':'#FFFFFF',     # font color
        'font_size':18,             # font size 
    }
    nx.draw(G, pos, with_labels = True,**options)
    plt.savefig("Course_Assignment.png")
    plt.show()