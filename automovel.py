'''
Um automóvel passa pelo marco km 40 de uma rodovia às 14h e pelo marco km 250 às 17h.
Calcule a velocidade escalar média desse automóvel no intervalo de tempo dado.
'''

#calculo a variação de espaço
def variacao_espaco (posicao_final,posicao_inicial):
    delta_espaco = posicao_final - posicao_inicial
    print('variação de espaço:', delta_espaco,'km')

#calculo a variação de tempo
def variacao_tempo (tempo_final, tempo_inicial):
    delta_tempo = tempo_final - tempo_inicial
    print('variação de espaço:', delta_tempo, 'horas')

#velocidade média do automovel 
def velocidade_media(posicao_final,posicao_inicial,tempo_final,tempo_inicial):
    delta_espaco = posicao_final - posicao_inicial
    delta_tempo = tempo_final - tempo_inicial
    print('velocidade média:',delta_espaco / delta_tempo, 'Km/h')

variacao_espaco(250,40)
variacao_tempo(17,14)
velocidade_media(250,40,17,14)
