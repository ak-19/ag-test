from sys import argv

from Optimizer import Optimizer
from FileHandler import FileHandler

def main(files):
    if not files or len(files) != 2:
        print('Usage: missing input and output files paths')
        return
    [input_file, output_file] = files
    file_handler = FileHandler(input_file, output_file)
    data = file_handler.load_data()
    file_handler.save(Optimizer(data['items'], data['total_space']).get_result())

if __name__ == '__main__':
    main(argv[1:])