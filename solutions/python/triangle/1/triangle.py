def triangleCheck(sides):
    return max(sides) * 2 < sum(sides) and sum(sides) > 0

def equilateral(sides):
    a, b, c = sides
    return a == b == c and triangleCheck(sides)

def isosceles(sides):
    a, b, c = sides
    return triangleCheck(sides) and (a == b or b == c or a == c) 

def scalene(sides):
    a, b, c = sides
    return a != b != c != a and triangleCheck(sides)

