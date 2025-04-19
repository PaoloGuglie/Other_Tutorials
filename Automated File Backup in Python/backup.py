import os
import shutil
import datetime
import scheduler
import time

from data import *


def create_destination_dir(destination_dir: str) -> None:
    """ Create the directory, ignore errors if already exists """

    try:
        os.mkdir(destination_dir)

    except FileExistsError:
        pass


def main() -> None:

    create_destination_dir(DESTINATION_DIRECTORY)


if __name__ == '__main__':
    main()
