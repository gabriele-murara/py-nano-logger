# NanoLogger

**Minimal setup. Maximum clarity.**  
A lightweight logger that works out of the box, configurable via environment variables or constructor arguments, and ready to handle log messages in a file, console, or both.

## 📖 Overview

A simple yet powerful logger that lets you write log messages with custom levels and formats, either to a single file, standard output, or both.  
It can be configured transparently via environment variables or directly through the constructor.  

Perfect for projects that need **minimal logging setup** but want to start handling log messages immediately, with **just a few easy steps**.


## 📦 Installation

### Install in development mode

```bash
git clone https://github.com/gabriele-murara/py-nano-logger.git
```

### Build a wheel

```bash
bash build.sh
pip install dist/nano_logger-<version>-py3-none-any.whl
```

### Install for use in another project

```bash
pip install --extra-index-url https://pip.murara.computer \
            --trusted-host pip.murara.computer \
            nano-logger
```

### Adding to requirements.txt

```
--index-url https://pypi.org/simple
--extra-index-url https://pip.murara.computer
--trusted-host pip.murara.computer

nano-logger==1.1.0
```

---

## ⚙️ Requirements

- Python 3.8+

---

## 📦 Dependencies

This project depends on:

- `boolifyer==1.0.0` – used to convert string values from environment variables into booleans.

### ℹ️ Installation Note

`nano-logger` depends on `boolifyer==1.0.0`.  

- By default, `boolifyer` is installed from the project's **public personal PyPI repository**, which is fully accessible here : [https://pip.murara.computer/boolifyer/](https://pip.murara.computer/boolifyer/).  
- If you prefer not to install from a non-official index, you can also clone `boolifyer` from its **GitHub repository** and install it manually.  

This ensures that `nano-logger` works correctly regardless of your preferred installation method.

---

## 🛠️ Usage

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
- **suppress_warnings**: `False`

### Customizing the Logger

You can override the default values by passing parameters to the constructor:

```python
from nano_logger.nano_logger import NanoLogger

logger = NanoLogger(
    name='my_custom_logger',
    log_level='WARNING',
    log_file_path='/tmp/custom_log.log',
    write_to_console=True,
    format="%(message)s",
    suppress_warnings=True
)
```

Alternatively, you can configure NanoLogger using environment variables:

```sh
export NANO_LOGGER_NAME=nano_logger_from_env
export NANO_LOGGER_LOG_LEVEL=/var/log/my-project/nano_logger_from_env.log
export NANO_LOGGER_LOG_LEVEL=INFO
export NANO_LOGGER_WRITE_TO_CONSOLE=true
export NANO_LOGGER_FORMAT="%(asctime)s %(process)d: %(levelname)s - %(message)s"
export NANO_LOGGER_SUPPRESS_WARNINGS=true
```

### 🔢 Environment Variables Defaults

| Environment Variable               | Default Value                                                                                          | Description |
|-----------------------------------|--------------------------------------------------------------------------------------------------------|------------|
| `NANO_LOGGER_NAME`              | `'nano_logger'`                                                                                        | The logger’s name. |
| `NANO_LOGGER_LOG_LEVEL`         | `'DEBUG'`                                                                                              | Logging level. |
| `NANO_LOGGER_LOG_FILE_PATH`     | `'/tmp/nano_logger.log'`                                                                               | Path to the log file. |
| `NANO_LOGGER_WRITE_TO_CONSOLE`  | `False`                                                                                                | Whether to write logs to the console. |
| `NANO_LOGGER_FORMAT`            | `'%(asctime)s %(process)d: %(levelname)s [%(name)s:%(module)s:%(funcName)s:%(lineno)d] - %(message)s'` | Log message format. |
| `NANO_LOGGER_SUPPRESS_WARNINGS` | `False`                                                                                                | Whether to suppress warnings from the logger. |

### 🔢 Environment Variables Behavior

When creating an instance of the logger, if no `log_file_path` is provided:

* If `write_to_console` is set to `True`, **no file will be created** and all output will be written to the console.
* Otherwise, a file at `/tmp/nano_logger.log` will be created, and a **warning will be issued** indicating that the default file is being used.

To suppress this warning, set the `suppress_warnings` flag to `True`.

---

## ⚖️ License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve NanoLogger, feel free to open an issue or submit a pull request.

---

## 👤 Author

Developed by Gabriele Murara

---

## ✉️ Contact

For any questions or support, please reach out to [gabriele@murara.computer].

---