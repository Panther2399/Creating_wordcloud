with open("Panther.txt", 'r') as fh:
    filedata = fh.read()
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, max_words=25, \
                      background_color="white").generate(filedata)
import matplotlib.pyplot as mpLib
mpLib.imshow(wordcloud)
mpLib.axis("off")
mpLib.show()

