# Desafio:TwoSum - Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que a soma deles sejatarget .
#   Você pode assumir que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.
#   Você pode retornar a resposta em qualquer ordem.

# Exemplo 1:
#   Entrada: nums = [2,7,11,15], alvo = 9
#   Saída: [0,1]
#   Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].

# Tabela Hash - estrutura de dados eficiente que permite armazenar e recuperar informações de forma rápida (mapeia um valor para sua posição na tabela)
# Enumerate - Imprima tuplas de valores de índice E elemento
# Resposta esperada (de acordo com os valores dados): [1,2]

nums = [1,2,3]
target = 5

mapa_nums = {}  # Inicializa o dicionário (mapa) para armazenar números e seus respectivos índices

for i, num in enumerate(nums):  # Itera sobre a lista 'nums', com 'i' sendo o índice e 'num' o valor
    complemento = target - num  # Calcula o complemento: o valor necessário para atingir o 'target'

    if complemento in mapa_nums:  # Verifica se o complemento já foi encontrado em iterações anteriores
        print([mapa_nums[complemento], i])  # Retorna os índices do complemento e do número atual

    mapa_nums[num] = i  # Armazena o número atual e seu índice no dicionário, caso o complemento ainda não tenha sido encontrado
