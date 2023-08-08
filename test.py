import string

import jieba

import pandas as pd

data1 = pd.read_csv("DepressionTwitterDatasetFeatureExtraction.csv")
data2 = pd.read_csv("SentimentalAnalysisforTweets.csv")
data3 = pd.read_excel("Student-Depression-Text.xlsx",engine="openpyxl")
data4 = pd.read_excel("StudentsAnxietyandDepressiondataset.xlsx",engine="openpyxl")
stopword = pd.read_csv("stopwords.txt").values
stopwords = []
for i in stopword:
    word = i[0].strip()
    stopwords.append(word)
dict_word = {}
data4.dropna(inplace=True)
for j in data4['text']:

    j = j.translate(str.maketrans('','',string.punctuation))
    words = j.split()

    for i in words:
        if i not in stopwords:
            if i in dict_word.keys() :

                dict_word[i]+= 1

            else:
                dict_word[i] = 1
sort_word = sorted(dict_word.items(),key=lambda x:x[1],reverse=True)
print(sort_word)
