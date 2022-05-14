from scipy.optimize import minimize_scalar, brentq

f = lambda x: (x - 2) * (x + 1) ** 2
res = minimize_scalar(f, method='brentq')
# res = brentq()
print(res)