import subprocess
import os
import pathlib


def install(modules):
    for module in modules:
        result = subprocess.run(
            f'pip install {module}', shell=True, capture_output=True)


def extension(path):
    return pathlib.PurePath(path).suffix


def get_modules(path):
    modules = []
    with open(path) as file:
        for line in file:
            words = line.strip().split()
            try:
                if words[0] == 'import' or words[0] == 'from':
                    if 'mymodules' not in words[1]:
                        if '.' not in words[1]:
                            modules.append(words[1])
                        else:
                            modules.append(words[1].split('.')[0])
            except:
                continue
    return modules


def main():
    path_to_directory = str(pathlib.Path(__file__).parent.absolute())
    for file in os.listdir(path_to_directory):
        if extension(file) == '.py':
            modules = get_modules(file)
            install(modules)

    # path = input()
    # install(modules(path))


if __name__ == '__main__':
    main()
