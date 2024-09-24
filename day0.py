student_count = 100 #integer
rating=9.88 # float
is_published=True #booloean , always start with caps
course_name= "python" #string
print(student_count)

#primitive types= stings numbers boolean
#non primitive types= lists dictionaries sets tuples
#non primitive types are mutable
#primitive types are immutable
# In Python, you can use the `type()` function to check the type of a variable.
# For example:
print(type(student_count))

#lecture 2
#variable names
#variable names should be descriptive and meaningful
#variable names should be in lowercase with underscores
#use underscore to separate two words
#space between "=" and var name 

#lecture 3
#strings
#strings are enclosed in single quotes or double quotes
#strings are immutable
course = "python programming"
print(len(course))
#access to a specific part of sting
print(course[0])
print(course[-1])
print(course[0:3]) # character at the end index is not included
print(course[0:])#returns same as entire string
print(course[:3])#start index considered 0 in this case
print(course[-3:])#returns last 3 characters
print(course[:])#entire string

#double quote awithin a string
course_0='python "programming"'
course_1 = "python \"Programming\""
print(course_0+" "+course_1)

#lecture 4
#escape sequences

# \' print"
# \" print ""
# \\ print backslash
# \n new line

first ="sanika"
last="wani"
full = first + " "+ last
#formatted string
full1 = f"{first} {last}"
print(full)
print(full1)

full2 = f"{len(first)} {2+2}"
print(full2)

#string methods
#upper() converts to uppercase
#lower() converts to lowercase
#title() converts to title case
#strip() removes leading and trailing spaces
#replace() replaces a substring with another substring
#split() splits a string into a list of words
#join() joins a list of words into a string

course= "    python course"
print(course.upper())
print(course)#original string not affected else store in variable
print(course.lower())
print(course.title())
print(course.strip())#remove white spaces from beginning and end , rstrip and lstrip also present
print(course.find("cou")) #index of pro 
print(course.replace("c","C"))#replace small c with cap C
print("pro" in course) # check to see if pro is present in course in boolean
print("Pro" not in course)

#numbers
x = 1 #integers
y = 1.2 #float
print(x,y,sep=",",end=".\n")#sep is used to separate values and
z = 1 + 2j # a + bi complex numbers

#arithmatic operators
# + addition
# - subtraction
# * multiplication
# / division
print(10+3)
print(10-3)
print(10*3)
print(10/3)  #gives floating point number
print(10//3) #gives integer value
print(10%3) #remainder of division
print(10**3) #exponentiation

#augmented assignment operator
a = 10
print(a)
a += 3 #a = a + 3
print(a)
a -= 3 #a = a - 3
print(a)
a *= 3 #a = a * 3
print(a)
a /= 3 #a = a / 3
print(a)
a //= 3 #a = a // 3
print(a)
a %= 3 #a = a % 3
print(a)
a **= 3 #a = a ** 3
print(a)

print("work with numbers")
print(round(2.9)) # roundoff
print(abs(-2.9)) #-ve to +ve

print("importing math")
import math
print(math.ceil(2.2)) #get ceiling of a number . ans 3
print(math.copysign(6.0,-9))
print(math.fabs(6.0)) #return absolute value of x
x=4
print(math.factorial(x))#returns x factorial. valueerror: given when x in not integral value
print(math.floor(x)) #returns floor of x. largest integer less than or equal to x

print("type conversion")
abc = input("x: ") #always string as default
#y = x + 1 #"1"  = 1 'not possible'
#print(y) # will give garbage value or type error
print(type(abc))
print(f"x: {x}, y: {y}")
# int(x)
# float(x)
# bool(x)
# str(x)

#bool()
#falsy values
#""
#0
#None - absense of a value
print("bool===")
print(bool(0))
print(bool(-1))
print(bool(56))

print("quiz")
