input = open('day2data.txt')

totalRibbonNeeded = 0;
for line in input:
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    perimeter1 = 2 * (length + width)
    perimeter2 = 2 * (length + height)
    perimeter3 = 2 * (width + height)

    smallestPerimeter = min(min(perimeter1, perimeter2), perimeter3)
    volume = length*width*height
    totalRibbonNeeded += smallestPerimeter + volume

print(totalRibbonNeeded)