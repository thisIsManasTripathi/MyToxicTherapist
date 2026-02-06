from utils import preprocess_data, readJSON
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os, joblib

model_path = "/home/amimanas/NDVLLR/myToxicTherapist/model/trained_model.pkl"
model = joblib.load(model_path)

tfidf_matrix = joblib.load("/home/amimanas/NDVLLR/myToxicTherapist/model/tfidf_matrix.joblib")

def fit_model():
    trainingCorpus = readJSON()
    vectorizer = TfidfVectorizer()

    model = vectorizer.fit(trainingCorpus)
    tfidf_matrix = vectorizer.transform(trainingCorpus)

    model_path = os.path.join('/home/amimanas/NDVLLR/myToxicTherapist/model/', 'trained_model.pkl')

    joblib.dump(model, model_path)
    joblib.dump(tfidf_matrix, "tfidf_matrix.joblib")


def predictResponse(data):
    text_vect = model.transform(data)
    similarity_matrix = cosine_similarity(text_vect, tfidf_matrix)[0]
    trainingCorpus = readJSON()
    for i in range(len(trainingCorpus)):
        if similarity_matrix[i]:
            print(trainingCorpus[i])
    

predictResponse(["my brain won't shut up at night"])