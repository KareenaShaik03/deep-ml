def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n = len(vectors[0])

	means = []
	for feature in vectors:
		means.append(sum(feature)/n)

	result = []

	for i in range(len(vectors)):
		row = []

		for j in range(len(vectors)):
			covariance = 0
			
			for k in range(n):
				covariance += (vectors[i][k]-means[i]) * (vectors[j][k]- means[j])

			covariance = covariance/(n-1)
			row.append(covariance)

		result.append(row)
	return result
