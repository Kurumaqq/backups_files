from shutil import make_archive
from time import sleep
import os
import json



def dirs_archive(dirs_input : list, dir_output : str, format : str) -> None:
    for dir in dirs_input:
        for name in os.listdir(dir):
            full_path_input = dir + name
            full_path_output = f'{dir_output}/{name}'

            make_archive(full_path_output, format, full_path_input)

def dir_archive(dir_input : list, dir_output : str, format : str) -> None:
    for full_path_input in dir_input:
        name = full_path_input.split('/')[-1]
        full_path_output = f'{dir_output}/{name}'
        make_archive(full_path_output, format, full_path_input)



if __name__ == '__main__':
    while True:
        with open('config.json', 'r') as read_file: config = json.load(read_file)

        dirs_input = config['dirs_input']
        dir_input = config['dir_input']
        dir_output = config['dir_output']
        format = config['format']
        timer = config['timer'] * 60*60
        
        dirs_archive(dirs_input, dir_output, format)
        dir_archive(dir_input, dir_output, format)
        sleep(timer)
    