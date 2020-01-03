import pylab

FILENAME = './data/nightlight.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		lamp, nightLight, noLight = [], [], []
		for line in dataFile:
			lightType, response = line.strip().split(DELIMITER)
			if lightType == 'lamp':
				lamp.append(response)
			elif lightType == 'night light':
				nightLight.append(response)
			elif 'no light':
				noLight.append(response)
			else:
					raise ValueError('Invalid Value')
	return (lamp, nightLight, noLight)

def buildPivotTable(attribute):
	props = {}
	for data in attribute:
		count = props.get(data)
		if count is None:
			props[data] = 1
		else:
			props[data] = count + 1
	return props

def buildTwoWayTable(names, *attributes):
	twoWaytable = {}
	for i, attribute in enumerate(attributes):
		twoWaytable[names[i]] = buildPivotTable(attribute)
	return twoWaytable

def buildPercentageTable(twoWayTable):
	percentTable = {}
	for row in twoWayTable:
		percentTable[row] = {}
		for col in twoWayTable[row]:
			percentTable[row][col] = round((twoWayTable[row][col] / sum(twoWayTable[row].values())) * 100, 2)
	return percentTable 

lamp, nightLight, noLight = importData(FILENAME)
twoWayTable = buildTwoWayTable(['lamp', 'night light', 'no light'], lamp, nightLight, noLight)
percentTable = buildPercentageTable(twoWayTable)
print(percentTable)

# pylab.bar(percentTable.keys(), percentTable.values())
# pylab.show()






