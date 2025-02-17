# Duplicate Line Remover

## Overview
This script processes an input file (or standard input) to remove duplicate lines and writes the cleaned output to `result.txt`. It includes options to preserve whitespace and mark duplicate empty lines with `#`.

## Features
- Removes duplicate lines while preserving the first occurrence.
- Supports optional whitespace sensitivity.
- Allows replacing duplicate empty lines with `#`.
- Works with both file input and manual text entry via standard input.

## Usage
Run the script using Python:

```sh
python script.py [input_file] [-s] [-p]
```

### Arguments
- `input_file` (optional): The file to process. If not provided, the script reads from standard input.
- `-s`: Preserve leading and trailing spaces in line comparison.
- `-p`: Replace duplicate empty lines with `#`.

### Example Commands
#### Remove duplicate lines:
```sh
python script.py input.txt
```
This removes all duplicate lines while ignoring extra spaces at the beginning or end of lines.

#### Preserve whitespace when checking for duplicates:
```sh
python script.py input.txt -s
```
This treats lines with different leading/trailing spaces as unique (e.g., `" hello"` and `"hello"` would be considered different).

#### Replace duplicate empty lines with `#`:
```sh
python script.py input.txt -p
```
This replaces duplicate blank lines with `#` instead of removing them.

#### Combine options:
```sh
python script.py input.txt -s -p
```
This keeps whitespace differences and replaces duplicate empty lines with `#`.

## Output
- The cleaned output is saved in `output.txt` in the same directory.
- If run without an input file, the script will prompt for text input and terminate upon pressing `Ctrl+D` (Linux/macOS) or `Ctrl+Z` (Windows).

## Notes
- The script processes input line by line, making it efficient for large files.
- If no input file is provided, the script waits for manual text entry.

