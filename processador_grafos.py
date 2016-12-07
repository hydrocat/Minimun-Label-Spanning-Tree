from algoritmos import *
from connected_component import *
from graph_importer import *
from heuristicas import *
from graph import *
import time
import os

def compose_process(algoritmo, heuristica, grafo):
    def process_no_h():
        return algoritmo(grafo)

    def process_with_h():
        return algoritmo(heuristica,grafo)

    if heuristica == None:
        return process_no_h
    else:
        return process_with_h

def processar_grafos(algoritmo,heuristica, arquivo_de_entrada, diretorio_de_entrada):
    if diretorio_de_entrada == None:
        processa_arquivo(algoritmo,heuristica,arquivo_de_entrada)
    else:
        processa_diretorio(algoritmo,heuristica,diretorio_de_entrada)
        
def processa_arquivo(algoritmo,heuristica,arquivo_de_entrada):
    print("Processando " + arquivo_de_entrada)
    graph_importer = Graph_importer(arquivo_de_entrada)
    graph_list = list(graph_importer.graphs())
    #graph_list = filter(lambda x: x.connected(), graph_list)

    print("Processando "+str(len(graph_list))+" grafos validos")
    print("")

    qtd_rotulos = 0.0
    contador_tempo = 0.0

    


    for graph in graph_list:
        #processar = compose_process(algoritmo,heuristica,graph)
        processar = connectedd
        inicio = time.clock()
        resultado = processar(graph)
        fim = time.clock()
        
        tempo = fim - inicio
        contador_tempo += tempo
        qtd_rotulos += resultado[0]
        #n_rotulos = 1
        print("Quantidade de Rotulos: {}".format(resultado[0]))
        print("Tempo de Execucao: %0.3fs" % tempo)

    print("Quantidade media de rotulos por grafo: " +
          str(qtd_rotulos/len(graph_list)))
    print("Tempo medio de processamento: " +
          str(contador_tempo/len(graph_list)) +"s")
    print("")
    
def processa_diretorio(algoritmo,heuristica,diretorio_de_entrada):
    arquivos = os.listdir(diretorio_de_entrada)
    for a in arquivos:
        processa_arquivo(algoritmo,heuristica,diretorio_de_entrada+a)
