

from src.estado import Estado
from src.transicao import Transicao

class Afd:
    def __init__(self, nodes=[], edges=[], finals=[], symbols=[]):
        self.nodes = nodes
        self.edges = edges
        self.finals = finals
        self.symbols = symbols
        self.endLine = "*"

    # ultimo caractere de uma string aceita
    def setEndLine(self, endLine):
        self.endLine = endLine
    
    def add_node(self, name):
        node = Estado(name)
        self.nodes.append(node)

    def add_edge(self, source_name, target_name, weight):
        source = self.get_node_by_name(source_name)
        target = self.get_node_by_name(target_name)
        edge = Transicao(source, target, weight)
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

    # set node as final
    def set_final(self, name):
        node = self.get_node_by_name(name)
        node.setFinal()
        self.finals.append(node)

    def set_initial(self, name):
        node = self.get_node_by_name(name)
        node.setInitial()
        self.initial = node

    def visualize_graph(self):
        print("\n\nVisualization:")
        for edge in self.edges:
            source_name = edge.source.name
            target_name = edge.target.name
            weight = edge.weight
            print(f"{source_name} -- {weight} --> {target_name}")

    def check_transition(self, string):
        start_node = self.initial
        current_node = start_node
        path = [current_node.name]
        stringCheck = string + self.endLine
        print("\n\nChecando transições - Input: '" + string+"'")

        for char in stringCheck:
            valid_transition = False
            outgoing_edges = self.get_outgoing_edges(current_node)
            for edge in outgoing_edges:
                # se char esta dentro do array de pesos
                if char in edge.weight:
                    print(
                        f"Token: '{char}', transição: {edge.source.name} -- {edge.weight} --> {edge.target.name}")
                    valid_transition = True
                    current_node = edge.target
                    path.append(current_node.name)
                    break

            if not valid_transition:
                print(f"\nNão existe transição valida. Token '{char}', transição não encontrada para o estado {current_node.name}")
                print("")

                return []

        if not current_node.is_final:
            print("")
            print("")
            return []

        return path

