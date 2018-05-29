import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

H = nx.read_edgelist(path = 'data_grafo.txt', create_using = nx.DiGraph() , nodetype = str, data = (('weight', float),))

nx.draw_networkx(H, arrows = True, with_labels = True)
# Podemos guardar la imagen del grafo con:
plt.savefig('digraph.png')
# Podemos darle un titulo al grafico
plt.title('Grafo dirigido, con pesos')
plt.show()


