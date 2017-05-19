'''
Created on 16 mai 2017

@author: kimtaing
'''
from googlesearch.googlesearch import GoogleSearch
import re
import unicodedata

import sys

from langdetect import detect

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import string
from itertools import islice

import gensim
from gensim import corpora, models, similarities
from six import iteritems
 
# ========================================================================================
# functions
# ========================================================================================
# geet data from google
def googleSearch(query,num_results):
    response = GoogleSearch().search(query, num_results = num_results)
    doc_complete = []
    for result in response.results:
        if (result.getText() is not None and langdetect(result.getText())=='en'):
            doc_complete.append(re.sub("\s+"," " , result.getText()))
    return doc_complete

# langue detection
def langdetect(txt):
    return detect(txt)


def clean(doc):
    # cleaning and procesing data
    tokenizer = RegexpTokenizer(r'\w+')
    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation) 
    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()
    lemma = WordNetLemmatizer()
    # clean and tokenize document string
    raw = doc.lower()
    tokens = tokenizer.tokenize(raw)
    
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in stop]
    
    # remove punc_free from tokens
    punc_free = [ch for ch in stopped_tokens if ch not in exclude]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in punc_free]
    
    # lemm tokens
    normalized = [lemma.lemmatize(word) for word in punc_free]
    
    return normalized

def ngrams(tokens, n):
    # reconstruction de la chaine
    if n==1:
        grams=tokens
    else :
        raw="".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
        raw=raw.split()
    
        grams = [' '.join(raw[i:i+n]) for i in xrange(len(raw)-n+1)]
    
    return grams

# ================= Model ==============
def gettfidf(doc_term_matrix):
    tfidf = models.TfidfModel(doc_term_matrix) # step 1 -- initialize a model
    corpus_tfidf = tfidf[doc_term_matrix]
    return corpus_tfidf

def Lsi(corpus_tfidf,dictionary,nbtopic,num_words):
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=nbtopic) # initialize an LSI transformation
    return lsi

def LDA(doc_term_matrix,dictionary,nbtopic,num_words):
    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel
    # Running and Trainign LDA model on the document term matrix.
    ldamodel = models.LdaModel(doc_term_matrix, num_topics=nbtopic, id2word = dictionary, passes=50)
    #print(ldamodel)
    # words by topic
    return ldamodel

def print_topics(topics):
    #print "======= topics======================================================================================="
    for i,topic in enumerate(topics):
        print "topic %s : %s" %(i,topic[1])
        
def topics_toArray(topics):
    for i,topic in enumerate(topics):
        print "topic %s : %s" %(i,topic[1])

def topics_toList(topics):
    topics_j=[]
    for i,topic in enumerate(topics):
        topic_j={}
        topic_j["name"]="topic "+str(i)
        keywords=[]
        terms=re.compile(r'[*+]+').split(topic[1])
        for t,term in enumerate(terms):
            if not isfloat(term):
                keywords.append(str(term))
        topic_j["keywords"]=keywords
        
        topics_j.append(topic_j)
    return topics_j

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def get_topics(query):
    # google seach
    num_results_search=10
    doc_complete=googleSearch(query,num_results_search)
    
    # cleaning + split in ngrams
    n_gram=3
    doc_clean = [ngrams(clean(doc),n_gram) for doc in doc_complete]
    
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. 
    dictionary = corpora.Dictionary(doc_clean)
    once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq <= 1] # get words that appear only once
    query_ids=[tokenid for tokenid, term in dictionary.iteritems() if term == query]
    dictionary.filter_tokens(once_ids)  # remove words that appear only once
    dictionary.filter_tokens(query_ids)  # remove words that equal to query
    
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    
    #parameter for model 
    nbtopic=5
    num_words=3

    #run model
    if len([x for x in doc_term_matrix if x != []]) >0:
        ldamodel=LDA(doc_term_matrix,dictionary,nbtopic,num_words)
        topics=ldamodel.print_topics(num_topics=nbtopic, num_words=num_words)
        return topics_toList(topics)
        

# ========================================================================================
# Mains
# ========================================================================================

topics=get_topics("data analytic")
print topics

# search info from net

"""

topics=get_topics("data analytic")
print topics



queries = ["data analytic","data visualization","network analysis"]
for i, query in enumerate(queries):
    print "==============================", query ,"=============================="
  
    num_results_search=10
    doc_complete=googleSearch(query,num_results_search)
    '''for i in range(2): #range(len(doc_complete)):
        u=doc_complete[i]
        print "============================== doc", i,"======================================================"
        print u[:500]
    '''    
    # cleaning + split in ngrams
    n_gram=3
    doc_clean = [ngrams(clean(doc),n_gram) for doc in doc_complete]
    '''for i in range(2):#range(len(doc_clean)):
        print "============================== doc", i,"======================================================"
        print doc_clean[i][:30]

    '''    

    # Creating the term dictionary of our courpus, where every unique term is assigned an index. 
    dictionary = corpora.Dictionary(doc_clean)
    once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq <= 1] # get words that appear only once
    query_ids=[tokenid for tokenid, term in dictionary.iteritems() if term == query]
    dictionary.filter_tokens(once_ids)  # remove words that appear only once
    dictionary.filter_tokens(query_ids)  # remove words that equal to query
    #print dic to ckeck
    '''for k, v in list(islice(dictionary.iteritems() , 5)):
        print "id %s => %s" % (k, v)
    '''  

    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    '''for i,doc in enumerate(doc_term_matrix):
        print "============ doc %s =======================" %(i)
        for d in doc:
            print "%s : %s"% (dictionary[d[0]], d[1])
    '''        
    #parameter for model 
    nbtopic=5
    num_words=3

    #run model
    if len([x for x in doc_term_matrix if x != []]) >0:
        ldamodel=LDA(doc_term_matrix,dictionary,nbtopic,num_words)
        topics=ldamodel.print_topics(num_topics=nbtopic, num_words=num_words)
        print_topics(topics)
        print "\n*** topic rate by doc ***"
        for i,doc in enumerate(doc_term_matrix):
            print "===> doc ",i," :"
            print(ldamodel.get_document_topics(doc))
"""