import pylab

FILENAME = './data/sdintuition.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		class_1, class_2, class_3 = [], [], []
		for line in dataFile:
			dataRecord = line.strip().split(DELIMITER)
			class_1.append(int(dataRecord[0]))
			class_2.append(int(dataRecord[1]))
			class_3.append(int(dataRecord[2]))
	return (class_1, class_2, class_3)

class_1, class_2, class_3 = importData(FILENAME)
print(round(pylab.std(class_1), 2))
print(round(pylab.std(class_2), 2))
print(round(pylab.std(class_3), 2))