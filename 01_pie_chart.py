import pylab

FILENAME = './data/friends.csv'
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

def buildPivotTable(values):
	props = {}
	for data in values:
		count = props.get(data)
		if count is None:
			props[data] = 1
		else:
			props[data] = count + 1
	return props

data = importData(FILENAME)
friends = data['Friends']
pivotTable = buildPivotTable(friends)
print(pivotTable)
pylab.figure()
pylab.pie(pivotTable.values(), labels = pivotTable.keys(), labeldistance = None, autopct = '%.2f%%', startangle = 90, colors = ['tab:green', 'tab:blue', 'tab:red'])
pylab.title('Friend Preferences')
pylab.legend()
pylab.show()
