###### Bienvenid@! :purple_heart: Puedes encontrame en: 
[![Twitter](https://user-images.githubusercontent.com/282759/84680160-40c90c80-af00-11ea-8390-bb86858c5fa5.png)](https://twitter.com/AbdielGuerrer20) [![LinkedIn](https://user-images.githubusercontent.com/282759/84680162-4161a300-af00-11ea-912c-8f32e5cc1676.png)](https://www.linkedin.com/in/abdiel-guerrero-360a39195/)

[![Twitter: AbdielGuerrero](https://img.shields.io/twitter/follow/AbdielGuerrer20?style=social)](https://twitter.com/AbdielGuerrer20)[![Linkedin:Abdiel Guerrero](https://img.shields.io/badge/-AbdielGuerrero-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/abdiel-guerrero-360a39195/)](https://www.linkedin.com/in/abdiel-guerrero-360a39195/)[![GitHub abdielgv162](https://img.shields.io/github/followers/abdielgv162?label=follow&style=social)](https://github.com/abdielgv162)[![Instagram: AbdielGuerrero](https://img.shields.io/badge/-abdielgv162-blue?style=flat-square&logo=Instagram&logoColor=white&link=https://www.instagram.com/abdielgv162/)](https://www.instagram.com/abdielgv162/)

---

<div align="Center"><h2>Estadística computacional con Python </h2></div>
<div align="center">
    <img src="https://i.pinimg.com/originals/30/d9/1e/30d91e04235f12b644fcdf15081d164b.gif" width="400" height="250" >
</div>
<div align="Center">
    <br><i>Documento basado en el curso de Estadística Computacional de Platzi.</i></br>
    <i>Impartido por David Aroesti.</i>

</div>

---

  - [Objetivos](#objetivos)
  - [Programacion dinámica](#programacion-dinámica)
    - [Introduccion a la Programación Dinámica](#introduccion-a-la-programación-dinámica)
    - [Optimizacion de Fibonacci](#Optimizacion-de-Fibonacci)
      - [Explicacion Fibonacci recursivo vs Fibonacci Dinámico](#explicación-fibonacci-recursivo-vs-fibonacci-dinámico)
        - [Porque usar diccionarios y no listas?](#por-que-usar-diccionario-y-no-listas)
  - [Caminos aleatorios](#caminos-aleatorios)
    - [¿Qué son los caminos aleatorios?](#qué-son-los-caminos-aleatorios)
     - [Caminata aleatoria](#caminana-aleatoria)
     - [Desarrollando la simulación](#desarrollando-la-simulación)

---

## Objetivos

* Aprender cuándo utilizar Programación Dinámica y sus beneficios.
* Entender la diferencia entre programas deterministas y estocásticos.
* Aprender a utilizar Programacion Estocástica.
* Aprender a crear simulaciones computacionales válidas.
* Aprender a simplificar la notacion big O(n) de ciertos algoritmos de optimización.

---

## Programacion dinámica

### Introduccion a la Programación Dinámica

<i>La programación dinámica es es un método para reducir el tiempo de ejecución de un algoritmo mediante la utilización de subproblemas superpuestos y subestructuras óptimas.</i>

El matemático Richard Bellman inventó la programación dinámica en 1953 que se utiliza para optimizar problemas complejos que pueden ser discretizados y secuencializados.
<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Richard_Ernest_Bellman.jpg/220px-Richard_Ernest_Bellman.jpg" width="300" height="300" >
    <h5>Richard Bellman</h5>
</div>

Fun fact :
El nombre de Programación Dinámica lo escogió Bellman para esconder a los patrocinadores gubernamentales que financiaban su investigacion, el hecho que en realidad estaba haciendo matemáticas. Lo usó para que ningún congresista pudiera oponerse a ese nombre tan atractivo.

La programación dinámica permite optimizar ciertos problemas que cuentan con.

- <strong>Subestructura Óptima:</strong>
    <i>Una solución global óptima se puede encontrar al combinar soluciones óptimas de subproblemas locales.</i>
    En otras palabras, los subproblemas se resuelven a su vez dividiéndolos en subproblemas más pequeños hasta que se alcance el caso fácil, donde la solución al problema es trivial. 

- <strong>Problemas empalmados:</strong>
    <i>Una solución óptima que involucra resolver el mismo problema en varias ocasiones (cómo en el caso de la recursiviadad).</i>
    Es decir, que se usa un mismo subproblema para resolver diferentes problemas mayores. Por ejemplo, en la sucesión de Fibonacci <i>(f3 = f1 + f2) y (f4 = f2 + f3)</i>.

La optimizacion para que el programa se ejecute mucho más rápido se logra a través de la <strong>memorización:</strong>
- <i>La memorización es una técnica para guardar cómputos previos y evitar realizarlos nuevamente.</i>
- <i>Normalmente se utiliza un diccionario { } , donde las consultas se pueden hacer en O(1) .</i>
- <i>Intercambia: Tiempo vs Espacio en memoria.</i>
  
La <strong>memorización</strong> nos ayuda a evitar computos adicionales, guardando el resultado de computaciones previas en alguna estructura de datos que podemos consultar rápidamente.

---

### Optimizacion de Fibonacci

Recordemos los numeros de Fibonacci.

<div align="center">
    <img src="https://lh3.googleusercontent.com/proxy/VukrJ6Oxe7tPB5i2SMVUhIJZTRe36SMJLDWjn9GUy61M7TNvViAuDcJWTAhnRuiFUHmwutd1t352H8L1WIAmbVml6kM2Fn_isBz-XlKHbTbpm5YwP38tWnuC0w" width="250" >
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/PascalTriangleFibanacci.svg/360px-PascalTriangleFibanacci.svg.png" width="350" height="250" >
</div>

La forma recursiva de Fibonacci <i>f(n) = f<sub>n-1</sub> + f<sub>n-2 </sub></i> es muy fácil de implementar en código, pero es poco eficiente ya que repetimos el mismo computo muchas veces, aumentando innecesariamente la cantidad de iteraciones.

Para optimizar esta función haremos uso de la memorización anteriormente mencionada.
Aqui tenemos una implementación de <i>Fibonacci Recursivo vs Fibonacci Dinámico: </i>
```py
import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_dinamico(n, memoria={}):
    if n == 0 or n == 1 :
        return 1
    try:
        return memoria[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    n = int(input("Escoge un numero: "))
    # resultado = fibonacci_recursivo(n)
    resultado = fibonacci_dinamico(n)
    print(resultado)
```
---

#### Explicación Fibonacci Recursivo vs Fibonacci Dinámico

```py
def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
```

En esta parte tenemos la función de `fibonacci_recursivo()`.

Definimos la función con un parámetro <i>n</i> de entrada, ahora en el primer `if` cómo sabemos que el caso base de Fibonacci para 0 y 1 es igual a 1 solo retornamos 1. 

De no ser así, retornaremos una llamada recursiva de Fibonacci para el numero anterior <i>(n-1)</i> más el numero anterior a ese <i>(n-2)</i>.

Recordemos que la recursividad es la forma en la cual se especifica un proceso basado en su propia definición, que en este caso es una función que se llama a sí misma.

```py
def fibonacci_dinamico(n, memoria={}):
    if n == 0 or n == 1 :
        return 1
    try:
        return memoria[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado
```

Aqui tenemos la version <i>dinámica</i>.

Primero definimos la función `fibonacci_dinamico()`, donde a diferencia de la primera tenemos un parametro extra llamado `memoria{}` , que es un diccionario que en este caso será nuestra estructura de datos para efectuar la <i>memorización</i>

Ahora tenemos algo nuevo llamado `try/except`, este es un buen mecanismo para el control del flujo del programa ya que nos permite manejar la excepciones que puedan surgir y tomar acciones de recuperación para evitar la interrupción del programa o, al menos, para realizar algunas acciones adicionales antes de interrumpirlo.

```py
    try:
        return memoria[n]
```
Dentro del bloque `try` se ubica todo el código que pueda llegar a levantar una excepción, se utiliza el término levantar para referirse a la acción de <i>generar una excepción</i>.

Si tenemos como llave <i>[n]</i> en el diccionario, regresemos <i>n</i>.

```py
    except KeyError:
        resultado = fibonacci_dinamico(n-1, memoria) + fibonacci_dinamico(n-2, memoria)
        memoria[n] = resultado
        return resultado
```
El bloque `except` se encarga de capturar la excepción y nos da la oportunidad de procesarla.

Si no tenemos como llave <i>[n]</i> en el diccionario, anticiparemos el `KeyError` que nos saldría al intentar acceder a una llave que no existe.

Nos anticiparemos llamando a la funcion `fibonacci_dinamico()` para <i>(n-1)</i> y <i>(n-2)</i>, pero en este caso tendremos como parametro extra el diccionario `memoria{}` para después guardar ahí el resultado anterior, y retornaremos este valor para la siguiente iteración.

Esta es la parte diferenciadora entre la versión recursiva simple y la versión dinámica, ya que al tener los resultados de iteraciones anteriores dentro del diccionario nos ahorraremos el tiempo del calcular todos los resultados anteriores de <i>n</i> para solo tener que buscar ese resultado anterior dentro del diccionario y sumarlo, lo cual hace MUCHO más eficiente el algoritmo.

Tan solo calcular <i>n=50</i> con `fibonacci_recursivo()` toma muchísimo más tiempo que calcular <i>n=500</i> con `fibonacci_dinamico()`.

```py
import sys
    .
    .
    .
    sys.setrecursionlimit(10000)
```

Estas lineas nos ayudan a incrementar el límite de recursividad limitado por python, importando la librería `sys` para seleccionar el limite de recursión.

---

#### Por que usar diccionario y no listas?

El algoritmo que usa Python internamente para buscar un elemento en un diccionario es muy distinto que el que utiliza para buscar en listas.

<i>Para buscar en las listas, se utiliza un algoritmos de comparación que tarda cada vez más a medida que la lista se hace más larga. En cambio, para buscar en diccionarios se utiliza un algoritmo llamado hash, que se basa en realizar un cálculo numérico sobre la clave del elemento, y tiene una propiedad muy interesante: sin importar cuántos elementos tenga el diccionario, el tiempo de búsqueda es siempre aproximadamente igual O(1).

Este algoritmo de hash es también la razón por la cual las claves de los diccionarios deben ser inmutables, ya que la operación hecha sobre las claves debe dar siempre el mismo resultado, y si se utilizara una variable mutable esto no sería posible.</i>

---

## Caminos aleatorios

### ¿Qué son los caminos aleatorios?

* Es un tipo de simulación que elige aleatoriamente una decisión dentro de un conjunto de decisiones válidas.

* Se utilizan en muchos campos del conocimiento cuando los sistemas <i>no son deterministas</i> e incluyen elementos de aleatoriedad.

* Nos permiten realizar simulaciones de eventos de carácter probabilístico o no determinista para entender su comportamiento desde otra perspectiva de análisis.


<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Brownian_motion_large.gif" width="300" height="300" >
    <h6>Movimiento browniano </h6>
</div>

---

### Caminana aleatoria

Para este programa imaginemos que queremos describir el comportamiento de un individuo que camina aleatoriamente dando pasos hacia adelante, atras, izquierda y derecha con la misma probabilidad.

Primero vamos a posicionarnos en un plano cartesiano en donde vamos a describir la trayectoria aleatoria.

<div align="center">
    <img src="https://concepto.de/wp-content/uploads/2019/09/plano-cartesiano-cuadrantes-e1569779047143.jpg" width="400" height="300" >
    <br></br>
</div>

Para atacar este problema lo vamos a dividir en 3 clases, la clase `Individuo` que modelará a la persona que efectúa el movimiento, la clase `Campo` que es el entorno en el cual se va a mover y la clase `Coordenada` que modelará el punto en el que se encuentra el borracho a lo largo del recorrido.

```py
import random

class Individuo:
    def __init__ (self,nombre):
        self.nombre = nombre

class Aleatorio_Tradicional(Individuo):
    def __init__ (self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
```
Recordando el concepto de <i>herencia de POO</i>, podemos observar que estamos creando la superclase `Individuo` que solo recibe como parametro nombre (recordemos que `self` es obligatorio en cada una ya que hace referencia a la instancia).

Después extendemos la superclase `Individuo` hacia la subclase `Aleatorio_Tradicional`, en la cual crearemos el método `camina()` donde gracias al método `random.choice` simplemente devolverá una selección aleatoria de los valores de nuestra <i>tupla</i> que representa las diferentes direcciones en las que puede dar un paso.

Para la clase `Coordenadas` tenemos lo siguiente.

```py
class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return ((delta_x)**2+(delta_y)**2)**0.5  
```

Creamos la clase con parametros <i>x </i> y <i>y</i>  en su constructor e iniciamos los atributos de instancia  `self.x` y `self.y` que almacenarán las coordenadas a lo largo del movimiento.

Después creamos el método `mover` con parametros `delta_x` y `delta_y` el cual se encargará de traer a la clase `Coordenada`, pero con la siguiente posición, ya que le habrá sumado las diferencias en <i>x </i> y <i>y</i>.

Ahora definimos el método `distancia` que recibirá como parámetro `otra_coordenada`, donde tendremos los atributos de instancia `delta_x` y `delta_y` las cuales son, respectivamente, las diferencias en en el eje <i>x </i> y <i>y</i> . Despúes efectuaremos el Torema de Pitágoras para obtener la distancia resultante.

En la clase `campo` tenemos lo siguiente.

```py
class Campo:
    def __init__(self):
        self.coordenadas_de_persona = {}

    def anadir_persona(self, persona, coordenada):
        self.coordenadas_de_persona[persona] = coordenada

    def mover_persona(self, persona):
        delta_x, delta_y = persona.camina()
        coordenada_actual = self.coordenadas_de_persona[persona]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_persona[persona] = nueva_coordenada

    def obtener_coordenada(self, persona):
        return self.coordenadas_de_persona[persona]
```

Recordemos que el <i>campo</i> modelará el entorno en el que están nuestros individuos y pueden moverse, aquí comenzaremos creando la clase `campo` que no tendrá más parámetros que la referencia a la instancia y definiremos un <i>artibuto de instancia</i> llamado `.coordenadas_de_persona` que simplemente sera un diccionario.

Ahora vamos a crear 3 métodos, el <i>primero</i> será `anadir_persona` que recibira el parametro <i>persona y coordenda</i>, el cual podemos imaginarlo como la acción se situar a algun individuo en el plano, en cierta coordenada. Aquí mismo tendremos una llamada al atributo `.coordenadas_de_persona[persona]` que irá guardando las coordenadas en el diccionario que despúes será de ayuda para trazar su recorrido.

El <i>segundo método</i> es `mover_persona` que tiene como atributo el individuo que queremos mover. Guardaremos en `delta_x` y `delta_y` los valores aleatorios arrojados por `.camina()`, después obtenemos la coordenada actual del diccionario <i>{ }</i> del método anterior y ,posteriormente, obtenemos una nueva coordenada que será igual a la coordenada actual más el moviemiento de `delta_x` y `delta_y` y esta la añadiremos a nuestra lista de coordenadas.

El <i>tecer método</i> `obtener_coordenada` solo tendrá como parametro al individuo que queremos ubicar y lo único que hará será regresar el valor de nuestra coordenada almacenada actualmente en nuestra lista de coordenadas.

<div align="center"><br>
    <img src="https://www.bigger-tree.org/post/2019-09-15-random-walking/rw_anim.gif" width="350" height="200" >
    </br>
</div>
<br></br>

*Aclaracion: Los tres codigos son archivos independientes.*

---

### Desarrollando la simulación




