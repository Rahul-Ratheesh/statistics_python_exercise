import pylab

FILENAME = './data/actor_2013.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		ages = []
		for line in dataFile:
			dataRecord = line.strip().split(DELIMITER)
			ages.append(int(dataRecord[0]))
	return ages

ages = importData(FILENAME)
figure = pylab.figure()    
plot = figure.add_subplot(1,1,1)
print(pylab.hist(ages, bins=11, range=(25, 79), color='steelblue', edgecolor='black', linewidth=0.5))
pylab.title('Ages of Best Actor Oscar Winners')
pylab.xlabel('Age')
pylab.ylabel('Count')
plot.set_axisbelow(True)
plot.yaxis.grid(color='gray', linestyle='solid')
pylab.show()