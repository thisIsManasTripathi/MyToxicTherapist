import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re, contractions, string, json
from spellchecker import SpellChecker

# nltk.download('punkt_tab')
# nltk.download('wordnet')

def sanitize_input(inp):
    inp = inp.lower()
    inp = re.sub(r'\d+', ' ', inp) #rm numbers
    inp = re.sub(f'[{string.punctuation}]+','',inp) #removing punctuations
    inp = re.sub(r'\W ', ' ', inp) #rm special chars 
    print(inp)  
    return inp

def filter_input(cleaned_data):
    tokenizedOp = word_tokenize(cleaned_data) #splitting text to words

    lemmatizer = WordNetLemmatizer()
    spellChecker = SpellChecker()
    lemmatizedOp = [lemmatizer.lemmatize(word) for word in tokenizedOp] #transforms the word into crude form (playing,plays->play)
    expandedOp = [contractions.fix(word) for word in lemmatizedOp] #cant -> cannot
    finalOp = [spellChecker.correction(word) for word in expandedOp]
    return finalOp

def preprocess_data(data): #'data' -> list of sentences made from the user input
    sanitizedOp = [sanitize_input(sent) for sent in data]
    filteredOp = [filter_input(sent) for sent in sanitizedOp]
    finalOp = [" ".join(sent) for sent in filteredOp] #Re-join token into sentences
    return finalOp

def readJSON():
    data = ''
    trainingCorpus = []
    with open('/home/amimanas/NDVLLR/myToxicTherapist/model/corpus.json', 'r') as file:
        data = json.load(file)

    for i in data["themes"]:
        trainingCorpus += i["patterns"]

    return trainingCorpus
