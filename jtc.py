__author__ = 'Anivarth Peesapati'
__version__ = '0.1.0'
__license__ = 'MIT'

import csv, sys

class Json:
	def __init__(self, json_data):
		self.json_data = json_data
		self.rows_list = []

	def recursive_json(self, data, store_list = [], level = 0, key = None):
		# code for dictionary
		if type(data) == type({}):
			# for each key in the data
			for key in sorted(data.keys()):
				# if the size of the list is smaller than the level
				# then add the value to the end
				if len(store_list) <= level+1:
					store_list.append(key)
				# if already some other variable had
				# resided at this level before,
				# add the value to the list inplace of old one
				else:
					store_list[level] = key
				# once processed send the data back to the 
				# function along with the list created and
				# the level
				# Also send the key(it is optional)
				self.recursive_json(data[key], store_list, level+1, key)
		# if data is a list
		# take each and every value in the list and then send it back to
		# the function so that we can check if the value is some other data
		# type and process it based  on the data
		elif type(data) == type([]):
			for value in data:
				self.recursive_json(value, store_list, level, key)
		# This is the case when we have reached the end of the
		# the level. Now add the final value to the 
		# store list(only till the row because we have not deleted)
		# the values residing in other levels which might have resided
		# before.
		# except: Actually written that for unicode error
		else:
			try:
				self.rows_list.append(store_list[:level]+[data])
			except:
				print("Error occured at:", data)

	def convert_to_csv(self, filename = "jsonto.csv", delimiter = ","):
		self.recursive_json(self.json_data)
		with open(filename, "wb") as csvfile:
			spamwriter = csv.writer(csvfile, delimiter = delimiter)
			for row in self.rows_list:
				try:
					spamwriter.writerow(row)
				except:
					print("Error occured at:", row)
