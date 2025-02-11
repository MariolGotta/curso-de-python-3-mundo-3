# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depoismostre:
# Apenas os 5 primeiros colocados
# Os ultimos 4 colocados da tabela.
# Uma lista com os timers em ordem alfabética
# Em que posição da tabela está o time do São Paulo

times_brasileirao = (
    "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
    "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco",
    "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude",
    "Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá"
)

print('-='*25)
print(f'Lista de times do Brasileirão: {times_brasileirao}')
print('-='*25)
print(f'Os 5 primeiros são {times_brasileirao[0:5]}')
print('-='*25)
print(f'Os 4 últimos são {times_brasileirao[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print('-='*25)
print(f'O São Paulo está na {times_brasileirao.index('São Paulo')+1}ª posição')
print('-='*25)
