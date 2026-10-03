def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == "row":
		means = []

		for row in matrix:
			means.append(sum(row)/len(row))
		return means
	
	elif mode == "column":
		means = []

		for j in range(len(matrix[0])):
			total = 0

			for i in range(len(matrix)):
				total += matrix[i][j]
			means.append(total/len(matrix))
	return means