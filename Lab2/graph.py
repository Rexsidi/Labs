import csv
from datetime import datetime
import matplotlib.pyplot as plt

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
	total = q*k1 
else: 
	total = b*k1+(q-b)*k2

print(total)

plt.plot(times, bytes)
plt.title('Статистика объема трафика')
plt.grid(True)
plt.show()
