# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:55:56 2020

@author: Donal

"""
from utils.intent import intentdetection
def update(): None
def context(): None

slots = {"days" : ["1", "3" , "5", "1 day", "3 days", "5 days"],         "ticker": {"AAPL" :["apple", "Apple"] , "DJIA":["dow", "dow jones"]}}

context.userdata =  {"slotsfill": 'ticker'}
context.userdata =  {"slotsfill": 'days'}
update.message = "for 3 days"


def contextcheck (update, context):
    utterance = update.message
    intent, pred_score = intentdetection(utterance)
    user_data = context.userdata
    try:
        user_data["slot"] = {user_data["slotsfill"] : [i for i in slots["ticker"] for j in slots["ticker"][i] for k in utterance.split() if k==j]}
        slots[user_data["slotsfill"]]
        