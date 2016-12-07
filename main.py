#!/usr/bin/env python2
import sys
import getopt
import os
from algoritmos import *
from heuristicas import *
from processador_grafos import *

def usage():
	print("\nUso:")
	print("\tpython main.py -a ALGORITMO -h HEURISTICA -f arquivo_de_entrada -d diretorio_de_entrada")
        print("### Parametros ###")
	print(" -h Heuristica: qtd_rotulos")
        print(" -a Algoritmo:  estrela|guloso|largura|profundidade")
        print(" -f arquivo de entrada (File)")
        print(" -d Diretorio de entrada")


def main():
	funcoes_heuristicas = { 'qtd_rotulos': label_amount }
	funcoes_busca = { 'estrela': busca_estrela, 'guloso': busca_gulosa, 'largura': busca_largura, 'profundidade': busca_profundidade  }

	algoritmo = None
	heuristica = None
        arquivo_de_entrada = None
        diretorio_de_entrada = None

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'a:h:d:f:u', ['algoritmo=', 'heuristica=', 'diretorio_de_entrada=','arquivo_de_entrada=','dumb='])
	except getopt.GetoptError:
		usage()
	
	if len(opts) == 0:
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-a', '--algoritmo'):
			try:
                                algoritmo = funcoes_busca[arg]	
			except KeyError:
				usage()
				sys.exit(2)
                                
		elif opt in ('-h', '--heuristica'):
			try:
				heuristica = funcoes_heuristicas[arg]
			except KeyError:
				usage()
				sys.exit(2)
                                
        	elif opt in ('-d', '--diretorio_de_entrada'):
                        print(arg)
                        if not os.path.isdir(arg):
                                print("Diretorio invalido")
                                usage()
                                sys.exit(2)
                        diretorio_de_entrada = arg

                elif opt in ('-f', '--arquivo_de_entrada'):
                        if not os.path.isfile(arg):
                                print("Arquivo invalido")
                                usage()
                                sys.exit(2)
                        arquivo_de_entrada = arg

                elif opt in ('-u', '--unused'):
                                usage()
                                sys.exit(2)
                else:
                        print("Opcao inexistente")
                        usage()
                        sys.exit(2)
                        

        processar_grafos(algoritmo, heuristica, arquivo_de_entrada, diretorio_de_entrada)

	
if __name__ == '__main__':
	main()
