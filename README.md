# Algorithm explorer
> A tool to compare execution times between sorting, searching and mathematical algorithms.

## Features
- Algorithm implementations written from scratch.
- Benchmarks to compare execution times.
- Practical and intuitive UI.
- Unit tests with unittest.

## Technologies and libraries
- Python 3.12+
- unittest
- functools
- random
- time

## Project structure
```
algorithm-explorer/
├── src/
│   ├── main.py                 --> Interactive console menu
│   ├── benchmark.py            --> Time measurement and benchmark setup
│   └── algorithms/
│       ├── sorting/            --> bubble, insertion, selection, merge, quick
│       ├── searching/          --> linear, binary, recursive binary
│       └── mathematics/        --> recursive factorial, recursive and cached fibonacci
├── tests/
│   ├── test_benchmark.py
│   ├── test_sorting_algorithms.py
│   ├── test_searching_algorithms.py
│   └── test_mathematic_algorithms.py
├── LICENSE
├── README.md
└── README.es.md
```

Each algorithm lives in its own module with a function documented with its time and space complexities. `benchmark.py` generates the test data for the benchmark and measures the time of each one with `time.perf_counter`.

## Algorithms
| Algorithm                      |           Best |        Average |          Worst |        Space |
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
Tests are written with `unittest`. The algorithm tests use `subTest` to run the same case
against every implementation of the same family.

- `test_sorting_algorithms.py`: empty lists, single-element lists, sorted, reversed, with
  repeated elements, all elements equal and with negative numbers.
- `test_searching_algorithms.py`: present and absent elements, searches at the first and last
  index, empty lists, lists with duplicates and with negative numbers.
- `test_mathematic_algorithms.py`: base cases (0 and 1), regular and large numbers, and
  ValueError when passing negative numbers.
- `test_benchmark.py`: test list generation, time measurement and formatting.

## How to run
#### Requirements
- Python 3.12+
- No external dependencies.

```bash
git clone https://github.com/HelloAdrian2k/algorithm-explorer.git
cd algorithm-explorer
```

#### Run the project
```bash
python -m src.main
```
A console menu opens where you choose the algorithm family.

#### Run the tests
```bash
python -m unittest tests.test_benchmark tests.test_sorting_algorithms tests.test_searching_algorithms tests.test_mathematic_algorithms
```

Or a single module:

```bash
python -m unittest tests.test_sorting_algorithms
```

## Future improvements
- Add more algorithms
    - More mathematical algorithms
    - More searching algorithms
    - More sorting algorithms
- Add other specific benchmark categories:
    - Comparison between fibonacci implementations
    - Comparison between binary searches
    - Comparison against Python's built-ins
- Choose between several list sizes and several types of test data:
    - Sorted list
    - Reversed list
    - Random list
    - List with many repeated elements
    - Sorted list with only 2 swaps
- Add reproducibility to the benchmarks with seeds when generating data
- Add a detailed performance summary across runs:
    - Show how time grows with list size
    - Show the speedup between algorithms (X is 53x faster than Y)
- Add a memory usage benchmark
