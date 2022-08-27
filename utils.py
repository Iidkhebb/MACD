import csv
import os
import requests
import pandas as pd
import numpy as np
from math import floor
import datetime
import time
import yfinance as yf

class tools:
	def read_coins():
		pair_list = []
		with open("./Coins_List/coins.csv", newline='') as f:
			reader = csv.DictReader(f)
			for r in reader:
				pair_list.append(r['name'])
		return pair_list

class Settings(object):
		def __init__(self, setting):
			self.setting = setting

class StockReader(object):
	def __init__(self, instance):
		self.instance  = instance

	def get_df(self):
		data = yf.download(
			tickers = self.instance.setting.get("stock").get("ticker"),
			period = self.instance.setting.get("stock").get("period"),
			interval = self.instance.setting.get("stock").get("interval"),
			auto_adjust = True,
			prepost=True,
			threads=True
		)
		return data

class MACD(object):
	def __init__(self, df, instance):
		self.df = df
		self.instance  = instance

	def get_macd(self):
		exp1 = self.df.Close.ewm(span=self.instance.setting.get("algorithm").get("slow_ma"), adjust=False).mean()
		exp2 =  self.df.Close.ewm(span=self.instance.setting.get("algorithm").get("fast_ma"), adjust=False).mean()
		self.df["macd"] = exp1-exp2
		self.df["signal"] = self.df.macd.ewm(span=self.instance.setting.get("algorithm").get("smooth"), adjust=False).mean()
		self.df["hist"] = self.df["macd"] - self.df["signal"]
		return self.df

class GenerateTradeSignal(object):
	def __init__(self, df=None):
		self.df = df

	def get_signals(self):
		prices = self.df.Close
		buy_price = []
		sell_price = []
		macd_signal = []
		signal = 0
		for i in range(len(self.df)):
			if self.df['macd'][i] > self.df['signal'][i]:
				if signal != 1:
					buy_price.append(prices[i])
					sell_price.append(np.nan)
					signal = 1
					macd_signal.append(signal)
				else:
					buy_price.append(np.nan)
					sell_price.append(np.nan)
					macd_signal.append(0)
			elif self.df['macd'][i] < self.df['signal'][i]:
				if signal != -1:
					buy_price.append(np.nan)
					sell_price.append(prices[i])
					signal = -1
					macd_signal.append(signal)
				else:
					buy_price.append(np.nan)
					sell_price.append(np.nan)
					macd_signal.append(0)
			else:
				buy_price.append(np.nan)
				sell_price.append(np.nan)
				macd_signal.append(0)
		self.df["buy_price"] = buy_price
		self.df["sell_price"] = sell_price
		self.df["macd_signal"] = macd_signal
		return self.df
