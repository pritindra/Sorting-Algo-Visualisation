import time

def bub_sort(data,drawdata,timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawdata(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    drawdata(data, ['green' for x in range(len(data))])
