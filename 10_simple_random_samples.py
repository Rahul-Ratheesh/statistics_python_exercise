import random, pylab, utils

FILENAME = './data/student_survey.csv'

data = utils.importData(FILENAME)
course = data['Course']
handed = data['Handed']
sex = data['Sex']
data['Verbal'] = [ verbal if verbal != '*' else '0' for verbal in data['Verbal']]
verbal = [int(verbal) for verbal in data['Verbal']]
data['Age'] = [ age if age != '*' else 0 for age in data['Age']]
age = [float(age) for age in data['Age']]

courseSample = random.sample(course, 192)
handedSample = random.sample(handed, 192)
sexSample = random.sample(sex, 192)
verbalSample = random.sample(verbal, 192)
ageSample = random.sample(age, 192)

p_course = utils.buildPivotTable(course)
print(p_course)
s_course = utils.buildPivotTable(courseSample)
print(s_course)
p_handed = utils.buildPivotTable(handed)
print(p_handed)
s_handed = utils.buildPivotTable(handedSample)
print(s_handed)
p_sex = utils.buildPivotTable(sex)
print(p_sex)
s_sex = utils.buildPivotTable(sexSample)
print(s_sex)
print(utils.fiveNumberSummary(verbal))
print(utils.fiveNumberSummary(verbalSample))
print(utils.fiveNumberSummary(age))
print(utils.fiveNumberSummary(ageSample))
pylab.figure()
pylab.suptitle('Population vs Sample')
pylab.subplot(3, 2, 1)
pylab.title('Course - Population')
pylab.pie(p_course.values(), labels = p_course.keys(), labeldistance = None, autopct = '%.2f%%', startangle = 90, colors = ['tab:green', 'tab:blue', 'tab:red'])
pylab.legend()
pylab.subplot(3, 2, 2)
pylab.title('Course - Sample')
pylab.pie(s_course.values(), labels = s_course.keys(), labeldistance = None, autopct = '%.2f%%', startangle = 90, colors = ['tab:green', 'tab:blue', 'tab:red'])
pylab.legend()
pylab.subplot(3, 2, 3)
pylab.title('Handed - Population')
pylab.pie(p_handed.values(), labels = p_handed.keys(), labeldistance = None, autopct = '%.2f%%', colors = ['tab:green', 'tab:blue'])
pylab.legend()
pylab.subplot(3, 2, 4)
pylab.title('Handed - Sample')
pylab.pie(s_handed.values(), labels = s_handed.keys(), labeldistance = None, autopct = '%.2f%%', colors = ['tab:green', 'tab:blue'])
pylab.legend()
pylab.subplot(3, 2, 5)
pylab.title('Sex - Population')
pylab.pie(p_sex.values(), labels = p_sex.keys(), labeldistance = None, autopct = '%.2f%%', startangle = 90, colors = ['tab:green', 'tab:blue'])
pylab.legend()
pylab.subplot(3, 2, 6)
pylab.title('Sex - Sample')
pylab.pie(s_sex.values(), labels = s_sex.keys(), labeldistance = None, autopct = '%.2f%%', startangle = 90, colors = ['tab:green', 'tab:blue'])
pylab.legend()
pylab.show()
