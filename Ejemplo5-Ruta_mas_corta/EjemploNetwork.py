import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



G = nx.DiGraph()

aristas = [('a', 'b', 5), ('a', 'c', 6), ('a', 'g', 17),
           ('b', 'a', 3), ('b', 'c', 4), ('b', 'h', 7),
           ('c', 'f', 6), ('c', 'h', 11),
           ('f', 'c', 7), ('f', 'g', 9), ('f', 'h', 4), ('f', 'a', 11),
           ('g', 'h', 5),
           ('h', 'g', 4), ('h', 'f', 9), ('h', 'a', 11),
           ]
G.add_weighted_edges_from(aristas)
pos_xy = dict()
pos_xy['a'] = np.array([1, 1])
pos_xy['b'] = np.array([2, 1.2])
pos_xy['c'] = np.array([1.5, 2])
pos_xy['h'] = np.array([4, 1])
pos_xy['f'] = np.array([3, 2])
pos_xy['g'] = np.array([5, 1.5])

nx.draw_networkx(G, pos = pos_xy, arrows = True, with_labels = True)


nodes_ruta = nx.shortest_path(G, source = 'c', target = 'g', weight = 'weight')
print 'Los nodos de la ruta mas corta es: ', nodes_ruta
largo_ruta = nx.shortest_path_length(G, source='c', target='g', weight='weight')
print 'El largo de la ruta mas corta: ', largo_ruta
# podriamos pintar los nodos de la ruta mas corta:
nx.draw_networkx_nodes(G, pos = pos_xy, nodelist = nodes_ruta, node_color='b')

# podriamos pintar las aristas de la ruta mas corta:
aristas_ruta = [(nodes_ruta[i], nodes_ruta[i+1]) for i in range(len(nodes_ruta)-1)]
nx.draw_networkx_edges(G, pos = pos_xy, width=2.0, edge_color='b', edgelist= aristas_ruta)
plt.title('Ruta mas corta')
plt.savefig('net.png')
plt.show()