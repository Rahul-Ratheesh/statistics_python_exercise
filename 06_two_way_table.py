import pylab, numpy

FILENAME = './data/nightlight.csv'
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

def buildTwoWayTable(table):
	twoWayTable = {}
	for index, key in enumerate(table):
		twoWayTable[key] = buildPivotTable(table[key])
	return twoWayTable

def buildPercentageTable(twoWayTable):
	percentTable = {}
	for row in twoWayTable:
		percentTable[row] = {}
		for col in twoWayTable[row]:
			percentTable[row][col] = round((twoWayTable[row][col] / sum(twoWayTable[row].values())) * 100, 2)
	return percentTable 

data = importData(FILENAME)

lightGroup = {}
for lightType, nearsightedness in zip(*list(data.values())):
    if lightGroup.get(lightType) is None:
        lightGroup[lightType] = [nearsightedness]
    else:
        lightGroup[lightType].append(nearsightedness)

twoWayTable = buildTwoWayTable(lightGroup)
percentTable = buildPercentageTable(twoWayTable)
print(percentTable)

summary = {}
for x in percentTable:
    for y in percentTable[x]:
        if summary.get(y) is None: 
            summary[y] = [percentTable[x][y]]
        else:
            summary[y].append(percentTable[x][y])
print(summary)
keys = list(summary.keys())
values = list(summary.values())
bar_width = 0.35
N = len(percentTable)
index = numpy.arange(N)

for i in range(len(values)):
    pylab.bar(index + bar_width*i, values[i], bar_width, label=keys[i])

pylab.title('Lighting Conditions and Near Sightedness')
pylab.xticks(index + bar_width, list(percentTable.keys()))
pylab.ylabel('Near Sightedness')
pylab.legend()
pylab.show()






