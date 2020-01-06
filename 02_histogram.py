import pylab

FILENAME = './data/actor_2013.csv'
DELIMITER = ','

def importData(filename):
	data = {}
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		for header in headers:
			data[header] = []
		for line in dataFile:
			datarecord = line.strip().split(DELIMITER)
			for index, value in enumerate(datarecord):
				data[headers[index]].append(value)
	return data

ages = importData(FILENAME)
ageValues = [int(age) for age in ages['Age']]
figure = pylab.figure()    
plot = figure.add_subplot(1, 1, 1)
print(pylab.hist(ageValues, bins=11, range=(25, 79), color='steelblue', edgecolor='black', linewidth=0.5))
pylab.title('Ages of Best Actor Oscar Winners')
pylab.xlabel('Age')
pylab.ylabel('Count')
plot.set_axisbelow(True)
plot.yaxis.grid(color='gray', linestyle='solid')
pylab.show()