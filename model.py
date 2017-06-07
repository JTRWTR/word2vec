from xml.etree import ElementTree
from gensim.models import word2vec
import logging

# PLEASE DOWNLOAD jawiki-latest-pages-articles.xml.bz2 FROM THIS URL(https://dumps.wikimedia.org/jawiki/latest/)
XMLFILE = "data/jawiki-latest-pages-articles.xml"

# ------- XMLをテキスト形式へ変換 -------

tree = ElementTree.parse(XMLFILE)
root = tree.getroot()

signs = ["[","]","*","{","}","=","|","-","<",">",":",";","'",]

text = ""

# wikiの各記事のテキストタグを拾い、テキストから上記の記号を除去
for e in root.getiterator():
  if 'text' in e.tag:
    result = e.text
    for s in signs:
      try:
        result = result.replace(s,"")
      except:
        result = result
    print(result)
    text = text + result

# ------- XMLをテキスト形式へ変換 -------

# ------- model作成 -------

#進捗表示
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

tagger = MeCab.Tagger("-Owakati")
wakati = taggar.parse(text)

data = word2vec.Text8Corpus(wakati)

model = word2vec.Word2Vec(data, size=200, min_count=20, window=15)

model.save("model/wiki.model")

# ------- model作成 -------
