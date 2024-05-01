import nltk
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
import joblib

def summarizer(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    freq_dist = FreqDist(filtered_tokens)

    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word]
                else:
                    sentence_scores[sentence] += freq_dist[word]

    summary_sentences = nlargest(5, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    pdf_file.close() 
    # print(summary)
    return summary

def categorizer(summary):
    classifier = joblib.load('saved_model/classifier_model.pkl')
    vectorizer = joblib.load('saved_model/vectorizer_model.pkl')
    new_text = summary
    new_text_tfidf = vectorizer.transform([new_text])
    predicted_category = classifier.predict(new_text_tfidf)[0]
    return predicted_category