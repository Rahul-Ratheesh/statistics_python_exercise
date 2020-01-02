FILENAME = './data/depression.csv'
DELIMITER = ','

def importData(filename):
	with open(filename, 'r') as dataFile:
		headers = dataFile.readline().strip().split(DELIMITER)
		hospt, treat, outcome, time, acuteT, age, gender = [], [], [], [], [], [], [] 
		for line in dataFile:
			dataRecord = line.strip().split(DELIMITER)
			hospt.append(int(dataRecord[0]))
			treat.append(dataRecord[1])
			outcome.append(dataRecord[2])
			time.append(float(dataRecord[3]))
			acuteT.append(int(dataRecord[4]))
			age.append(int(dataRecord[5]))
			gender.append(int(dataRecord[6]))
	return (hospt, treat, outcome, time, acuteT, age, gender)


hospt, treat, outcome, time, acuteT, age, gender = importData(FILENAME)
print(gender)
gender = ['Female' if g == 1 else 'Male' for g in gender]
print(gender)
