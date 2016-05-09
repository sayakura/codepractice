from math import sqrt
def pearson_correlation(x,y):
	n = len(x)
	r = (sum([x[i] * y[i] for i in range(len(x))])  - (sum([xi for xi in x]) * sum( [yi for yi in y] )  / n)) / (sqrt(sum([pow(xi,2) for xi in x]) - (pow(sum([xi for xi in x]),2) / n)) * sqrt(sum([pow(yi,2) for yi in y]) - (pow(sum([yi for yi in y]),2) / n)))
	return r
#(sum([x[i] * y[i] for i in range(len(x))])  - (sum([xi for xi in x]) * sum( [yi for yi in y] )  / n)) 
#(sqrt(sum([pow(xi,2) for xi in x]) - (pow(sum([xi for xi in x]),2) / n)) * sqrt(sum([pow(yi,2) for yi in y]) - (pow(sum([yi for yi in y]),2) / n)))