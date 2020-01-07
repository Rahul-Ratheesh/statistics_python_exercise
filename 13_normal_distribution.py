import scipy.stats

# Example
mean = 507
sd = 111

#P(X <= 700)
x = 700
prob = round(scipy.stats.norm.cdf(x, mean, sd), 5)
print(prob)

#P(X > 700)
k = 700
prob = round(1 - scipy.stats.norm.cdf(x, mean, sd), 5)
print(prob)

z_score = round(scipy.stats.norm.ppf(prob), 4)
print(z_score)

# Question
mean = 69
sd = 2.8

prob = 0.5/100
z_score = round(scipy.stats.norm.ppf(prob), 4)
x = (z_score * sd) + mean
print(round(x, 2))

prob = 1 - 0.25/100
z_score = round(scipy.stats.norm.ppf(prob), 4)
x = (z_score * sd) + mean
print(round(x, 2))