import networkx as nx
import matplotlib.pyplot as plt

def Graph_Creator(courselist,professorList):      #not sure if putting import statements outside the function header updates the value stored in inport statements when the function is called
    
    plt.figure(figsize=(100, 100))
    G = nx.Graph()
    print(G)

    pos = nx.circular_layout(G)

    for professor in professorList:
        professorID = professor.getID()
        G.add_node(professorID)

    for course in courselist:
        G.add_node(course.getCourseCode())
        for professor in course.profsTakingCourse:
            G.add_edge(professor.getID(), course.getCourseCode(),length=100)
    pos = nx.circular_layout(G)

    edge_labels={}
    for edge in G.edges():
        edge_priority=0
        for i in professorList:
            if str(i.getID())==edge[1]:
                for j in courselist:
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
    plt.savefig("Course_Assignment.png")
    plt.show()