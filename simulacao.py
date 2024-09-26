from processos import adicionar_processos

def obter_tempo_chegada(processo):
    return processo.tempo_chegada

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))  # Removendo as barras laterais

def fifo_escalonamento_matriz(processos):
    processos.sort(key=obter_tempo_chegada)

    ultimo_processo = max([p.tempo_chegada for p in processos])  # Descobre-se o último processo
    tempo_total = 0
    for processo in processos:
        if processo.tempo_chegada == ultimo_processo:
            tempo_total = processo.tempo_chegada + processo.tempo_servico  # Calcula-se o tempo total de execução

    # Certifique-se de que tempo_total é calculado corretamente
    
    matriz = []

    # Primeira linha da matriz (representando o tempo)
    linha_tempo = [str(i).zfill(2) for i in range(tempo_total + 1)]  # Usando zfill para formatar os números
    matriz.append(linha_tempo)

    # Inicializando as linhas da matriz para cada processo
    for processo in processos:
        matriz.append(["# " for _ in range(tempo_total + 1)])

    tempo_atual = 0
    fila = []
    processo_em_andamento = None

    while tempo_atual <= tempo_total or fila:
        # Adicionar processos à fila com base no tempo de chegada
        for processo in processos:
            if processo.tempo_chegada == tempo_atual and processo not in fila:
                fila.append(processo)
                matriz[processos.index(processo) + 1][tempo_atual] = "X "  # Marca 'X' na matriz na hora de chegada

        if not processo_em_andamento and fila:
            processo_em_andamento = fila.pop(0)

        if processo_em_andamento:
            processo_em_andamento.tempo_restante -= 1
            if tempo_atual < len(matriz[processos.index(processo_em_andamento) + 1]):
                matriz[processos.index(processo_em_andamento) + 1][tempo_atual + 1] = f"{processo_em_andamento.nome} "

            if processo_em_andamento.tempo_restante == 0:
                processo_em_andamento.tempo_termino = tempo_atual
                processo_em_andamento = None

        tempo_atual += 1

    # Imprimir a matriz completa
    imprimir_matriz(matriz)

# Executar o simulador
processos = adicionar_processos()
fifo_escalonamento_matriz(processos)
