import nltk
from nltk.tokenize import word_tokenize,sent_tokenize,line_tokenize,WhitespaceTokenizer
from nltk.util import bigrams, trigrams, ngrams
from nltk.stem import LancasterStemmer,SnowballStemmer,PorterStemmer,WordNetLemmatizer
import streamlit as st

st.set_page_config(page_title="Artificial Intelligence Basics",page_icon=":robot",layout="wide")
st.title("Welcome to Natural Language Processing App")
st.write("This app is the example for Tokenization,Stemming ")

st.header("For enter text",divider= 'blue')
text_input = st.text_area("enter the text here",max_chars=500)

st.subheader("Tokenize and Stemming")

option= st.selectbox("select Tokenizer",['word_tokenize','sent_tokenize','line_tokenize','WhitespaceTokenizer'])

if st.button('Run Tokenizer'):   

    if  option == 'word_tokenize':
        wrd_tkn = word_tokenize(text_input)
        st.write("output of word tokenizer is:",wrd_tkn)
    if option == 'sent_tokenize':
        snt_tkn = sent_tokenize(text_input)
        st.write("output of sentance tokenize is:",snt_tkn)
    if option == 'line_tokenize':
        ln_tkn = line_tokenize(text_input)
        st.write('line tokenize output is:',ln_tkn)
    if option == 'WhitespaceTokenizer':
        wht_spc = WhitespaceTokenizer().tokenize(text_input)
        st.write(wht_spc)
btn = st.selectbox("select util",['bigrams','trigrams','ngrams'])
if st.button('util'):
    
    if btn == 'bigrams':
        bgrm = list(nltk.bigrams(text_input))
        st.write("displays two words in list",bgrm)
    if btn == 'trigrams':
        tgrm = list(nltk.trigrams(text_input))
        st.write("displays three words in list",tgrm)
    if btn == 'ngrams':
        ngrm= list(nltk.ngrams(text_input,6))
        st.write("displays 6 words in list",ngrm)
butn= st.selectbox("select stemming",['PorterStemmer','LancasterStemmer','SnowballStemmer','WordNetLemmatizer'])
wrd = st.text_input("enter word")
if st.button(" stemmer"): 
   if wrd:
      if butn == 'PorterStemmer':
            pstr = PorterStemmer()
            st.write("root of the word is:",pstr.stem(wrd))
      if butn == 'LancasterStemmer':
            lncstm = LancasterStemmer()
            st.write("accurate root of word is:",lncstm.stem(wrd))
      if butn == 'SnowballStemmer':
            snbstm= SnowballStemmer('english',ignore_stopwords= False)
            st.write("same as PorterStemmer",snbstm.stem(wrd))
      if butn == 'WordNetLemmatizer':
            wrdlmt = WordNetLemmatizer()
            st.write("noun",wrdlmt.lemmatize(wrd,'n'))
    

