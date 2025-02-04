# Deduplicate Lines Script

This script removes duplicate lines from either a specified file or user input entered through the terminal.

## How It Works

- If a file path is provided as a command-line argument, the script processes the file and writes a deduplicated version to `result`.
- If no file path is provided, the script prompts the user to enter lines manually. After pressing `Ctrl+C`, it saves unique lines to `result`.

## Usage

### Removing Duplicates from a File
```sh
python script.py <file_path>
```
- `<file_path>`: The path to the file containing lines to be deduplicated.
- Output is saved in a file named `result`.

### Removing Duplicates from Terminal Input
```sh
python script.py
```
- Enter lines one by one.
- Press `Ctrl+C` to stop input and save unique lines to `result`.

## Notes
- The script ensures that the order of the first occurrence of each unique line is preserved.
- If the file does not exist, an error message is displayed.

## Example

### File Input
#### Input (`input.txt`)
```
apple
banana
apple
orange
banana
```
#### Command
```sh
python script.py input.txt
```
#### Output (`result`)
```
apple
banana
orange
```

### Terminal Input
#### User Input
```
hello
world
hello
python
```
(Press `Ctrl+C` to stop)

#### Output (`result`)
```
hello
world
python
```

