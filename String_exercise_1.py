#1
str1 = "bark"
print(str1[0], str1[1], str1[2], str1[3])
str1 = "park"
print(str1[0], str1[1], str1[2], str1[3])

#2
s2 = "pin"
print(s2[:2])
print(s2[1:])


#3
s3 = "abracadabra"
print(s3[:s3.index("c")], s3[s3.index("c"):])

#4
s4 = "four"
print(len(s4))

#5
s5 = "viisi"
print(len(s5))

#6
s6 = "breathe"
print(s6.rstrip("e"))

#7
s7 = "weight"
print(s7[0:s7.index("t")])


#8
print(s7.lstrip("w"))
print(s7[1:])


#9
s9 = "hearth"
print(s9[1:])

#10
s10 = "intermediate"
print(s10.lstrip("inter").rstrip("te"))

#11
s11 = "premediates"
print(s11[s11.find("media"):s11.index("t")])


#12
s12 =  "grand"
s12a = "ma"
print(s12+s12a)

#13
s13 = "dad"
print(s12+s13)

#14
print(s12*3+s12a)

#15
print(s12*4+s13)

#16
num = 3
print("'%d'" % num)

#17
num1 = "4"*3
print("'%s'" % num1)

#18
str18 = "Another bad example, what a good day"
print(str18.replace('good', 'bad').replace('bad','good',1))

