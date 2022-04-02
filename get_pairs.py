import csv

def get_pair():
	with open("./macd_data.csv", newline='') as f:
		reader = csv.DictReader(f)
		for r in reader:
			with open ("./Coins_List/coins.csv", 'a') as s:
				s.write(r['symbol'])
				s.write('-USD')
				s.write(',')
				s.write('crypto')
				s.write('\n')
get_pair()