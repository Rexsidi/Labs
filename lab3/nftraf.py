import csv
from datetime import datetime
import matplotlib.pyplot as plt


def count():
	ipaddr = '192.168.250.62'
	k1 = 0.5
	k2 = 1
	b = 100

	data = []
	q = 0

	times = []
	timee = []
	bytes = []

	wor = {}

	with open('dataset.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			if row.get('sa') == ipaddr or row.get('da') == ipaddr:
				times.append(datetime.strptime(row.get('te'), '%Y-%m-%d %H:%M:%S'))
				bytes.append(int(row.get('ibyt')))
				q+=int(row.get('ibyt'))
	q = q/1024
	if q <= b:
		total = round (q*k1, 2)
	else:
		total = round (b*k1+(q-b)*k2, 2)
	
	return (total)

if __name__ == '__main__':
	a = count()
	print(a)
