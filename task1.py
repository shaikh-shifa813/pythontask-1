#QUESTION(1)
str = (input("Enter a string: "))
vowels = "a,e,i,o,u"
print("a=",str.count('a'))
print("e=",str.count('e'))
print("i=",str.count('i'))
print("o=",str.count('o'))
print("u=",str.count('u'))

#QUESTION(2)
a = [1,2,3]
b= [1,456,2]
result =list(set(a) ^ set(b))
print(result)

#QUESTION(3)
sentence = "this are flowers this are also flowers"
words = sentence.split()#split is use for seperation 
count = {}#create dic
for word in words:
    if word in count:
        count[word] = count[word] + 1#word are already ther then increase value by 1
    else: 
        count[word] = 1#if word appear in one time
    print(count)

#QUESTION(4)
{"a":1, "b":2}#The keys become values
{1:"a", 2:"b"}# The values become keys
Given = {"a":1, "b":2}
swapped = {}
for key, value in Given.items():
    swapped[value] = key
print(swapped)

#QUESTION(5)
numbers = [2,6,4,8]#create list
maximum = numbers[0]#assume the maximum and minimum number
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum:", maximum)
print("Minimum:", minimum)

#QUESTION(6)
thislist = ['mango','banana','banana','orange','orange','apple']
result =[]
for list in thislist:
    if list not in result:
        result.append(list)
    print(result)

#QUESTION(7)
mytuple = (10,20,30,40,50)
a, b, *middle, last = mytuple#[30, 40] (skipped values stored as a list)
print("First:", a)#use * for skip middle value
print("Second:", b)
print("Last:", last)

#QUESTION(8)
dict1 = {"a": 2, "b": 3}#create dic
dict2 = {"a": 5, "c": 10}
result = {}#it will store merge dic
for key, value in dict1.items():
    result[key] = value

for key, value in dict2.items():
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value
print(result)

#QUESTION(9)
text = input("Enter a word:")
reversed_text = text[::-1]
if text == reversed_text:
    print("This word is Palindrome")
else:
    print("This word is not Palindrome")

#QUESTION(10)
str1 = "hello"
str2 = "world"
s1 = input("Enter the first str:")
s2 = input("Enter the second str:")
set1 = set(s1)
set2 = set(s2)
common = set1.intersection(set2)
print("Common characters:", common)


















   










