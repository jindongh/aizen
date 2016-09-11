#!/bin/env python

import sys
import os,io
from bs4 import BeautifulSoup


def main():
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    for f in os.listdir(input_folder):
        html = io.open('%s/%s' % (input_folder,f), 'r', encoding='utf8').read()
        soap=BeautifulSoup(html)
        text=soap.get_text()
        io.open('%s/%s' % (output_folder, f), 'w', encoding='utf8').write(text)
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Usage: %s <input folder> <output folder>' % sys.argv[0])
    main()
