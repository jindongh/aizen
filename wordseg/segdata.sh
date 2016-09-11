#!/bin/bash
set -x
if [ "$1" == "" -o "$2" == "" ];then
    echo "Usage $0 <input folder> <output folder>" && exit 1
fi
INPUT=$1
OUTPUT=$2

./wordseg/stanford-segmenter-2015-12-09/segment.sh pku ${INPUT} ${OUTPUT} utf-8 0
