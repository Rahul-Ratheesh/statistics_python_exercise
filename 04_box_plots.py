import pylab, numpy

FILENAME = './data/graduation.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		colleges = {}
		for line in dataFile:
			name, grad_percent = line.strip().split(DELIMITER)
			if colleges.get(name) is None:
				colleges[name] = [float(grad_percent)]
			else:
				colleges[name].append(float(grad_percent))
	return colleges

colleges = importData(FILENAME)
result = pylab.boxplot(colleges.values(), 
	labels = ['College A', 'College B', 'College C', 'College D', 'College E', 'College F'])
# print(result)
pylab.show()