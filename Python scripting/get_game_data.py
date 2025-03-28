"""
    Copy only the folders that have "game" in their name and all their content
    from a chosen folder to a new chosen folder. These copied folders will be
    renamed without the "game".
"""

import os
import json
import shutil
from subprocess import PIPE, run  # to run any terminal command I want
import sys  # to gain access to command-line arguments


GAME_DIR_PATTER = "game"  # look for the string "game" in every directory
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def find_all_game_paths(source):
    game_paths = []

    # Walk recursively through the source directory
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTER in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break  # only run this one time. I only care about the top-level directory

    return game_paths


def get_name_from_paths(paths, to_strip):
    new_names = []

    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


def make_json_metadata_file(path, game_dirs):
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }

    with open(path, "w") as file:
        json.dump(data, file)


def compile_game_code(path):
    # find filename
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break

        break

    if code_file_name is None:
        return

    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print(f"Compile result: {result}")

    # return to current working directory
    os.chdir(cwd)


def main(source, target):
    # current working directory
    cwd = os.getcwd()
    # get complete paths
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    # get game paths and create new ones
    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "_game")
    # create target path
    create_dir(target_path)
    # copy
    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        # compile
        compile_game_code(dest_path)
    # create metadata file
    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)


# Checks if I'm running this file directly
# to allow importing this file without running it.
if __name__ == "__main__":
    args = sys.argv

    if len(args) != 3:
        raise Exception("You must pass a source and traget directory - only.")

    source, target = args[1:]
    main(source, target)
