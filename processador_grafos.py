from algoritmos import *
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
    graph_list = filter(lambda x: x.connected(), graph_list)

    print("Processando "+str(len(graph_list))+" grafos validos")
    print("")

    qtd_rotulos = 0.0
    contador_tempo = 0.0



    for graph in graph_list:
        processar = compose_process(algoritmo,heuristica,graph)
        inicio = time.clock()
        resultado = processar()
        fim = time.clock()
        
        tempo = fim - inicio
        contador_tempo += tempo
        n_rotulos = resultado[2].n_label
        qtd_rotulos += n_rotulos
        print("Ticks: %d" % resultado[0] )
        print("Numero de nos expandidos: %d" %resultado[1])
        print("Quantidade de Rotulos: " + str(n_rotulos))
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
