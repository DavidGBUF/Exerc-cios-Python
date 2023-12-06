import matplotlib.pyplot as plt
import timeit

# Função de busca binária recursiva
def busca_binaria_recursiva(lista, numero):
    # Cria uma cópia da lista para trabalhar com ela
    lista_ordenada = lista[::]
    
    # Define os índices inicial, médio e final
    indice_min = 0
    indice_max = len(lista_ordenada) - 1
    indice_medio = (indice_max + indice_min) // 2
    
    # Caso base: se a lista estiver vazia, o número não está presente
    if len(lista_ordenada) <= 0:
        return f"O número {numero} não está na lista"
    
    # Se o número for encontrado, retorna que está na lista
    if lista_ordenada[indice_medio] == numero:
        return f"O número {numero} está na lista"
    
    # Se o número do meio for maior, busca na metade inferior
    if lista_ordenada[indice_medio] > numero:
        return busca_binaria_recursiva(lista_ordenada[indice_min:indice_medio], numero)
    
    # Se o número do meio for menor, busca na metade superior
    if lista_ordenada[indice_medio] < numero:
        return busca_binaria_recursiva(lista_ordenada[indice_medio + 1:indice_max + 1], numero)

# Lista para teste
lista = []

# Função para executar a busca e medir o tempo
def resultado_busca():
    return busca_binaria_recursiva(lista, 0)

# Lista para armazenar os tempos de execução
lista_tempos = []

# Executa a busca 1000 vezes e mede o tempo
for i in range(1000):
    lista = [1 for _ in range(i)]
    tempo = timeit.timeit(resultado_busca, number=5) / 5
    lista_tempos.append(tempo)

# Lista com os tamanhos de entrada
tamanhos_entrada = [i for i in range(1000)]

# Plota o gráfico dos tempos de execução
plt.plot(tamanhos_entrada, lista_tempos)
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (s)')
plt.title('Desempenho da Busca Binária Recursiva')
plt.show()
