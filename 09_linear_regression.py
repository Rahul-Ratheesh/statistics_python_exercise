import pylab, numpy

FILENAME = './data/olympics_2012.csv'
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
years = [int(year) for year in data['Year']]
times = [float(time) for time in data['Time']]

years = pylab.array(years)
times = pylab.array(times)

figure = pylab.figure()    
plot = figure.add_subplot(1, 1, 1)
plot.set_axisbelow(True)
plot.yaxis.grid(color='gray', linestyle='solid', alpha=0.5)

pylab.scatter(years, times, color='steelblue')
pylab.title('Winning times of 1500 meter race in Olympics 2012')
pylab.xlabel('Year')
pylab.ylabel('Time')
a, b = pylab.polyfit(years, times, 1)
label = f'y = {round(a, 3)}x + {round(b, 3)}'
estTimes = a * years + b
pylab.plot(years, estTimes, color='black', label=label, linewidth=1)
pylab.legend()
pylab.show()


	
