import os

students_list = [
    'yuliiavoronina',
    'kloncopy23',
    'StupakVitalii',
    'Andrey3112',
    'AndrBoiko',
    'xslmur',
    'ViktoriiaFedorenko',
    'obodman37',
    'Yevgeniy99',
    'KBiliak',
    'QA-Dmytro-Melnyk',
    'RollerLeon',
    'YashaMoisha2015',
    'Valentyn_Vildiaiev',
    'iegorkobieliev',
    'Yuzhna',
    'grabarvlad'
]

path_to_folder = "./lesson_11/home_work/"  # Change this to the desired parent directory

for folder in students_list:
    # Combine the parent directory and folder name to get the full path
    full_path = os.path.join(path_to_folder, folder)
    # Create the folder
    os.makedirs(full_path, exist_ok=True)

    with open(f'{full_path}/__init__.py', 'w'):
        pass
