import sys
import argparse

def filter_rep_lines(input_stream, result, space_flag, comment_flag):
    set_lines = set()
    with open(result, 'w') as outfile:
        for line in input_stream:
            new_line = line.rstrip('\n')
            if not space_flag:
                new_line = new_line.strip()
            if new_line not in set_lines:
                if comment_flag and new_line == '':
                    outfile.write('#\n')
                else:
                    outfile.write(line)
                set_lines.add(new_line)

def main():
    parse = argparse.ArgumentParser(description="Filter equal lines from input.")
    parse.add_argument('input_file', nargs='?', help="Input file or read from terminal if not provided")
    parse.add_argument('-s',  action='store_true', help="Preserve whitespace when checking for duplicates")
    parse.add_argument('-p',  action='store_true', help="Comment empty lines")
    args = parse.parse_args()

    result = 'output.txt'
    
    if args.input_file:
        with open(args.input_file, 'r') as infile:
            filter_rep_lines(infile, result, args.spaces, args.comment)
    else:
        print("Enter lines (press Ctrl+C to finish):")
        filter_rep_lines(sys.stdin, result, args.spaces, args.comment)

if __name__ == "__main__":
    main()