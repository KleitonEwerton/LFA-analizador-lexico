from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 
from matplotlib.path import Path


class Node:
    def __init__(self, name):
        self.name = name

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, name):
        node = Node(name)
        self.nodes.append(node)

    def add_edge(self, source_name, target_name, weight):
        source = self.get_node_by_name(source_name)
        target = self.get_node_by_name(target_name)
        edge = Edge(source, target, weight)
        self.edges.append(edge)

    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

    def get_outgoing_edges(self, node):
        outgoing_edges = []
        for edge in self.edges:
            if edge.source == node:
                outgoing_edges.append(edge)
        return outgoing_edges

    def visualize_graph(self):
        print("Graph visualization:")
        for edge in self.edges:
            source_name = edge.source.name
            target_name = edge.target.name
            weight = edge.weight
            print(f"{source_name} -- {weight} --> {target_name}")

    def visualize_graph_plot(self):
        G = nx.DiGraph()

        # Adicionar nós ao grafo
        for node in self.nodes:
            G.add_node(node.name)

        # Adicionar arestas ao grafo
        for edge in self.edges:
            source_name = edge.source.name
            target_name = edge.target.name
            weight = edge.weight
            G.add_edge(source_name, target_name, weight=weight)

        # Definir layout circular do grafo
        pos = nx.circular_layout(G)

        # Desenhar nós
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

        # Desenhar arestas com setas
        labels = nx.get_edge_attributes(G, 'weight')
        edges = nx.draw_networkx_edges(G, pos, edge_color='gray', arrowstyle='->', arrowsize=15, connectionstyle='arc3,rad=0.2')
       
         # Ajustar posição dos rótulos das arestas
        for (_, label), edge in zip(labels.items(), G.edges()):
            x_start, y_start = pos[edge[0]]
            x_end, y_end = pos[edge[1]]

            # Calcular posição exata no meio da curva da aresta
            x_interpolated = np.interp(0.5, [0, 1], [x_start, x_end])
            y_interpolated = np.interp(0.5, [0, 1], [y_start, y_end])
            curve_midpoint = (x_interpolated, y_interpolated)

            x = curve_midpoint[0]
            y = curve_midpoint[1]

            plt.text(x, y, label[0], fontsize=10, ha='center', va='center')

        # Desenhar rótulos dos nós
        nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

        plt.axis('off')
        plt.show()
        
    def check_transition(self, string):
        start_node = self.nodes[0]
        current_node = start_node
        path = [current_node.name]

        for char in string:
            valid_transition = False
            outgoing_edges = self.get_outgoing_edges(current_node)
            for edge in outgoing_edges:
                if edge.weight == char:
                    print(f"{edge.source.name} -- {edge.weight} --> {edge.target.name}")
                    valid_transition = True
                    current_node = edge.target
                    path.append(current_node.name)
                    break
            if not valid_transition:
                return []

        if current_node != self.nodes[-1]:
            return []

        return path



def main():
    graph = Graph()
    graph.add_node("q0")
    graph.add_node("q1")
    graph.add_node("q2")
    graph.add_node("q3")
    graph.add_edge("q0", "q1", "a")
    graph.add_edge("q1", "q2", "b")
    graph.add_edge("q2", "q3", "a")
    graph.add_edge("q3", "q2", "b")

    # graph.visualize_graph()

    string = "ababa"
    path = graph.check_transition(string)
    if len(path) == len(string) + 1:
        print(f"Accepted: {path}")
    else:
        print("Rejected")
    graph.visualize_graph_plot()
    
if __name__ == "__main__":
    main()
