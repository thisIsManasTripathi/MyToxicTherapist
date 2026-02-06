import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re, contractions, string
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


inp = "Hello dudee! Can't wait to see ya on frida 78."
print(filter_input(sanitize_input(inp)))