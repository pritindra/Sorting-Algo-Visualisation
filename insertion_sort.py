import time

def insertionSort(data,drawdata,timeTick):
    for i in range(1, len(data)):

        key = data[i]
        j = i-1

        while j >= 0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
                drawdata(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
        data[j+1] = key

    drawdata(data, ['green' for x in range(len(data))])
