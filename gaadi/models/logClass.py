__author__ = 'Varna Nair'

import logging
import subprocess


class Log:
    """
    Log class initializes multiple logger instances based on the logging levels

    To use the logClass,
    1.from logging import Log
    2.Initialize Log class by passing the path
    Eg: Log('D:\\')# for Windows
    Eg: Log('/var/logs/temp')# for Linux
    """
    warn = logging.getLogger('warn')
    criti = logging.getLogger('criti')
    error = logging.getLogger('error')
    info = logging.getLogger('info')
    debug = logging.getLogger('debug')

    files = {'warn': 'WARNING.logs', 'criti': 'CRITICAL.logs', 'error': 'ERROR.logs', 'info': 'INFO.logs',
             'debug': 'DEBUG.logs'}

    def __init__(self):
        """
        Initializes logs class by providing the path where
        logs files has to be created.
        :rtype : None
        :param path: Path is where logs files have to be created
        :type path: string
        """

    def set_logger(self, path):
        """
        Initializes logs class by providing the path where
        logs files has to be created.
        :rtype : None
        :param path: Path is where logs files have to be created
        :type path: string
        """
        files = self.files
        # keys = files.keys()
        for (key, value) in files.iteritems():
            self.setup_logger(key, path + '\\' + value)

    def setup_logger(self, logger_name, log_file, level=logging.WARNING):
        """
        Creates the logs files based on the loggers
        and each logger's level is set as logging.WARNING by default

        :param logger_name: logger_name is the Logger created for logging
        :param log_file: log_file contains path and file name to be created
        :param level: level is the debugging level which is set for each logger

        """
        l = logging.getLogger(logger_name)
        if len(l.handlers) == 0:
            formatter = logging.Formatter('%(asctime)s [%(levelname)-5.5s]-> %(message)s')
            fileHandler = logging.FileHandler(log_file, mode='a')
            subprocess.call(['chmod', '0777', log_file])
            fileHandler.setFormatter(formatter)
            # streamHandler = logging.StreamHandler()
            # streamHandler.setFormatter(formatter)

            l.setLevel(level)
            l.addHandler(fileHandler)
            # l.addHandler(streamHandler)


    def set_level(self, logger_name, level):
        """
        Sets the debugging level of info & debug loggers
        as logging.INFO & logging.DEBUG

        """
        logger = logging.getLogger(logger_name)
        if (logger_name == 'info'):
            logger.setLevel(logging.INFO)
        elif (logger_name == 'debug'):
            logger.setLevel(logging.DEBUG)
        else:
            if (level == 1):
                logger.setLevel(logging.INFO)
            elif (level == 2):
                logger.setLevel(logging.DEBUG)
            else:
                logger.setLevel(logging.INFO)
                logger.setLevel(logging.DEBUG)


    def get_logger(self, logger_name):
        result = logging.getLogger(str(logger_name))
        return result
