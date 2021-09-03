#!/usr/bin/env python3

'''
This script generates a bed file with motifs extracted from a fasta file.
It requires an input file in fasta format, output file name and list of motifs.

Example:

$ ./motif2bed.py -i input.fa -o motifs.bed -m TTAGGG TCAGGG TTTTTAAAGGGGCC

'''

import argparse
import sys
import time

import pandas as pd
from Bio import SeqIO

from pycmri.utils import *

if __name__ == "__main__":

    # store start time for benchmarking
    start_time = pd.to_datetime(time.time(), unit="s")

    # setup logger
    root_logger, log_formatter = get_cmri_logger()

    # setup arguments
    parser = argparse.ArgumentParser(description='Generates a bed file with motifs extracted from a fasta file.',
                                     epilog=epilog_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--silent', action='store_true', help='Starts in silent mode, no message will be output.')
    parser.add_argument('-d', '--debug', action='store_true', help='Shows debug info')
    parser.add_argument('-i', '--input', type=str, help='Input fasta file', default="input.fa", required=True)
    parser.add_argument('-o', '--output', type=str, help='Output bed file', default="output.bed", required=True)
    parser.add_argument('-m', '--motifs', type=str, nargs='+', help='List of motifs', required=True)

    # parse arguments and set logger
    args = parser.parse_args()
    consoleHandler = logging.StreamHandler(sys.stdout)

    if args.debug:
        root_logger.setLevel(logging.DEBUG)

    if args.silent:
        consoleHandler.setLevel(logging.ERROR)

    consoleHandler.setFormatter(log_formatter)
    root_logger.addHandler(consoleHandler)

    print_cmri_welcome("motif2bed")

    logging.info("Input file: %s" % (args.input))
    logging.info("Output file: %s" % (args.output))
    logging.info("Motifs: %s" % (",".join(args.motifs)))
    count = 0

    if file_exists(args.input, must_exist=True):
        with open(args.output, 'w') as output_file:
            for m in args.motifs:
                len_m=len(m)
                with open(args.input, 'r') as input_file:
                    index=0
                    for i, item in enumerate(SeqIO.parse(input_file, 'fasta')):
                        seq = str(item.seq).upper()
                        len_seq = len(seq)
                        while index < len_seq:
                            i=seq.find(m,index)
                            if i < 0:
                                break
                            index=i+len_m
                            output_file.write("%s\t%d\t%d\t%s\n"%(item.name,i,index,m))
                            count+=1



    logging.info("Total motifs: %d", count)
    logging.info("Total computation time: %s", str(pd.to_datetime(time.time(), unit="s") - start_time))
