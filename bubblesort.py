

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for x in range(n-1):
	# range(n) also work but outer loop will repeat one time more than needed.

		# Last x elements are already in place
		for y in range(0, n-x-1):

			# traverse the array from 0 to n-x-1
			# Swap if the element found is greater
			# than the next element
			if arr[y] > arr[y+1] :
				arr[y], arr[y+1] = arr[y+1], arr[y]

# for testing above
arr = [77, 33, 44, 55, 22, 11, 66]

bubbleSort(arr)

print ("Sorted array is:")
for x in range(len(arr)):
	print ("%d" %arr[x]),
