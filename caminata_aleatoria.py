
from individuo import Aleatorio_Tradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, persona, pasos):
    inicio = campo.obtener_coordenada(persona)

    for _ in range(pasos):
        campo.mover_persona(persona)

    return inicio.distancia(campo.obtener_coordenada(persona))

def simular_caminata(pasos, numero_de_intentos, tipo_de_tendencia):
    persona = tipo_de_tendencia(nombre='Nombre1')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_persona(persona, origen)
        simulacion_caminata = caminata(campo, persona, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_tendencia):

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_tendencia)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_tendencia.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Distancia maxima = {distancia_maxima}')
        print(f'Distancia minima = {distancia_minima}')

if __name__ == '__main__':
    distancias_de_caminata = [10,100,1000,10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, Aleatorio_Tradicional)