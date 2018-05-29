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


print "Los nodos son: ", G.nodes
print "Las aristas son (no muestra la info de los pesos): ", G.edges
print "Las aristas con info de los atributos (pesos, etc): ", G.edges(data=True)
print "Numero de nodos del grafo: ", G.number_of_nodes()
print "Numero de aristas del grafo: ", G.number_of_edges()

print "Grado en funcion del numero de aristas adyacentes al nodo: "
print "Grado de entrada del nodo 'a': ", G.in_degree('a')
print "Grado de salida del nodo 'a': ", G.out_degree('a')

print "Grado en funcion del numero de aristas adyacentes al nodo: "
print "Grado de entrada en funcion de los pesos: ", G.in_degree('a', weight = 'weight')
print "Grado de entrada en funcion de los pesos: ", G.out_degree('a', weight = 'weight')

print "Lista de aristas que entran al nodo 'a': ", list(G.in_edges('a'))
print "Lista de aristas que salen del nodo 'a': ", [('a', x) for x in G['a']]

nx.draw_networkx(G,arrows=True, with_labels=True)
plt.title('Grafo dirigido, con pesos')
plt.show()




