import random
from utils.slots import getslots as slotsdetection
from GetStockNews import GetTrendingNews, GetStockNews
from SlotsFill import slotfill
import settings.store
def Finance_WatchlistE_Clear(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)


def Finance_WatchlistE_Drop(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)	
	return random.choice(replies)


def Finance_WatchlistE_Add(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)



def Finance_General_CurrentPrice(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)



def Finance_General_Whatcanido(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)


def Finance_News_Trending(utterance):
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	print("stockname : ", slots.get('stockname'))

	if not bool(slots):
		reply = slotfill.stockname()
	else:
		results = GetTrendingNews.GetAnswer()
		replies = [["The Trending news are :"], ["The following are the trending news :"], ["Found trending news :"], ["Are you interested in the following trending news?"]]
		reply   = random.choice(replies)
		reply.append("\n\n")
		reply.append(results)
		print(reply)	
	return reply

def Finance_News_Watchlist(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)


def Finance_News_Today(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	print (slots)

	return random.choice(replies)


def Finance_News_Stock(utterance):
	print(settings.store)
	countlength = len(utterance.split())
	if countlength == 1:
		utterance = "for " + utterance
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	print("stockname : ", slots.get('stockname'))
	if not bool(slots["stockname"]):
		reply = slotfill.stockname()
	else:
		stockName = slots.get('stockname')
		results   = GetStockNews.GetAnswer(stockName)
		replies   = [["The Stock news are :"], ["The following are the Stock news :"], ["Found the Stock news :"], ["Are you interested in the following Stock news?"]]
		reply     = random.choice(replies)
		reply.append("\n\n")
		reply.append(results)
	return (reply)


def Finance_Predictions_Sentiments_SingleStock(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)

def Finance_Predictions_Sentiments_Watchlist(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)

def Finance_Predictions_Price_SingleStcok(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)

def Finance_Predictions_Price_Bearish(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)

def Finance_Predictions_Price_Bullish(utterance):
	replies = ["this is my reply"]
	slots = slotsdetection(utterance)
	print("slot : ", slots)
	return random.choice(replies)
