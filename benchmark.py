import argparse
from enum import Enum
import time
import math
import random
from pathlib import Path
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort1 import hybrid_sort1
from hybrid_sort2 import hybrid_sort2
from hybrid_sort3 import hybrid_sort3
import csv
parser = argparse.ArgumentParser(
    prog= "Benchmark",
    description= "Benchmark the performance of sorting algorithm",
)

class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'uniform'
    REVERSE_SORTED = 'reverse'
    ALMOST_SORTED = 'almost'

DATA_DIRECTORY = Path('data')

SORTING_ALGORITHMS = {
    'insertion_sort': insertion_sort,
    'merge_sort': merge_sort,
    'shell_sort1': shell_sort1,
    'shell_sort2': shell_sort2,
    'shell_sort3': shell_sort3,
    'shell_sort4': shell_sort4,
    'hybrid_sort1': hybrid_sort1,
    'hybrid_sort2': hybrid_sort2,
    'hybrid_sort3': hybrid_sort3
}

parser.add_argument('size', type=int, help='size of the input list')
parser.add_argument('permutation', type=PermutationType, help = "permetation of the input list")
parser.add_argument('algorithm_name', choices=SORTING_ALGORITHMS.keys(), help="Name of the sorting")

def generate_random_list(size:int, permutation: PermutationType)->list[int]:
    nums = []
    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            nums = generate_uniformly_distributed_permutation(size)
        case PermutationType.REVERSE_SORTED:
            nums = generate_reverse_list(size)
        case PermutationType.ALMOST_SORTED:
            nums = generate_almost_sorted_permutation(size)
    return nums

def generate_uniformly_distributed_permutation(n):
    permutation = list(range(1, n+1))
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)  # Choose a random index j such that 0 ≤ j ≤ i
        permutation[i], permutation[j] = permutation[j], permutation[i]  # Swap the elements at indices i and j
    return permutation
def generate_reverse_list(n):
    reverse_list = list(range(n, 0, -1))
    return reverse_list
def generate_almost_sorted_permutation(n):
    permutation = list(range(1, n+1))
    
    # Choose the number of pairs to swap (2log n)
    num_pairs = int(2 * math.log(n,2))

    for _ in range(num_pairs):
        # Generate random indices i and j
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        
        # Ensure i and j are distinct
        while i == j:
            j = random.randint(0, n-1)
        # Swap elements at indices i and j
        permutation[i], permutation[j] = permutation[j], permutation[i]

    return permutation

def get_data_path(permutation: PermutationType, algorithm_name: str) -> Path:
    directory = DATA_DIRECTORY/algorithm_name
    directory.mkdir(parents=True, exist_ok=True)
    return (directory/permutation.value).with_suffix('.csv')


def save_data(size: int, permutation: PermutationType, algorithm_name:str, time_ns: int):
    path = get_data_path(permutation, algorithm_name)
    with open(path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([size, time_ns])


def run_benchmark(size: int, permutation: PermutationType, algorithm_name: str, algorithm) -> int:
    nums = generate_random_list(size, permutation)
    start_time = time.process_time_ns()
    algorithm(nums)
    end_time = time.process_time_ns()
    print("after sorting: ", nums)
    return end_time - start_time

if __name__ == "__main__":
    args = parser.parse_args()
    args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]
    t = run_benchmark(args.size, args.permutation, args.algorithm_name, args.algorithm)
    get_data_path(args.permutation, args.algorithm_name)
    save_data(args.size, args.permutation, args.algorithm_name, t)

   
