import os
import shutil
import datetime
import schedule
import time

from data import *


def create_todays_destination_dir_name(destination_dir: str) -> str:
    """ Create today's directory name inside the destination directory """

    today = datetime.date.today()

    today_dir = os.path.join(destination_dir, str(today))

    return today_dir


def copy_folder_to_directory(source_dir: str, destination_dir: str) -> None:

    try:
        shutil.copytree(source_dir, destination_dir)
        print(f"Folder copied to {destination_dir}!")

    except FileExistsError:
        print(f"Folder already exists in {destination_dir}!")


def main() -> None:

    today_dir = create_todays_destination_dir_name(DESTINATION_DIRECTORY)

    copy_folder_to_directory(SOURCE_DIRECTORY, today_dir)


if __name__ == '__main__':

    schedule.every().day.at(RUN_TIME).do(main)  # it does not execute without schedule.run_pending()

    while True:
        # Necessary for the schedule to run
        schedule.run_pending()  # looks for any scheduled task not already run and runs it.
        time.sleep(60)
