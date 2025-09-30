import nltk
import spacy
import re
from nltk.stem import PorterStemmer
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize,blankline_tokenize,WhitespaceTokenizer
import matplotlib.pyplot as plt


text = '''ishaan is 6 years old boy. he loves to dance. 
        ishaan is studying in desia school. ishaan have more than 5 friends.
         he is learning abacus in school.  '''

# cleaning text
sent_tokens = nltk.sent_tokenize(text)
print(sent_tokens,'\n')
sentence = nltk.blankline_tokenize(text)
print(sentence)

corpus = []
for i in range(len(sentence)):
    review = re.sub('[^a-zA-Z*]',' ',sentence[i])
    review = re.sub(r'\s+','',sentence[i])
    review = review.lower()
    review = review.split()
    review = '  '.join(review)
    corpus.append(review)
print(corpus)
white_spacetoken = WhitespaceTokenizer().tokenize(text)
stop_words = list(STOP_WORDS)
# word cloud means which word frequency is more (which word repeates more than other words) that word will highlates 
wc = WordCloud(width= 800,height = 400,background_color= 'white', mode= "RGB",stopwords= stop_words).generate(text)
plt.figure(figsize=(8,6))
plt.imshow(wc,interpolation= 'bilinear')
plt.axis("off")
plt.show()

#save ti file
wc.to_file("ishaan_wordcloud.png")
