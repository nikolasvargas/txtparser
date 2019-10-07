from pathlib import Path
from watchgod import watch

from directory import create_inpath, create_outpath, INPUT_DIRECTORY
from files import process_file


if __name__ == '__main__':
    create_inpath()
    create_outpath()
    process_file()

    outpath: str = Path.home() / INPUT_DIRECTORY
    delete_event: str = 'Change.deleted'

    for changes in watch(outpath):
        process_file(
            file[1] for file in changes
            if delete_event not in str(file[0])
        )
