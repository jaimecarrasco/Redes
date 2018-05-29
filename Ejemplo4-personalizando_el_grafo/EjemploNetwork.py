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
# Aqui personalizamos los nodos. Por defecto, node_size = 300, pero lo subimos a 1000 para que se
# se vea mas grande. Solo los nodos 'c' y 'g' son redibujados. con node_color podemos cambiar el color
# elegimo blue = 'b'
nx.draw_networkx_nodes(G, pos = pos_xy, node_size = 1000, nodelist=['c','g'], node_color='b')

plt.savefig('net.png')


plt.show()
