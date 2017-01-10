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
        """pass logfile to be opened and handler to flush writing the file"""
        super(MyEventHandler, self).__init__()
        self.run_log = Logger('Runs')
        self.fs_log = Logger('Files')
        socket_path = environ.get("NVIM_LISTEN_ADDRESS")
        self.nvim = attach('socket', path=socket_path)
        self.log_file = logfile
        self.run_handler = run_handler

    def on_moved(self, event):
        """called when a file or folder is moved"""
        super(MyEventHandler, self).on_moved(event)
        what = 'directory' if event.is_directory else 'file'
        log_msg = "Moved {}: from {} to {}".format(what, event.src_path, event.dest_path)
        self.fs_log.info(log_msg)

    def on_created(self, event):
        """called on creation of a file or folder"""
        super(MyEventHandler, self).on_created(event)
        what = 'directory' if event.is_directory else 'file'
        self.fs_log.info("Created {}: {}".format(what, event.src_path))

    def on_deleted(self, event):
        """called on deletion of a file or folder"""
        super(MyEventHandler, self).on_deleted(event)
        what = 'directory' if event.is_directory else 'file'
        self.fs_log.info("Deleted {}: {}".format(what, event.src_path))

    def on_modified(self, event):
        """when a file is modified the event is logged and appended to a separate file
        Then the script is run through python and the output is (over)written to self.log_file
        and appended to the file handled by the info handler"""
        super(MyEventHandler, self).on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        self.fs_log.info("Modified {}: {}".format(what, event.src_path))
        event_path = Path(event.src_path) # using plain src_path gives nonexistent path
        if event_path.is_file():
            in_file = str(event_path)
            out_str = python(in_file)
            self.run_log.notice('Output:\n{}'.format(out_str))
            self.run_handler.close()
            self.nvim.command('pedit ' + self.log_file)


def main():
    """watch a specific directory, logging changes and
    running python scripts when they are written to disk"""
    home_dir = Path(environ.get('HOME'))
    run_logfile = home_dir / 'pyrun.log'
    watchdog_logfile = home_dir / 'pydir.log'
    run_log = FileHandler(str(run_logfile), level='NOTICE', bubble=True, mode='w', delay=True)
    file_log = FileHandler(str(watchdog_logfile), level='INFO', bubble=True)
    with run_log.applicationbound():
        with file_log.applicationbound():
            watched_dir = home_dir / 'code' / 'pyrep' / 'coderunner' / 'snippets'
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
