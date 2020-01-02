import pylab

FILENAME = './data/friends.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		friends = []
		for line in dataFile:
			dataRecord = line.strip().split(DELIMITER)
			friends.append(dataRecord[0])
	return friends

def buildPivotTable(attribute):
	props = {}
	for data in attribute:
		count = props.get(data)
		if count is None:
			props[data] = 1
		else:
			props[data] = count + 1
	return props

friends = importData(FILENAME)
pivotTable = buildPivotTable(friends)
print(pivotTable)
pylab.figure()
pylab.pie(pivotTable.values(), 
					labels = pivotTable.keys(), 
					labeldistance = None,
					autopct = '%.2f%%', 
					startangle = 90, 
					colors = ['tab:green', 'tab:blue', 'tab:red'])
pylab.title('Friend Preferences')
pylab.legend()
pylab.show()
