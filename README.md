# NanoLogger

NanoLogger is a simple and efficient logging library that allows you to quickly set up and configure logging for your projects.

## Installation

You can install NanoLogger via pip:

```sh
pip install nano-logger
```

## Usage

To get started, instantiate the logger and use it with the default settings:

```python
from nano_logger.nano_logger import NanoLogger

logger = NanoLogger()
logger.debug("This is my first debug message")
```

### Default Settings

NanoLogger comes with the following default values:

- **name**: `'nano_logger'`
- **log_level**: `'DEBUG'`
- **log_file_path**: `'/tmp/nano_logger.log'`
- **write_to_console**: `False`
- **format**: `'%(asctime)s %(process)d: %(levelname)s [%(name)s:%(module)s:%(funcName)s:%(lineno)d] - %(message)s'`

### Customizing the Logger

You can override the default values by passing parameters to the constructor:

```python
logger = NanoLogger(
    name='my_custom_logger',
    log_level='WARNING',
    log_file_path='/tmp/custom_log.log',
    write_to_console=True,
    format="%(message)s"
)
```

Alternatively, you can configure NanoLogger using environment variables:

```sh
export NANO_LOGGER_NAME=nano_logger_from_env
export NANO_LOGGER_FILE_PATH=/var/log/my-project/nano_logger_from_env.log
export NANO_LOGGER_LOG_LEVEL=INFO
export NANO_LOGGER_WRITE_TO_CONSOLE=true
export NANO_LOGGER_FORMAT="%(asctime)s %(process)d: %(levelname)s - %(message)s"
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! If you’d like to improve NanoLogger, feel free to open an issue or submit a pull request.

## Author

Developed by Gabriele Murara

## Contact

For any questions or support, please reach out to [gabriele@murara.computer].

