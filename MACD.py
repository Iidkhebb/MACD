import csv
import requests
import pandas as pd
import numpy as np
from math import floor
import datetime
import time
import os
import yfinance as yf
from utils import *
from time import sleep as wait
from logic_handler import *

pair_list = tools.read_coins()
len_pair = len(pair_list)
pair_index = 0

class Controller(object):
	def __init__(self, commands):
		self.commands = commands

	def get(self):
		settings = Settings(setting=self.commands)
		helper = StockReader(instance=settings)
		df = helper.get_df()
		macd_helper = MACD(instance=settings, df=df)
		df    = macd_helper.get_macd()
		signal_helper = GenerateTradeSignal(df=df)
		df = signal_helper.get_signals()
		df.to_csv("./output_csv/" + str(pair_list[pair_index]) + ".csv")

	def main():
		global pair_index
		for row in pair_list:
			print(row)
			commands = {
				"stock":{
					"ticker": str(row),
					'interval':"1d",
					'period':"3mo"
				},
				"algorithm":{
					"slow_ma":12,
					"fast_ma":26,
					"smooth":9
				}
			}
			helper = Controller(commands=commands)
			response  = helper.get()
			pair_index += 1

if __name__ == "__main__":
	Controller.main()
	logic.json_append(logic.check_signals())
	print("Done")
