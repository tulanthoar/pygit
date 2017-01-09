""" run a python file with logging and output"""
from logging import basicConfig, info, INFO
from os import environ
from pathlib import Path
from time import sleep

from neovim import attach
from sh import python  # pylint: disable=no-name-in-module
from watchdog.events import FileSystemEventHandler
from watchdog.observers.inotify import InotifyObserver


class MyEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""


    def on_moved(self, event):
        super(MyEventHandler, self).on_moved(event)
        what = 'directory' if event.is_directory else 'file'
        info("Moved %s: from %s to %s", what, event.src_path, event.dest_path)

    def on_created(self, event):
        super(MyEventHandler, self).on_created(event)
        what = 'directory' if event.is_directory else 'file'
        info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super(MyEventHandler, self).on_deleted(event)
        what = 'directory' if event.is_directory else 'file'
        info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(MyEventHandler, self).on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        info("Modified %s: %s", what, event.src_path)
        event_path = Path(event.src_path)
        home = Path(environ.get('HOME'))
        buff = home / 'buffer'
        script_dir = home / 'code' / 'pyrep' / 'coderunner' / 'runner.py'
        if event_path != str(script_dir) and event_path.is_file():
            with buff.open("w") as buf:
                print(python(str(event_path)))
                python(str(event_path), _out=buf)
            socket_path = environ.get("NVIM_LISTEN_ADDRESS")
            nvim = attach('socket', path=socket_path)
            nvim.command('vertical botright pedit ' +  str(buff))


def main():
    """watch a specific directory, logging changes and
    running python scripts when they are written to disk"""
    basicConfig(level=INFO,
                format='%(asctime)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
    watched_dir = Path(environ.get('HOME')) / 'code' / 'pyrep' / 'coderunner'
    handler = MyEventHandler()
    obs = InotifyObserver()
    obs.schedule(handler, str(watched_dir), False)
    try:
        obs.start()
        while True:
            sleep(1)
    finally:
        obs.stop()
    obs.join()


if __name__ == '__main__':
    main()
