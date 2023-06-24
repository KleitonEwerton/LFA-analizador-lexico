import json
from sys import argv
from src.afd import Afd

def main():
    graph = Afd()

    #verifica se o arquivo foi passado como argumento e se é um arquivo JSON
    if len(argv) != 3 or not argv[1].endswith('.json') or not argv[2].endswith('.json'):
        print("Error: argumento invalido. \nModo de uso: python3 main.py <definicao.json> <strings.json>")
        return

    # Abre o arquivo JSON que
    with open(argv[1]) as arquivo:
        dados = json.load(arquivo)
           
    # abre o arquivo json qe contem strings a serem testadas, e as armazena em uma lista argv[2]
    with open(argv[2]) as arquivo:
        strings = json.load(arquivo)
    
    # Obtém as transições do arquivo JSON
    transicoes = dados['transition']

    # Itera sobre as chaves das transições e obtém as informações desejadas
    for estado, transicao in transicoes.items():
        for t in transicao:
            to = t['to']
            read = t['read']
            graph.add_node(estado)
            graph.add_node(to)
            graph.add_edge(estado, to, read)

    graph.set_initial(dados['initial'])
    graph.setEndLine(dados['endLine'])
    final = dados['final']
    for f in final:
        graph.set_final(f)

    graph.visualize_graph()

    for string in strings:
        print(f"\n\n--------------------------------------------------------------\n\n")
        path = graph.check_transition(strings[string])
        if path:
            print(f"\n\nAccepted - Transições: {path}")
        else:
            print("\nRejected")
            
        
if __name__ == "__main__":
    main()
