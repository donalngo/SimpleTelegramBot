# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:05:34 2020

@author: Donal
"""

import os
import json
import codecs
import pandas as pd
import numpy as np
import random

from itertools import chain
import nltk
import pickle
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import metrics
from sklearn.preprocessing import LabelBinarizer
from conversation import smalltalk, fallback, stocks


import pycrfsuite
import spacy
import en_core_web_sm


##prepare dataset
from os import getcwd, chdir



def intentdetection (utterance):
    intentlist = pickle.load(open("models//intentlist.pkl",'rb'))
    vectorizer = pickle.load(open("models//vectorizer.pk",'rb'))
    kbest = pickle.load(open("models//kbest.pk",'rb'))
    svm = pickle.load(open("models//svm.pk",'rb'))
    
    utterance_vect = vectorizer.transform([utterance])
    utterance_kbest = kbest.transform(utterance_vect)
    utterance_pred, pred_score = int(svm.predict(utterance_kbest)), np.amax(svm.predict_proba(utterance_kbest)[0])
    print(utterance_pred)
    utterance_intent = intentlist[utterance_pred]
    return utterance_intent , pred_score

def reformatting (Reply, Intent, Confidence):
    result = {"Reply" : Reply,
            "Intent": Intent,
            "Confidence": Confidence}
    return result

def getreply(utterance):
    intent, pred_score = intentdetection(utterance)
    if pred_score <= 0.2 :
        method_to_call = fallback.smalltalk_agent_acquaintance()
        result = reformatting("".join(method_to_call), intent, pred_score)
    else:
        if intent[:intent.index('_')] == 'smalltalk':
            method_to_call = getattr(smalltalk, intent)()
            result = reformatting("".join(method_to_call), intent, pred_score)

        elif intent[:intent.index('_')] == 'others':
            method_to_call = getattr(others, intent)()
            result = reformatting("".join(method_to_call), intent, pred_score)
        
    return result
    

