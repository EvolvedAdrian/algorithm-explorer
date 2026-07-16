from src.benchmark import prepare_sorting_benchmark
from src.benchmark import prepare_searching_benchmark
from src.benchmark import prepare_mathematics_benchmark
import subprocess
import os

def clear_console():
    subprocess.call("clear" if os.name == 'nt' else 'clear', shell=True)

def select_option(valid_options):
    while True:
        option = int(input("Select an option: "))
        if option in valid_options: 
            return option
        else:
            return None

def main():
    while True:
        clear_console()
        print("=" * 50)
        print("Algorithms explorer")
        print("=" * 50, "\n")
        print("1. Sorting algorithms")
        print("2. Searching algorithms")
        print("3. Mathematic algorithms")
        print("4. Exit")

        valid_options = list(range(1,5))
        option = select_option(valid_options)
        if option is None: 
            continue
        
        clear_console()
        match option:
            case 1:
                prepare_sorting_benchmark()
            case 2:
                prepare_searching_benchmark()
            case 3:
                prepare_mathematics_benchmark()
            case 4:
                exit()
            case _:
                pass
        
        input("\n---\nPress any key to continue...")

main()


