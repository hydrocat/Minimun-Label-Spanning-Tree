import sys
import collections
from tabuleiro import *
from fila import *
try:
	from queue import Queue
except ImportError:
	from Queue import Queue

"""
Retorna a quantidade de ticks, o parentesco, os locais por onde passou
e o ultimo no
"""

def busca_estrela( heuristica, grafo ):
	candidatos = PriorityQueue()
	candidatos.put((heuristica(grafo), grafo), 0)
	pai = {}
	pai[(heuristica(grafo), grafo)] = [None, 0]
	passados = {}
	passados[(heuristica(grafo), grafo)] = 0

	no_final = None
#	estado_final = (heuristica(Grafo()),Grafo())

	tick = 0
	while not candidatos.empty():
                #pega o melhor candidato
		candidato = candidatos.get()
                
		#gera os novos candidatos
		novos_candidatos = [(heuristica(filho), filho) for filho in candidato[1].filhos()]

                #o grafo gerou filhos ?
                if len(novos_candidatos) == 0:
                        no_final = candidato
                        break
                
		for novo_candidato in novos_candidatos:
			novo_custo = pai[candidato][1] + novo_candidato[0]
			if novo_candidato not in passados:
				passados[novo_candidato] = novo_custo
				prioridade = passados[novo_candidato]
				candidatos.put(novo_candidato, prioridade)
				pai[novo_candidato] = [candidato, pai[candidato][1] + 1]

		tick += 1

	return tick, len(passados), no_final[1]


"""
Retorna a quantidade de iteracoes usadas para terminar
"""
def busca_gulosa( heuristica, grafo ):
	#estado_final = (heuristica(Grafo()),Grafo())
	pai = {}
	pai[(heuristica(grafo), grafo)] = [None, 0]
	candidatos = [ (heuristica(grafo), grafo) ]
	encontrou = False
	passados = []
	tick = 0

	no_final = None

	while encontrou == False:
		candidatos.sort(key= lambda x: x[0], reverse=True)
		tick += 1
		candidato = candidatos.pop()
		passados.append(candidato)
                novos_candidatos = [ (heuristica(filho), filho) for filho in candidato[1].filhos() ]
                
                if len(novos_candidatos) == 0:
                        no_final = candidato
                        encontrou = True
                        break
                        
                for c in novos_candidatos:
                        if c not in passados and c != candidato:
                                candidatos.append(c)
                                pai[c] = [candidato, pai[candidato][1] + 1]
                                
	return tick, len(passados), no_final[1]

def busca_largura( grafo ):
	candidatos = Queue()
	candidatos.put(grafo)
	passados = {}
	passados[grafo] = [None, 0]

	no_final = None
	#estado_final = Grafo()

	tick = 0
	while not candidatos.empty():
		candidato = candidatos.get()

		novos_candidatos = [ filho for filho in candidato.filhos()]
                if len(novos_candidatos) == 0:
                        no_final = candidato
                        break

		for novo_candidato in novos_candidatos:
			if novo_candidato not in passados:
				candidatos.put(novo_candidato)
				passados[novo_candidato] = [candidato, passados[candidato][1] + 1]

		tick += 1

	return tick, len(passados), no_final

def busca_profundidade( grafo ):
	candidatos = []
	candidatos.append(grafo)
	passados = {}
	passados[grafo] = [None, 0]

	encontrou = False

	no_final = None
	#estado_final = Grafo()

	tick = 0
	while not encontrou:
		candidato = candidatos.pop()
		novos_candidatos = [ filho for filho in candidato.filhos()]
                if len(novos_candidatos) == 0:
                        encontrou = True
                        no_final = candidato
                        break
		for novo_candidato in novos_candidatos:
			if novo_candidato not in passados:
				candidatos.append(novo_candidato)
				passados[novo_candidato] = [candidato, passados[candidato][1] + 1]

		tick += 1

	return tick, len(passados), no_final
