import matplotlib.pyplot as plt
import timeit

# Função de busca binária interativa
def busca_binaria_interativa(lista, num):
    # Cria uma cópia da lista para não alterar a lista original
    lista_auxiliar = lista[::]
    
    # Loop que continua até quebrar explicitamente
    while True:
        # Define os índices máximo e mínimo da lista auxiliar
        IndiceMax = len(lista_auxiliar) - 1
        IndiceMin = 0
        # Calcula o índice médio da lista auxiliar
        IndiceMedio = int((IndiceMax + IndiceMin) / 2)
        
        # Se a lista auxiliar estiver vazia, retorna False (número não encontrado)
        if len(lista_auxiliar) == 0:
            return False
        
        # Se o número no índice médio for maior que o número procurado,
        # atualiza a lista auxiliar para a metade inferior
        if lista_auxiliar[IndiceMedio] > num:
            lista_auxiliar = lista_auxiliar[:IndiceMedio]
        
        # Se o número no índice médio for menor que o número procurado,
        # atualiza a lista auxiliar para a metade superior
        elif lista_auxiliar[IndiceMedio] < num:
            lista_auxiliar = lista_auxiliar[IndiceMedio + 1:]
        
        # Se o número no índice médio for igual ao número procurado,
        # retorna True (número encontrado)
        elif lista_auxiliar[IndiceMedio] == num:
            return True

# Lista para teste (inicialmente vazia)
lista = []

# Função para executar a busca binária e medir o tempo
def resultado_busca():
    # Chama a função de busca binária interativa com a lista e o número 0
    return busca_binaria_interativa(lista, 0)

# Lista para armazenar os tempos de execução
lista_tempos = []

# Executa a busca binária interativa para listas de tamanhos variados e mede o tempo
for i in range(0, 3001, 3):
    # Cria uma lista de tamanho 'i' com todos os elementos iguais a 1
    lista = [1 for indice in range(i)]
    # Mede o tempo de execução da função resultado_busca 100 vezes e calcula a média
    tempo = timeit.timeit(resultado_busca, number=100)
    # Adiciona o tempo médio à lista de tempos
    lista_tempos.append(tempo)

# Lista com os tamanhos de entrada para o gráfico
tamanhos_entrada = [i for i in range(0, 3001, 3)]

# Plota o gráfico dos tempos de execução em função do tamanho da entrada
plt.plot(tamanhos_entrada, lista_tempos)
plt.xlabel('Tamanho da Entrada')  # Rótulo do eixo X
plt.ylabel('Tempo de Execução (s)')  # Rótulo do eixo Y
plt.title('Desempenho da Busca Binária Interativa')  # Título do gráfico
plt.show()  # Exibe o gráfico
