import time


def partition(data,min,data_size,drawdata,timeTick):
    i = ( min-1 )
    pivot = data[data_size]   

    for j in range(min , data_size):
         if   data[j] <= pivot:
            i = i+1
            data[i],data[j] = data[j],data[i]

    data[i+1],data[data_size] = data[data_size],data[i+1]
    drawdata(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
    time.sleep(timeTick)
    return ( i+1 )

# Function to do Quick sort
def quickSort(data,min,data_size,drawdata,timeTick):
    if min < data_size:

        pi = partition(data,min,data_size,drawdata,timeTick)
        quickSort(data, min, pi-1,drawdata,timeTick)
        quickSort(data, pi+1, data_size,drawdata,timeTick)

    drawdata(data, ['green' for x in range(len(data))])
