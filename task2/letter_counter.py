from argparse import ArgumentParser
from collections import Counter
from itertools import repeat
from multiprocessing import cpu_count, Pool
from pathlib import Path
import requests


def count_for_file(file_name, url, directory):
    """
    Loads and saves text file, returns Counter of its content.
    """
    text = requests.get(url + file_name).text
    path = directory / file_name
    path.write_text(text, encoding='utf-8')
    return Counter(text)


def save_counter(c):
    """
    Saves Counter into file taking care of special symbols like '\n'
    """
    result_path = Path('result.txt')
    with result_path.open('w', encoding='utf-8') as result:
        for key, val in c.items():
            print(repr(key), val, file=result)


def main(url, num_processes):
    """
    * Gets list of text files in the dataset from files.txt
    * Creates 'dataset' directory
    * Runs num_processes processes with count_for_file function
    """
    r = requests.get(url + 'files.txt')
    files_list = r.text.split('\n')
    n_files = len(files_list)

    directory = Path('dataset')
    directory.mkdir(exist_ok=True)

    with Pool(num_processes) as pool:
        counters = pool.starmap(count_for_file, zip(files_list, repeat(url, n_files), repeat(directory, n_files)))

    final_counter = Counter()
    for counter in counters:
        final_counter += counter
    save_counter(final_counter)


if __name__ == "__main__":
    parser = ArgumentParser(description='Character counter for the provided dataset')
    parser.add_argument('--url', help='url to dataset', required=True)
    parser.add_argument('--num_processes',
                        help='number of processes to use for loading/counting; default = number of CPUs',
                        required=False,
                        type=int,
                        default=cpu_count()
                        )
    args = parser.parse_args()
    main(args.url, args.num_processes)
