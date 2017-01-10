""" run a python file with logging and output"""
from os import environ
from time import sleep
from pathlib import Path

from sh import python  # pylint: disable=no-name-in-module
from neovim import attach
from logbook import FileHandler, Logger
from watchdog.events import FileSystemEventHandler
from watchdog.observers.inotify import InotifyObserver


class MyEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def __init__(self, logfile, run_handler):
        super(MyEventHandler, self).__init__()
        self.run_log = Logger('Runs')
        self.file_log = Logger('Files')
        socket_path = environ.get("NVIM_LISTEN_ADDRESS")
        self.nvim = attach('socket', path=socket_path)
        self.log_file = logfile
        self.run_handler = run_handler

    def on_moved(self, event):
        super(MyEventHandler, self).on_moved(event)
        what = 'directory' if event.is_directory else 'file'
        self.file_log.info("Moved {}: from {} to {}".format(what, event.src_path, event.dest_path))

    def on_created(self, event):
        super(MyEventHandler, self).on_created(event)
        what = 'directory' if event.is_directory else 'file'
        self.file_log.info("Created {}: {}".format(what, event.src_path))

    def on_deleted(self, event):
        super(MyEventHandler, self).on_deleted(event)
        what = 'directory' if event.is_directory else 'file'
        self.file_log.info("Deleted {}: {}".format(what, event.src_path))

    def on_modified(self, event):
        super(MyEventHandler, self).on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        self.file_log.info("Modified {}: {}".format(what, event.src_path))
        event_path = Path(event.src_path) # using plain src_path gives nonexistent path
        if event_path.is_file():
            self.run_log.notice('Output:\n{}'.format(python(str(event_path))))
            self.run_handler.close()
            self.nvim.command('pedit ' + self.log_file)


def main():
    """watch a specific directory, logging changes and
    running python scripts when they are written to disk"""
    run_logfile = environ.get('HOME')+'/pyrun.log'
    watchdog_logfile = environ.get('HOME')+'/pydir.log'
    run_log = FileHandler(run_logfile, level='NOTICE', bubble=True, mode='w', delay=True)
    file_log = FileHandler(watchdog_logfile, level='INFO', bubble=True)
    with run_log.applicationbound():
        with file_log.applicationbound():
            watched_dir = Path(environ.get('HOME')) / 'code' / 'pyrep' / 'coderunner' / 'snippets'
            handler = MyEventHandler(run_logfile, run_log)
            obs = InotifyObserver()
            obs.schedule(handler, str(watched_dir), False)
            obs.start()
            try:
                while True:
                    sleep(1)
            except: #  pylint: disable=bare-except
                obs.stop()
            obs.join()


if __name__ == '__main__':
    main()
