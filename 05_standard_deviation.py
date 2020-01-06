import pylab

FILENAME = './data/sdintuition.csv'
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

data = importData(FILENAME)
class_1 = [int(rating) for rating in data['Class I']]
class_2 = [int(rating) for rating in data['Class II']]
class_3 = [int(rating) for rating in data['Class III']]
print(round(pylab.std(class_1), 2))
print(round(pylab.std(class_2), 2))
print(round(pylab.std(class_3), 2))