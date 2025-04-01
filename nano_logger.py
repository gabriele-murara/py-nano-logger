import os
import logging
import tempfile


class NanoLogger:

    def __init__(self, **kwargs):
        format_tpl = '%(asctime)s %(process)d: %(levelname)s '
        format_tpl += '[%(name)s:%(module)s:%(funcName)s:%(lineno)d] '
        format_tpl += '- %(message)s'

        self.__name = kwargs.get("name", 'nano_logger')
        self.__log_file_path = kwargs.get("log_file_path", None)
        self.__log_level = kwargs.get("log_level", logging.DEBUG)
        self.__write_to_console = kwargs.get("write_to_console", False)
        self.__format = kwargs.get("format", format_tpl)

        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__log_level)

        if not self.__log_file_path:
            tmp_path = tempfile.gettempdir()
            self.__log_file_path = os.path.join(
                tmp_path, "{}.log".format(self.__name)
            )

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

        self.__logger.handlers = []

        if not is_file_writable:
            msg = "Log file {} is not writable. Check your .env file or "
            msg += "set the environment variable LOG_FILE_PATH. Log "
            msg += "messages will be written to the standard output"
            print(msg.format(self.__log_file_path))
            self.__write_to_console = True
        else:
            fh = logging.FileHandler(self.__log_file_path)
            fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter(self.__format)
            fh.setFormatter(formatter)
            self.__logger.addHandler(fh)

        if self.__write_to_console:
            console = logging.StreamHandler()
            console_format_tpl = '%(asctime)s [%(levelname)s] - %(message)s'
            console_formatter = logging.Formatter(console_format_tpl)
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
