# KIRACRO-IMPROVED  
The best Da Hood macro... or is it?

---

## Table of Contents  
- [Supported Platforms](#supported-platforms)  
- [Installation](#installation)  
  - [Windows](#windows)  
    - [Download the Binary](#option-1-download-the-binary)  
    - [Install Using pip](#option-2-install-using-pip)  
  - [Linux](#linux)  
    - [Download the Binary](#option-1-download-the-binary-1)  
    - [Install Using pip](#option-2-install-using-pip-1)  
- [Requirements](#requirements)  
- [Build Instructions](#build-instructions)  
- [Usage](#usage)  
- [License](#license)  

---

## Supported Platforms  
| Platform | Status         |  
| -------- | -------------- |  
| Windows  | ✅ Supported   |  
| Linux    | ✅ Supported   |  
| macOS    | ❌ Unsupported |  

---

## Installation  

### Windows  
#### Option 1: Download the Binary  
- Visit the [latest release page](https://github.com/noktilumo/kiracro-improved/releases/latest)  
- Download the Windows binary and run it directly  

#### Option 2: Install Using pip  
- Download the `.whl` file from the [latest release](https://github.com/noktilumo/kiracro-improved/releases/latest)  
- Install it using pip:  
```bash
pip install <name-of-the.whl-file>
```

---

### Linux  
#### Option 1: Download the Binary  
- Visit the [latest release page](https://github.com/noktilumo/kiracro-improved/releases/latest)  
- Download the Linux binary and run it directly  

#### Option 2: Install Using pip  
- Download the `.whl` file from the [latest release](https://github.com/noktilumo/kiracro-improved/releases/latest)  
- Install it using pip:  
```bash
pip3 install <name-of-the.whl-file>
```

---

## Requirements  

To build or run KIRACRO-IMPROVED from source, you’ll need:

- [Python 3.8+](https://www.python.org/downloads/) (Recommended: Python 3.10 or newer)  
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management and building)  
- [Git](https://git-scm.com/downloads) (optional, for cloning the repo)  

---

## Build Instructions  

### Universal (Windows/Linux/macOS)  
```bash
git clone https://github.com/noktilumo/kiracro-improved.git  
cd kiracro-improved  
poetry install  
poetry build  
```

This will install all dependencies and build the project into a distributable package located in the `dist/` folder.

Alternatively you can test the script by running
```bash
poetry run poetry-runner
````
---

## Usage  

- Run the program with `--help` to see available flags  
- Use `--holdable` if you prefer holding the macro key (default is toggle)  

### Keybinds  
| Key      | Action |
| -------- | ------ |
| Esc      | Close  |
| Q        | Macro  |

---

## License  
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute just give credit where it's due.

---
