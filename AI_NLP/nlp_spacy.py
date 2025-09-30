import spacy
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize,WhitespaceTokenizer,blankline_tokenize
import re
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
nlp = spacy.load("en_core_web_md")
text = """my daughters name is samvedya,samvedya is in 5th standard,samvedya is studying in velammal school.
         she is very naughty girl. samvedya is learning dance,music and keyboard
         samvedya performed in so many dance programs
         she likes to dance."""
doc = nlp(text)
'''print("Named entity,phrases,concepts:")
for ent in doc.ents:
    print(f'{ent.text:15}{ent.label_:10}{ent.start_char:10}{ent.end_char:10}')
    
for token in doc:
    print(token.text,':',token.pos_,':',token.lemma_,':',token.dep_)'''
# cleaning data  

corpus = []
snt_token= nltk.sent_tokenize(text)
sentence = blankline_tokenize(text)
for i in range(len(sentence)):
    review = re.sub('[^a-zA-Z]',' ',sentence[i])
    review = re.sub(r'\s+','',sentence[i])
    review = review.strip()
    review = review.lower()
    review = review.split()
    review = ''.join(review)
    corpus.append(review)

stopwords= list(STOP_WORDS)
stopwords
tokens = [token.text for token in doc]
# frequency of tokens
word_freq={}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
print(word_freq) 
# weight of frequency
max_freq= max(word_freq.values())
print(max_freq)

#sentence score
sent_tokens = [sent for sent in doc.sents]
print(sent_tokens)
sent_score = {}
for i in sent_tokens:
    for word in sent_tokens:
        if word.text.lower() in word_freq.keys():
            if sent_tokens in sent_score.keys():
                sent_score[sent_tokens]=word_freq[word.text.lower()]
            else:
                sent_score[sent_tokens]+= word_freq[word.text.lower()]
#find top sentence_score
from heapq import nlargest
select_length = int (len(sent_tokens)*0.4)
print(select_length)
summary = nlargest(select_length,sent_score,key= sent_score.get)
final_summary = [word.text for word in summary]
print(final_summary) 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(width = 800,height = 400,background_color= 'white',stopwords= stopwords).generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
# to save in file
wc.to_file("word_cloud.png")