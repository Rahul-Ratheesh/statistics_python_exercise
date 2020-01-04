import pylab, numpy

FILENAME = './data/height.csv'
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
				try:
					value = int(value)
				except:
					data[headers[index]].append(value)
				else:
					data[headers[index]].append(value)
	return data

data = importData(FILENAME)
# print(data)
data['gender'] = ['Female' if value == 0 else 'Male' for value in data['gender']]
# print(data)

male_height, male_weight, female_height, female_weight = [], [], [], []
for gender, height, weight in zip(*list(data.values())):
	if gender == 'Male':
		male_height.append(height)
		male_weight.append(weight)
	else:
		female_height.append(height)
		female_weight.append(weight)		

# heights = data['height']
# weights = data['weight']

figure = pylab.figure()    
plot = figure.add_subplot(1, 1, 1)
pylab.scatter(male_height, male_weight, color = 'blue', label = 'Male')
pylab.scatter(female_height, female_weight, color = 'red', label = 'Female')
pylab.title('Height vs Weight')
pylab.xlabel('Height')
pylab.ylabel('Weight')
plot.set_axisbelow(True)
plot.yaxis.grid(color = 'gray', linestyle = 'solid', alpha = 0.5)
plot.legend()
pylab.show()

