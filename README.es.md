# Algorithm explorer
> Una herramienta para comparar tiempos de ejecución entre algoritmos de ordenación, búsqueda y matemáticos.

## Características
- Implementaciones desde cero de algoritmos.
- Benchmarks para comparar tiempos de ejecución.
- UI práctica e intuitiva.
- Tests unitarios con unittest.

## Tecnologías y librerías
- Python 3.12+
- unittest
- functools
- random
- time

## Estructura del proyecto
```
algorithm-explorer/
├── src/
│   ├── main.py                 --> Menú interactivo por consola
│   ├── benchmark.py            --> Medición de tiempos y preparación de los benchmarks
│   └── algorithms/
│       ├── sorting/            --> bubble, insertion, selection, merge, quick
│       ├── searching/          --> linear, binary, binary recursivo
│       └── mathematics/        --> factorial recursivo, fibonacci recursivo y cacheado
├── tests/
│   ├── test_benchmark.py
│   ├── test_sorting_algorithms.py
│   ├── test_searching_algorithms.py
│   └── test_mathematic_algorithms.py
├── LICENSE
└── README.es.md
```

Cada algoritmo está en su propio módulo con una función documentada con sus complejidades temporal y espacial. `benchmark.py` genera los datos de prueba para el benchmark y mide el tiempo de cada una con `time.perf_counter`.

## Algoritmos
| Algoritmo                      |          Mejor |          Medio |           Peor |     Espacial |
| ------------------------------ | -------------: | -------------: | -------------: | -----------: |
| Bubble Sort                    |       **O(n)** |      **O(n²)** |      **O(n²)** |     **O(1)** |
| Insertion Sort                 |       **O(n)** |      **O(n²)** |      **O(n²)** |     **O(1)** |
| Selection Sort                 |      **O(n²)** |      **O(n²)** |      **O(n²)** |     **O(1)** |
| Merge Sort                     | **O(n log n)** | **O(n log n)** | **O(n log n)** |     **O(n)** |
| Quick Sort                     | **O(n log n)** | **O(n log n)** |      **O(n²)** | **O(log n)** |
| Linear Search                  |       **O(1)** |       **O(n)** |       **O(n)** |     **O(1)** |
| Binary Search                  |       **O(1)** |   **O(log n)** |   **O(log n)** |     **O(1)** |
| Recursive Binary Search        |       **O(1)** |   **O(log n)** |   **O(log n)** | **O(log n)** |
| Recursive Factorial            |       **O(1)** |       **O(n)** |       **O(n)** |     **O(n)** |
| Recursive Fibonacci            |       **O(1)** |      **O(2ⁿ)** |      **O(2ⁿ)** |     **O(n)** |
| Cached Fibonacci               |       **O(1)** |       **O(n)** |       **O(n)** |     **O(n)** |


## Testing
Los tests están escritos con `unittest`. Los de algoritmos usan `subTest` para ejecutar el
mismo caso contra todas las implementaciones de una misma familia.

- `test_sorting_algorithms.py`: listas vacías, de un elemento, ordenadas, invertidas, con
  elementos repetidos, todos iguales y con números negativos.
- `test_searching_algorithms.py`: elemento presente y ausente, búsquedas en el primer y último
  índice, listas vacías, con repetidos y con negativos.
- `test_mathematic_algorithms.py`: casos base (0 y 1), números normales y grandes, y ValueError
  al pasar negativos.
- `test_benchmark.py`: generación de listas de prueba, medición de tiempos y formateo.

## Cómo ejecutar
#### Requerimientos
- Python 3.12+
- No hay dependencias externas.

```bash
git clone https://github.com/HelloAdrian2k/algorithm-explorer.git
cd algorithm-explorer
```

#### Ejecutar el proyecto
```bash
python -m src.main
```
Se abre un menú por consola donde eliges la familia de algoritmos.

#### Ejecutar los tests
```bash
python -m unittest tests.test_benchmark tests.test_sorting_algorithms tests.test_searching_algorithms tests.test_mathematic_algorithms
```

O un único módulo:

```bash
python -m unittest tests.test_sorting_algorithms
```

## Mejoras futuras
- Añadir más algoritmos
    - Más algoritmos matemáticos
    - Más algoritmos de búsqueda
    - Más algoritmos de ordenamiento
- Añadir otras categorías de benchmark específicas:
    - Comparación entre fibonacci
    - Comparación entre binary searches
    - Comparación contra Python.
- Elegir entre varios tipos de tamaños de lista y varios tipos de datos de prueba:
    - Lista ordenada
    - Lista inversa
    - Lista aleatoria
    - Lista con muchos elementos repetidos
    - Lista ordenada con solo 2 intercambios
- Añadir reproducibilidad en benchmarks con semillas al generar
- Añadir resumen detallado de rendimiento entre pruebas:
    - Mostrar incremento del tiempo según tamaños de lista
    - Mostrar speedup entre algoritmos. (X 53x más rápido que Y)
- Añadir benchmark de consumo de memoria
