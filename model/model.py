from utils import preprocess_data, readJSON, return_response_sheet, return_pattern_sheet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os, joblib
from random import randint
from numpy import where

model_path = "/home/amimanas/NDVLLR/myToxicTherapist/model/trained_model.pkl"
model = joblib.load(model_path)

trainingCorpus = readJSON()
patternSheet = return_pattern_sheet()
responseSheet = return_response_sheet()

tfidf_matrix = joblib.load("/home/amimanas/NDVLLR/myToxicTherapist/model/tfidf_matrix.joblib")

def fit_model():
    trainingCorpus = readJSON()
    vectorizer = TfidfVectorizer()

    model = vectorizer.fit(trainingCorpus)
    tfidf_matrix = vectorizer.transform(trainingCorpus)

    model_path = os.path.join('/home/amimanas/NDVLLR/myToxicTherapist/model/', 'trained_model.pkl')

    joblib.dump(model, model_path)
    joblib.dump(tfidf_matrix, "tfidf_matrix.joblib")

def find_cluster(index):
    cumulativeArr = [len(pattern)-1 for pattern in patternSheet]
    for i in range(1, len(cumulativeArr)):
        cumulativeArr[i] += (cumulativeArr[i-1]+1)

    print(cumulativeArr)

    clusterIdx = 0
    for i in range(len(cumulativeArr)):
        if index<=cumulativeArr[i]: 
            clusterIdx = i
            break

    print(clusterIdx)
    responseCluster = responseSheet[clusterIdx]
    
    print(responseCluster[randint(0, len(responseCluster)-1)])


def predictSentiment(data):
    text_vect = model.transform(data)
    similarity_matrix = cosine_similarity(text_vect, tfidf_matrix)[0]

    maxValIdx = where(similarity_matrix == max(similarity_matrix))[0][0] #return the index of pattern with highest similarity value

    print(maxValIdx, trainingCorpus[maxValIdx])

    return maxValIdx
    
# find_cluster(predictSentiment(["my brain won't shut up at night", "It just keeps telling me that I'm worthless."]))
find_cluster(predictSentiment([""]))
# predictResponse(["my brain won't shut up at night", "It just keeps telling me that I'm worthless."])