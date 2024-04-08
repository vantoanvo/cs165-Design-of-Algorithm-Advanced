import argparse
from enum import Enum
import time
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
    nums = list(range(size))
    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            pass
        case PermutationType.REVERSE_SORTED:
            nums.reverse()
        case PermutationType.ALMOST_SORTED:
            pass
    return nums
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
    return end_time - start_time

if __name__ == "__main__":
    args = parser.parse_args()
    args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]
    t = run_benchmark(args.size, args.permutation, args.algorithm_name, args.algorithm)
    get_data_path(args.permutation, args.algorithm_name)
    save_data(args.size, args.permutation, args.algorithm_name, t)
   
