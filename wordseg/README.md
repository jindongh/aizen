基于这里的评估：
https://github.com/ysc/cws_evaluation

比较好的两个都已经商业化了：
1. ICTALAS现在改名为NLPIR, https://github.com/NLPIR-team/NLPIR/tree/master/License
2. 清华的THULAS, http://thulac.thunlp.org/

结巴分词用了ICTALAS的词典，无水之木
BosonNLP采用了类似AWS的模式，每天可以免费分词500K个文档

所以这里用斯坦福的这个：
http://nlp.stanford.edu/software/segmenter.shtml

用法：
wget http://nlp.stanford.edu/software/stanford-segmenter-2015-12-09.zip
unzip stanford-segmenter-2015-12-09.zip
cd stanford-segmenter-2015-12-09
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default
cat > test.in << EOF
世界就是一个疯子的囚笼
EOF
./segment.sh pku test.in UTF-8 0


去除html标签的BeautifulSoup
sudo apt-get install python-bs4
