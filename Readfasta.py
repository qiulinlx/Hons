#####################
# code to read FASTA file
#####################
import sys, re
import os
import pandas as pd
import numpy as np
os.chdir("/home/panda/Documents/Honours Thesis/Dataset")

def read_fasta_file(filename):
    """
    Reads a FASTA file and returns a dictionary containing the sequence information.
    """
    sequences = {}
    with open(filename, 'r') as f:
        sequence = ''
        header = ''
        for line in f:
            line = line.rstrip()
            if line.startswith('>'):
                if sequence:
                    sequences[header] = sequence
                    sequence = ''
                header = line[1:]
            else:
                sequence += line
        sequences[header] = sequence
    return sequences

f=read_fasta_file('Swissprot.fasta')

def get_fasta_headers(filename):
    """
    Reads a FASTA file and returns a list of all the headers.
    """
    headers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line.startswith('>'):
                headers.append(line[1:])
    return headers

headers = get_fasta_headers('Swissprot.fasta')

h=[]

for header in headers:
        head=header.split()
        a=head[0]
        #print(a)
        h.append(a)

print(h)

