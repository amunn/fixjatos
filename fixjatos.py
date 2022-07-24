#!/usr/local/opt/python/libexec/bin/python
# This program converts the output of JATOS combined results from
# jsPsych JSON output into valid JSON that can be imported using
# jsonlite in R
#
# Copyright 2022 by Alan Munn
#
# Released under MIT License
#
#

import argparse
import sys
import pathlib

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [FILE]...",
        description="Convert JATOs combined results to valid JSON. Input file is assumed to be FILE.txt, output file will be FILE.json"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 0.5"
    )

    parser.add_argument('file', nargs=1)

    return parser

def fixjatos() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    for file in args.file:
        try: process_file(file)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{parser.prog}: {file}: {err.strerror}", file=sys.stderr)


def process_file(input_file:str) -> None:

    output_file = pathlib.Path(input_file).with_suffix('.json')
    with open(input_file) as infile:
        line_count = sum(1 for line in infile)
    with open(input_file,'r') as infile, open(output_file,'w') as outfile:
        line_no = 1
        outfile.write("[")
        for item in infile:
            if line_no < line_count:
                outfile.write(item.strip("[]\n") + ",")
                line_no += 1
            else:
                outfile.write(item.strip("[]\n"))
        outfile.write("]")

if __name__ == "__main__":
    fixjatos()
