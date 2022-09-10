def plotGraph(yDataArray, xDataArray, accuracy):
    height = yDataArray
    height = max(height)
    height = round(height, -len(str(height)) + 1)
    for i in range(accuracy + 1):
        segment = int(height/accuracy*(accuracy - i))
        print(str(segment) + " " * (len(str(height)) - len(str(segment))) + "|", end = "")
        for y in yDataArray:
            if(y >= segment):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

with open("data.txt") as f:
    data = f.read().splitlines()

xData = [int(x.split()[0]) for x in data]
yData = [int(y.split()[1]) for y in data]
    
#Change the 3rd arg to a suitable number
plotGraph(yData, xData, 100)