import os
import logging
import tempfile

from boolifyer.booleans import Booleans


class NanoLogger:

    def __init__(self, **kwargs):
        # The default template used for writing log messages to a file
        format_tpl = '%(asctime)s %(process)d: %(levelname)s '
        format_tpl += '[%(name)s:%(module)s:%(funcName)s:%(lineno)d] '
        format_tpl += '- %(message)s'

        # Retrieves the logger's name from the constructor arguments or from
        # the "NANO_LOGGER_NAME" environment variable.
        # Default is 'nano_logger'.
        self.__name = kwargs.get(
            "name",
            os.getenv('NANO_LOGGER_NAME', default='nano_logger')
        )

        # Retrieves the file path where log messages will be written from the
        # constructor arguments or from the "NANO_LOGGER_FILE_PATH" environment
        # variable. Default is None.
        self.__log_file_path = kwargs.get(
            "log_file_path",
            os.getenv('NANO_LOGGER_FILE_PATH', default=None)
        )

        # Retrieves the log level from the constructor arguments or from the
        # "NANO_LOGGER_LOG_LEVEL" environment variable. Default is 'DEBUG'.
        self.__log_level = kwargs.get(
            "log_level",
            os.getenv('NANO_LOGGER_LOG_LEVEL', default=logging.DEBUG)
        )

        # Retrieves the flag for writing to standard output from the
        # constructor arguments or from the "NANO_LOGGER_WRITE_TO_CONSOLE"
        # environment variable.
        # The environment variable can be a string, and values considered True
        # are those listed in boolifyer's TRUE_VALUES array. Default is False.
        write_to_console = Booleans.is_true(
            os.getenv('NANO_LOGGER_WRITE_TO_CONSOLE', default=False)
        )
        self.__write_to_console = kwargs.get(
            "write_to_console", write_to_console
        )

        # Retrieves the log message format template from the constructor
        # arguments or from the "NANO_LOGGER_FORMAT" environment variable.
        # Default is format_tpl.
        self.__format = kwargs.get(
            "format",
            os.getenv('NANO_LOGGER_FORMAT', default=format_tpl)
        )

        # Retrieves the flag for suppressing warnings from the constructor
        # arguments or from the "NANO_LOGGER_SUPPRESS_WARNINGS" environment
        # variable.
        # The environment variable can be a string, and values considered True
        # are those listed in boolifyer's TRUE_VALUES array. Default is False.
        suppress_warnings = Booleans.is_true(os.getenv(
            'NANO_LOGGER_SUPPRESS_WARNINGS', default=False
        ))
        self.__suppress_warnings = kwargs.get(
            "suppress_warnings",
            suppress_warnings
        )

        # Init the internal logger
        self.__logger = logging.getLogger(self.__name)
        # Set the log level to the internal logger
        self.__logger.setLevel(self.__log_level)

        # If no log file path is specified, checks the flag for writing to
        # standard output.
        if not self.__log_file_path:
            # If the flag for writing to standard output is not set, a log
            # file is created in the system's temporary directory.
            if not self.__write_to_console:
                tmp_path = tempfile.gettempdir()
                self.__log_file_path = os.path.join(
                    tmp_path, "{}.log".format(self.__name)
                )

            # If neither the flag for writing to standard output nor the flag
            # for suppressing warnings is set, a warning is written to
            # standard output.
            if not self.__write_to_console and not self.__suppress_warnings:
                msg = "[ WARNING ]: no 'NANO_LOGGER_FILE_PATH' specified. "
                msg += "Fallback to '{}'. Use 'NANO_LOGGER_SUPPRESS_WARNINGS' "
                msg += "env variable for suppress this warning"
                print(msg.format(self.__log_file_path))

        # Clears the handlers of the internal logger.
        self.__logger.handlers = []

        # If the file path is set, checks whether the file is writable.
        if self.__log_file_path:
            try:
                file = open(self.__log_file_path, "a")
                is_file_writable = file.writable()
            except FileNotFoundError as fe:
                is_file_writable = False
                msg = "A {} error occurred. Details: {}".format(
                    fe.__class__.__name__, str(fe)
                )
                print(msg)
            except Exception as e:
                is_file_writable = False
                msg = "A {} error occurred. Details: {}".format(
                    e.__class__.__name__, str(e)
                )
                print(msg)

            # If the file is not writable, forces log messages to be written
            # to standard output.
            if not is_file_writable:
                msg = "[ WARNING ] Log file {} is not writable. Check your "
                msg += ".env file or set the environment variable "
                msg += "LOG_FILE_PATH. Log messages will be written to the "
                msg += "standard output"
                print(msg.format(self.__log_file_path))
                self.__write_to_console = True
            # Otherwise, creates a FileHandler using the specified path, level
            # and format.
            else:
                fh = logging.FileHandler(self.__log_file_path)
                fh.setLevel(logging.DEBUG)

                formatter = logging.Formatter(self.__format)
                fh.setFormatter(formatter)
                self.__logger.addHandler(fh)

        # If the flag for writing to standard output is set, adds a
        # StreamHandler to the logger.
        if self.__write_to_console:
            console = logging.StreamHandler()
            console_formatter = logging.Formatter(self.__format)
            console.setFormatter(console_formatter)
            self.__logger.addHandler(console)

    def is_verbose(self):
        return self.__write_to_console

    def debug(self, msg):
        self.__logger.debug(msg, stacklevel=2)

    def info(self, msg):
        self.__logger.info(msg, stacklevel=2)

    def warning(self, msg):
        self.__logger.warning(msg, stacklevel=2)

    def warn(self, msg):
        self.__logger.warning(msg, stacklevel=2)

    def error(self, msg):
        self.__logger.error(msg, stacklevel=2)

    def critical(self, msg):
        self.__logger.critical(msg, stacklevel=2)

    @property
    def name(self):
        return self.__name

    @property
    def log_file_path(self):
        return self.__log_file_path

    @property
    def log_level(self):
        return self.__log_level

    @property
    def format(self):
        return self.__format

    @property
    def suppress_warnings(self):
        return self.__suppress_warnings
