import os
import json
import shutil
from subprocess import PIPE, run  # to run any terminal command I want
import sys  # to gain access to command-line arguments


def main(source, target):
    # current working directory
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    s


# Checks if I'm running this file directly
# to allow importing this file without running it.
if __name__ == "__main__":
    args = sys.argv

    if len(args) != 3:
        raise Exception("You must pass a source and traget directory - only.")

    source, target = args[1:]
    main(source, target)
