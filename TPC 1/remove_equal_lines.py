import os
import sys
import signal

def remove_equal_lines_from_file(file_path):
    set_of_lines = set()
    with open(file_path, 'r') as file_read:
        lines = file_read.readlines()
    with open('result', 'w') as file_write:
        for line in lines:
            if line not in set_of_lines:
                file_write.write(line)
                set_of_lines.add(line)

def remove_equal_lines_from_terminal():
    set_of_lines = set()
    lines = []
    print("Enter lines (press Ctrl+C to finish):")
    try:
        while True:
            line = input()
            #print(line)
            lines.append(line)
    except KeyboardInterrupt:
        print("\nFinished reading input.")

    with open('result', 'w') as file_write:
       for line in lines:
           if line not in set_of_lines:
               file_write.write(line + "\n")
               set_of_lines.add(line)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            print('File does not exist')
            sys.exit(1)
        remove_equal_lines_from_file(file_path)
    else:
        remove_equal_lines_from_terminal()