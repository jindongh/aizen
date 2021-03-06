#!/bin/sh

usage() {
  echo "Usage: $0 [ctb|pku] filename encoding kBest" >&2
  echo "  ctb : use Chinese Treebank segmentation" >&2
  echo "  pku : Beijing University segmentation" >&2
  echo "  kBest: print kBest best segmenations; 0 means kBest mode is off." >&2
  echo >&2
  echo "Example: $0 ctb test.simp.utf8 UTF-8 0" >&2
  echo "Example: $0 pku test.simp.utf8 UTF-8 0" >&2
  exit
}

if [ $# -lt 4 -o $# -gt 5 ]; then
	usage
fi

ARGS="-keepAllWhitespaces false"
if [ $# -eq 6 -a "$1"=="-k" ]; then
		ARGS="-keepAllWhitespaces true"
		lang=$2
		folder=$3
		output=$4
		enc=$5
		kBest=$6
else 
	if [ $# -eq 5 ]; then
		lang=$1
		folder=$2
		output=$3
		enc=$4
		kBest=$5
	else
		usage	
	fi
fi

if [ $lang = "ctb" ]; then
    echo "(CTB):" >&2
elif [ $lang = "pku" ]; then
    echo "(PKU):" >&2
else
    echo "First argument should be either ctb or pku. Abort"
    exit
fi

echo -n "Folder: " >&2
echo $folder >&2
echo -n "Output: " >&2
echo $output >&2
echo -n "Encoding: " >&2
echo $enc >&2
echo "-------------------------------" >&2

BASEDIR=`dirname $0`
DATADIR=$BASEDIR/data
#LEXDIR=$DATADIR/lexicons
JAVACMD="java -mx2g -cp $BASEDIR/classes:$BASEDIR/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFolder $folder -outputFolder $output -inputEncoding $enc -sighanPostProcessing true $ARGS"
#JAVACMD="java -mx2g -cp $BASEDIR/*: edu.stanford.nlp.ie.crf.CRFClassifier -sighanCorporaDict $DATADIR -textFile $file -inputEncoding $enc -sighanPostProcessing true $ARGS"
DICTS=$DATADIR/dict-chris6.ser.gz
KBESTCMD=""

if [ $kBest != "0" ]; then
    KBESTCMD="-kBest $kBest"
fi

if [ $lang = "ctb" ]; then
  $JAVACMD -loadClassifier $DATADIR/ctb.gz -serDictionary $DICTS $KBESTCMD
elif [ $lang = "pku" ]; then
  $JAVACMD -loadClassifier $DATADIR/pku.gz -serDictionary $DICTS $KBESTCMD
fi
