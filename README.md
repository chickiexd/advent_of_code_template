# Advent of Code Setup Script

This repository contains a python script to automatically set up directories and files for participating in the Advent of Code challenges in either Go or Python. The script streamlines the creation of a standardized folder structure and initial files for each day's challenge, allowing you to focus on solving the puzzles.

Credit for the amazing advent of code goes to [Eric Wastl](https://adventofcode.com/)

**Don't forget to add input.py, input.txt, problem_1.md and problem_2.md to your .gitignore to abide by the wishes of Eric Wastl
and maybe give me a star if u enjoy using this :)**

## Features

- Automatically creates a new directory for the specified day.
- Generates template files for the selected programming language (Go or Python).
- Supports adding both Part 1 and Part 2 solution template files.
- Easy to customize template files for your coding style.
- Downloads and creates your personal input.txt
- Downloads and creates problem_1.md with the first problem and creates a empty file problem_2.md for the second problem

## Prerequisites

Before you start using this script, ensure you have the following installed on your system:
- Python 3.x (for running the script and setting up Python challenges)
- Pip to install the required packages
- Go (if setting up challenges in Go)
- Git (optional, for version control)

## Getting Started

Clone this repository to your local machine using:
 
```
git clone https://github.com/chickiexd/advent_of_code_template.git
cd advent_of_code_template
pip install -r requirements.txt
```

## Usage

To use the script, navigate to the cloned directory and open create_new_day.py set the global variables to your needs.

- **LANG** is the language you want to use
- **DAY** is the day u want to create if u dont want to use cmd line arguments
- **PARSE_DAY** set to true if u want to pass the day as cmd line argumentn
- **PROJECT_DIR** the root directory of your advent of code directory

If u want to create the input.txt file with your personal input from advent of code u need to provide the session cookie as environment variable.

```
COOKIE="theactualcookievalue"
```

```
python create_new_day.py <day_number>
```

Replace `<day_number>` with the day of the challenge (e.g., 01, 02, 03, ...), remember to always use 2 digits even for single digit days.



### Examples

Setting up Day 1 for Python:

```
python setup_day.py 01
```

## Structure

After running the script, you will find the following structure in your project directory:
```
/project_dir/
/day<XX>/
- main_part_1.<go|py>
- main_part_2.<go|py>
- input.<go|py>
- problem_1.md
- problem_2.md
```

`<XX>` is the day's number, and the file extensions depend on the chosen language.

## Customization

Feel free to modify the template files located in the `day_00_template` directory to suit your coding preferences.

## Contributing

Contributions to improve this script or extend its functionalities are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.