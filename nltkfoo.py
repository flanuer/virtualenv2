#Trying to better understand nltk tools
# https://medium.com/@parthvadhadiya424/hello-world-program-with-nltk-92cd64509a9f

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "First step in NLTK is tokenizer.  Tokenizer means divide text data \
into tokens.  Here, token means single Entity that is split by any rule for example \
sentence from paragraph."

print(sent_tokenize(example_text))
print("..................................")
print(word_tokenize(example_text))

print("..................................")
from nltk.corpus import stopwords
import nltk

sw = stopwords.words('english')
print(sw)