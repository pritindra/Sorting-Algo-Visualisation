import time

def heapify(data, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and data[i] < data[l]:
		largest = l

	if r < n and data[largest] < data[r]:
		largest = r

	if largest != i:
		data[i],data[largest] = data[largest],data[i]

		heapify(data, n, largest)

    drawdata(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
    time.sleep(timeTick)


def heapSort(data):
	n = len(data)

	for i in range(n//2 - 1, -1, -1):
		heapify(data, n, i)

	for i in range(n-1, 0, -1):
		data[i], data[0] = data[0], data[i] # swap
		heapify(data, i, 0)
    drawdata(data, ['green' for x in range(len(data))])


data = [ 12, 11, 13, 5, 6, 7]
heapSort(data)
n = len(data)
print ("Sorted dataay is")
for i in range(n):
	print ("%d" %data[i]),
