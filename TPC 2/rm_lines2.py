import sys
import argparse

def filter_rep_lines(input_stream, result, space_flag, comment_flag):
    set_lines = set()
    with open(result, 'w') as outfile:
        for line in input_stream:
            new_line = line.rstrip('\n')
            if not space_flag:
                new_line = new_line.strip()
            if new_line == '' and comment_flag:
                outfile.write('#\n')
            elif new_line not in set_lines:
                outfile.write(line)
                set_lines.add(new_line)

def main():
    parser = argparse.ArgumentParser(description="Filter equal lines from input.")
    parser.add_argument('input_file', nargs='?', help="Input file or read from terminal if not provided")
    parser.add_argument('-s', action='store_true', help="Preserve whitespace when checking for duplicates")
    parser.add_argument('-p', action='store_true', help="Comment empty lines")
    args = parser.parse_args()

    result = 'output.txt'
    
    if args.input_file:
        with open(args.input_file, 'r') as file:
            filter_rep_lines(file, result, args.spaces, args.comment)
    else:
        print("Enter the text (Ctrl-D to end input):")
        filter_rep_lines(sys.stdin, result, args.spaces, args.comment)

if __name__ == "__main__":
    main()