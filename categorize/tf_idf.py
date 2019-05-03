# coding: utf-8
import math
import pandas as pd


def compute_tf(word_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_dict.items():
        tf_dict[word] = count/float(bow_count)
    return tf_dict


def compute_idf(doc_list):
    idf_dict = {}
    n = len(doc_list)
    idf_dict = dict.fromkeys(doc_list[0].keys(), 0)
    for doc in doc_list:
        for word, val in doc.items():
            if val > 0:
                idf_dict[word] += 1
    for word, val, in idf_dict.items():
        idf_dict[word] = math.log10(n/float(val))
    return idf_dict


def compute_tf_idf(tf_bow, idfs):
    tf_idf = {}
    for word, val in tf_bow.items():
        tf_idf[word] = val * idfs[word]
    return tf_idf


def load_tab(content):
    print(pd.DataFrame(content))


def worker(filename: str):
    with open(f"dataset/{filename}") as file:
        doc = file.read()
    bow = doc.split(" ")
    wordSet = set(bow)
    word_dict = dict.fromkeys(wordSet, 0)
    for word in bow:
        word_dict[word]+=1
    tfBow = compute_tf(word_dict, bow)
    idfs = compute_idf([word_dict])
    tfidfBow = compute_tf_idf(tfBow, idfs)
    load_tab([tfidfBow])
    sorted_tfidfBow_b = sorted(tfidfBow.items(), key=lambda tfidfBow: tfidfBow[1], reverse =True)
    load_tab([tfidfBow])
    return tfidfBow
