
def findWater(arr, n):
    height = [0]*n
    width = [0]*n

    volume = 0

    height[0] = arr[0]

    for i in range( 1, n):
        height[i] = max(height[i-1], arr[i])


	width[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        width[i] = max(width[i + 1], arr[i]);


	for i in range(0, n):
		volume += min(height[i], width[i]) - arr[i]

	return volume



