input = open('day2data.txt')

totalWrappingPaperNeeded = 0;
for line in input:
    dimensions = line.split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    side1 = length*width
    side2 = length*height
    side3 = width*height

    smallestSide = min(min(side1, side2), side3)
    totalWrappingPaperNeeded += 2*side1 + 2*side2 + 2*side3 + smallestSide

print(totalWrappingPaperNeeded)
