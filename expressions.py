#1
mile = 5280
feet_in_23 = mile * 23
print(feet_in_23)

#2
sec = 1
min = 60*sec
hour = 60*min
print("number of seconds:" + str(10*hour+35*min+20))

#3
w = 15
l = 10
result = str(2*w + 2*l)
print("Permiter of the rectanble is " + result)

#4
w = 10
h = 25
Area = str(w*h)
print("Area of the rectangle is " + Area)

#5
pi = 3.14
r = 8
circumference = 2*pi*r
print("Circumference of the circle is " + format(circumference))

#6
area_of_circle = pi*r**2
print("Area of the circle is {}" .format(area_of_circle))

#7
rate = 7
years = 10
p = 1000
interest = p*(1 + 0.01*rate*years)
print("Interest is %.2f" % interest)

#8
a= "My"
b = "name is"
c = "John"
d = "Smith"
print("Complete String is '{0} {1} {2} {3}'" .format(a, b, c, d))


#9
print("Another complete string is '{0} {1} " .format(c, d) + "is " + str(40) + " years old.'")

#10
x0 = 2
x1 = 1
y0 = 5
y1 = 6
distance = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
print("Distance between two points is %.2f" % distance)

