#install libraries
pip install openpyxl
python -c  "import nltk;  nltk.download('averaged_perceptron_tagger')"

#make directories
mkdir ./resources/en/fasttext
mkdir ./resources/en/PPDB
mkdir ./resources/es/fasttext
mkdir ./resources/pt/fasttext
mkdir ./results
mkdir ./results/en
mkdir ./results/es
mkdir ./results/pt


#installing resources for English
wget https://dl.fbaipublicfiles.com/fasttext/vectors-english/crawl-300d-2M-subword.zip -O ./resources/en/fasttext/crawl-300d-2M-subword.zip
unzip ./resources/en/fasttext/crawl-300d-2M-subword.zip
rm ./resources/en/fasttext/crawl-300d-2M-subword.zip
rm ./resources/en/fasttext/crawl-300d-2M-subword.bin
wget http://nlpgrid.seas.upenn.edu/PPDB/eng/ppdb-2.0-tldr.gz -O ./resources/en/PPDB/ppdb-2.0-tldr.gz
gunzip ./resources/en/PPDB/ppdb-2.0-tldr.gz

#installing resources for Spanish
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.es.300.vec.gz -O ./resources/es/fasttext/cc.es.300.vec.gz 
gunzip ./resources/es/fasttext/cc.es.300.vec.gz 


#installing resources for Portuguese
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz -O ./resources/pt/fasttext/cc.pt.300.vec.gz
gunzip ./resources/pt/fasttext/cc.pt.300.vec.gz 

