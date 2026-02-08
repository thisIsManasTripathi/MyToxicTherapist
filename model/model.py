from utils import preprocess_data, readJSON, return_response_sheet, return_pattern_sheet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os, joblib
from random import randint
from numpy import where
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

#Loading the model from memory
model_path = f"{BASE_DIR}/trained_model.pkl"
model = joblib.load(model_path)

trainingCorpus = readJSON()
patternSheet = return_pattern_sheet()
responseSheet = return_response_sheet()

tfidf_matrix = joblib.load(f"{BASE_DIR}/tfidf_matrix.joblib")

def fit_model():
    trainingCorpus = readJSON()
    vectorizer = TfidfVectorizer()

    model = vectorizer.fit(trainingCorpus)
    tfidf_matrix = vectorizer.transform(trainingCorpus)

    joblib.dump(model, model_path)
    joblib.dump(tfidf_matrix, f"{BASE_DIR}/tfidf_matrix.joblib")

def respond(index):

    #genrating cumulative array for easily finding the cluster to which the pattern belonged
    cumulativeArr = [len(pattern)-1 for pattern in patternSheet]
    for i in range(1, len(cumulativeArr)):
        cumulativeArr[i] += (cumulativeArr[i-1]+1)

    clusterIdx = 0
    for i in range(len(cumulativeArr)):
        if index<=cumulativeArr[i]: 
            clusterIdx = i
            break

    responseCluster = responseSheet[clusterIdx] #getting the corresponding response cluster.

    return responseCluster[randint(0, len(responseCluster)-1)]


def findSentimentIndex(data):
    data = preprocess_data(data) #cleaning the data before feeding it to the vectorizer

    text_vect = model.transform(data)
    similarity_matrix = cosine_similarity(text_vect, tfidf_matrix)[0]

    maxValIdx = where(similarity_matrix == max(similarity_matrix))[0][0] #return the index of pattern with highest similarity value

    return maxValIdx