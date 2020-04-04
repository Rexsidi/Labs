import csv

path = 'data.csv' 
number = '911926375'
k1 = 4
k2 = 1
y_sms = 1
free_sms = 5

data = []
sms = 0
outcome = 0.0
income = 0.0

total = 0.0

def read_file (path):
	with open(path) as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			if row.get('msisdn_origin') == number or row.get('msisdn_dest') == number:
				data.append(row)
	return data

def count_data (number):
	global sms, income, outcome 
	for i in data:
		if i.get('msisdn_origin') == number:
			sms += int(i.get('sms_number'))
			outcome += float(i.get('call_duration'))
		elif i.get('msisdn_dest') == number:
			income += float(i.get('call_duration'))
data = read_file(path)
count_data (number)
if sms <= free_sms: sms = 0
else: sms -= 5
if income <= 5: income = 0
else: income -= 5
total += (outcome * k1) + (income * k2) + (sms * y_sms)

print (total)