import pylab, numpy

FILENAME = './data/graduation.csv'
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
collegeGroup = {}
for college, gradPercent in zip(*list(data.values())):
    if collegeGroup.get(college) is None:
        collegeGroup[college] = [float(gradPercent)]
    else:
        collegeGroup[college].append(float(gradPercent))

pylab.boxplot(collegeGroup.values(), labels = ['College A', 'College B', 'College C', 'College D', 'College E', 'College F'])
pylab.ylabel('Graduation Percent')
pylab.show()