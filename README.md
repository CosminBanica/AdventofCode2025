# Advent of code 2025
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

### Usage
```python main.py <day> [-t|--test] [-g|--generate] [-n|--name <name>] [-h|--help]```

#### Explanation
* ```<day>``` is the day to run
* ```-t``` or ```--test``` runs the small test input instead of the big input
* ```-g``` or ```--generate``` generates files for the day, if they don't exist
* ```-n``` or ```--name``` sets the name of the problem for the day, in the newly generated files
* ```-h``` or ```--help``` shows the help message

#### Examples
* ```python main.py 1 -g -n "Trebuchet?!"```
* ```python main.py 4 -t```