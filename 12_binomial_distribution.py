import scipy.stats

n = 10
p = 0.2

#P(X <= 4)
k = 4
prob = round(scipy.stats.binom.cdf(k, n, p, loc=0), 4)
print(prob)

#P(X > 2)
k = 2
prob = round(1 - scipy.stats.binom.cdf(k, n, p, loc=0), 4)
print(prob)