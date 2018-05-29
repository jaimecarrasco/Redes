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
pos_xy['a'] = np.array([1, 1])   # posicion del nodo 'a'
pos_xy['b'] = np.array([2, 1.2]) # posicion del nodo 'b'
pos_xy['c'] = np.array([1.5, 2]) # posicion del nodo 'c'
pos_xy['h'] = np.array([4, 1])   # posicion del nodo 'h'
pos_xy['f'] = np.array([3, 2])   # posicion del nodo 'f'
pos_xy['g'] = np.array([5, 1.5]) # posicion del nodo 'g'

# Dibujamos ahora pasandole a draw, las posiciones definidas en el diccionario pos_xy
nx.draw_networkx(G, pos = pos_xy, arrows = True, with_labels = True)
plt.title('Grafo dirigido con posiciones fijas')
plt.savefig('digraph.png')
plt.show()
