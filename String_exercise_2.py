#1
str1 = "Anomalocaris"
print(str1.find('o'))

#2
print(str1.index('r'))


#3
s3 = "Waging on the purple drone"
print(s3.rfind('on'))

#4
s4 = "Superficial"
#print(s4.index('z'))

#5
s5 = "There truly is a dazzling bright world out there, waiting for us to explore."

print(s5[len(s5)//2:].index('a'))

#s6
print(s5[:len(s5)//2].rindex('a'))

#s7
s7 = "91342391"
print(s7.lstrip('913').rstrip('391'))

#s8
s8 = "-== Warning! ==-"
print(s8.lstrip('-== ').rstrip(' ==-'))

#s9
s9 = "-== Error! ==-"
print(s9.rstrip("! ==-"))
print(s9[0:s9.index("!")])

#s10
s10 = "-== Success! ==-"
print(s10.lstrip("-== "))

#s11
s11 = "Changing your dog for a bird? Some dog-lover you are."
print(s11.replace('dog', 'cat'))

#s12
s12 = "Being bold has some uses"
print(s12.replace('o', 'a', 1))

#s13
s13 = "-== Error ==-"
print(s13.upper())

#s14  TOBEDISCUSSED
s14= "abraham lincoln"
print(s14.title())


#S15
s15= "rEaDaBlE"
print(s15.lower())

#s16
s16 = "first word is capitalized"
print(s16.capitalize())

#s17
s17 = "a loooooooooooooooooooong word?"
print(s17.count('o'))


#s18
s18 = "100000000000000000000000000000000000000000"
print(s18.count('0'))

#s19
s19 = "Something out of nothing? I really doubt we can do it anytime soon.."
print(s19[:len(s19)//2].count('n'))

#s20
print(s18.replace('0', '9').replace('9', '0', 1))

#21
s21 = "what,if,we,have,no,choice?...."
print(s21.capitalize().replace(',', ' ').rstrip('....'))

