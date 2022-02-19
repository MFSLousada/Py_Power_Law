_author__ = 'user'

from s2g import ShapeGraph
import networkx as nx

sg = ShapeGraph(shapefile='C:\Users\Maura Lousada\Desktop\ teste_grafo.shp', to_graph=True)
assert isinstance(sg.graph, nx.Graph)