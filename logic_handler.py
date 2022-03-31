import csv
import os

class logic:
	def get_ouput_name():
		name_list = []
		for name in os.listdir("/Users/iidkhebb/Desktop/MACD_bot/output_csv"):
			name_list.append(name)
		return name_list

	def get_dataframe(df, file):
		data = []
		with open("./output_csv/" + file, newline='') as f:
			reader = csv.DictReader(f)
			for r in reader:
				data.append(r[str(df)])
		return data

	def get_volume(file):
		vol_data = logic.get_dataframe('Volume', file)
		change = ((float(vol_data[-1]) - float(vol_data[len(vol_data) - 2])) / float(vol_data[-1])) * 100
		return round(change, 2)

	def get_signal(file):
		signal_data = logic.get_dataframe('macd_signal', file)
		if ((int(signal_data[-1]) == 1) or (int(signal_data[len(signal_data) - 2]) == 1)):
			return 1
		elif (int(signal_data[-1]) == -1 or (int(signal_data[len(signal_data) - 2]) == 1)):
			return -1
		return 0

	def check_signals():
		files = logic.get_ouput_name()
		output = []
		for r in files:
			if(logic.get_signal(r) == 0):
				name = r.replace(".csv", "")
				vol = logic.get_volume(r)
				output.append([name, vol])
		return output

print(logic.check_signals())
