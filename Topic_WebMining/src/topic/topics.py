'''
Created on 16 mai 2017
@author: kimtaing
'''
from googlesearch.googlesearch import GoogleSearch
import re
from langdetect import detect
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import string
from gensim import corpora, models
from six import iteritems
 
# ========================================================================================
# functions
# ========================================================================================
# geet data from google
def googleSearch(query,num_results):
    response = GoogleSearch().search(query, num_results = num_results)
    doc_complete = []
    urls=[]
    titles=[]
    for result in response.results:
        try:
            if (result.getText() is not None and langdetect(result.getText())=='en'):
                doc_complete.append(re.sub("\s+"," " , result.getText()))
                urls.append(result.url)
                titles.append(result.title)
        except:
            print "failed to fetch text for page " + result.url
    return doc_complete,urls,titles

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
    normalized = [lemma.lemmatize(word) for word in stemmed_tokens]
    
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
def LDA(doc_term_matrix,dictionary,nbtopic,num_words):
    # Running and Trainign LDA model on the document term matrix.
    ldamodel = models.LdaModel(doc_term_matrix, num_topics=nbtopic, id2word = dictionary, passes=50)
    # words by topic
    return ldamodel

def print_topics(topics):
    #print "======= topics======================================================================================="
    for i,topic in enumerate(topics):
        print "topic %s : %s" %(i,topic[1])
        
def topics_toArray(topics):
    for i,topic in enumerate(topics):
        print "topic %s : %s" %(i,topic[1])

def topics_toList(topics,nbdocs_bytopic):
    topics_j=[]
    for i,topic in enumerate(topics):
        topic_j={}
        topic_j["name"]="topic_"+str(i)
        keywords=[]
        terms=re.compile(r'[*+]+').split(topic[1])
        for t,term in enumerate(terms):
            if not isfloat(term):
                keywords.append(str(term))
        topic_j["keywords"]=keywords
        topic_j["numberOfResults"]=nbdocs_bytopic["topic_"+str(i)]
        topics_j.append(topic_j)
    return topics_j

def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

def get_infos(query,n_grame):
    # google seach
    num_results_search=10
    doc_complete,urls,titles=googleSearch(query,num_results_search)
    print n_grame
    # cleaning + split in ngrams
    n_gram=n_grame
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
        
    
    results=[]   
    nbdocs_bytopic={}; 
    for i,doc in enumerate(doc_term_matrix):
        result={}
        result["title"]=titles[i]
        result["url"]=urls[i]
        result["excerpt"]=doc_complete[i][:50]
        topics_list=topics#ldamodel.get_document_topics(doc)
        topics_bydoc=[]
        for i,topic in enumerate(topics_list):
            topics_bydoc.append("topic_"+str(i))
            key ="topic_"+str(i)
            if key in nbdocs_bytopic:
                nbdocs_bytopic[key]=nbdocs_bytopic[key]+1
            else:
                nbdocs_bytopic["topic_"+str(i)]=1
        result["topics"]=topics_bydoc 
        results.append(result)
    
    
        
    return topics_toList(topics,nbdocs_bytopic),results
    

# ========================================================================================
# Mains
# ========================================================================================
"""
topics,docs=get_infos("data scientist",2)

for i,t in enumerate(topics):
    print t
      
for d in docs:
    print d


topics,docs=get_infos("data analytic")

for i,t in enumerate(topics):
    print t
      
for d in docs:
    print d
# search info from net

print topics_bydoc




queries = ["data analytic"]
for i, query in enumerate(queries):
    print "==============================", query ,"=============================="
  
    num_results_search=10
    doc_complete,urls,titles=googleSearch(query,num_results_search)
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
        
    
    results=[]   
    for i,doc in enumerate(doc_term_matrix):
        result={}
        result["title"]=titles[i]
        result["url"]=urls[i]
        result["excerpt"]=doc_complete[i][:50]
        topics_list=ldamodel.get_document_topics(doc)
        topics_bydoc=[]
        for i,topic in enumerate(topics_list):
            topics_bydoc.append("topic_"+str(i))
        result["topics"]=topics_bydoc 
        results.append(result)
    for i,r in enumerate(results):
        print r
    
"""    