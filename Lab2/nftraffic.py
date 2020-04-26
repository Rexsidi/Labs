import csv

ipaddr = '192.168.250.62'
k1 = 0.5
k2 = 1
b = 100

data = []
q = 0

wor = {}

with open('dataset.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		if row.get('sa') == ipaddr or row.get('da') == ipaddr:
			data.append(row)

for i in data: 
	q += int(i.get('ibyt'))

q = q/1024
if q <= b: 
	total = q*k1 
else: 
	total = b*k1+(q-b)*k2

print(total)
