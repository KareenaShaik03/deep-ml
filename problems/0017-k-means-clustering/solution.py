def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	centroids = [list(c) for c in initial_centroids]

	for _ in range(max_iterations):
		clusters = [[] for _ in range(k)]

		for point in points:
			distances =[]
			for centroid in centroids:
				distance = sum((point[d] - centroid[d])**2 for d in range(len(point)))
				distances.append(distance)

			closest = distances.index(min(distances))
			clusters[closest].append(point)

		new_centroids = []

		for i in range(k):
			if clusters[i]:
				dimensions = len(points[0])
				centroid = []

				for d in range(dimensions):
					mean = sum(point[d] for point in clusters[i]) / len(clusters[i])
					centroid.append(mean)

				new_centroids.append(centroid)
			
			else:
				new_centroids.append(centroids[i])

		if new_centroids == centroids:
			break

		centroids = new_centroids

	return [tuple(round(value,4) for value in c) for c in centroids]