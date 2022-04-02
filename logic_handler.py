import csv
import os
import json

class logic:
	def get_ouput_name():
		name_list = []
		for name in os.listdir("./output_csv"):
			name_list.append(name)
		return name_list

	def get_dataframe_raw(file):
		data = []
		with open("./output_csv/" + file, newline='') as f:
			reader = csv.DictReader(f)
			for r in reader:
				data.append(r)
		return data

	def get_dataframe_by_col(df, file):
		data = []
		reader = logic.get_dataframe_raw(file)
		for r in reader:
			data.append(r[str(df)])
		return data

	def get_volume(file):
		vol_data = logic.get_dataframe_by_col('Volume', file)
		change = ((float(vol_data[-1]) - float(vol_data[len(vol_data) - 2])) / float(vol_data[-1])) * 100
		return round(change, 2)

	def get_signal(file):
		signal_data = logic.get_dataframe_by_col('macd_signal', file)
		if ((int(signal_data[-1]) == 1) or (int(signal_data[len(signal_data) - 2]) == 1)):
			return 1
		elif (int(signal_data[-1]) == -1 or (int(signal_data[len(signal_data) - 2]) == 1)):
			return -1
		return 0

	def get_date(signal, r):
		if (int(r[-1]['macd_signal']) == signal):
			return r[-1]['Date']
		return
	
	def get_category(pair):
		data = []
		with open("./Coins_List/coins.csv", newline='') as f:
			reader = csv.DictReader(f)
			for r in reader:
				data.append(r)
		for r in data:
			if (r['name'] == pair):
				return r['category']
		return
	
	def check_signals():
		files = logic.get_ouput_name()
		output = []
		for r in files:
			if(logic.get_signal(r) == 1):
				name = r.replace(".csv", "")
				vol = logic.get_volume(r)
				date = logic.get_date(1, logic.get_dataframe_raw(r))
				category = logic.get_category(name)
				output.append([name, vol, str(date), category])
		return output
	
	def json_append(output):
		out = []
		for r in output:	
			save = {
				'name' : r[0],
				'category' : r[3],
				'date' : r[2],
				'volume' : r[1]
			}
			out.append(save)
		try:
			with open('./signals.json', "a") as file:
				json.dump(out, file)
		except:
			print("Error occurred during saving output")
			pass
		return
