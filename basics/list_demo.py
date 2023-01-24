demo1 = ["tanveer", 3.34, "BUBT", 27]
print(demo1)
name = "asib"
cgpa = 3.75
university = "BUBT"
age = 25
demo2 = [name, cgpa, university, age]
print(demo2)
print(len(demo2))
r1 = list(range(1, 10))
print(r1)
r2 = list(range(1, 10, 2))
print(r2)
colors = ["Red","Green","Blue"]
print(colors[0])
print(colors[-1]) #negative number starts counting from backwards in a list, -1 means the last index
print("Red" in colors) #Shows if a certain element is in the list
numbers = list(range(10))
for number in numbers:
    print(number)
numbers1 = list(range(10,0,-1))
for num in numbers1:
    print(num)
i = 0
while i < len(colors):
    print(colors[i])
    i+= 1
names = ["Tanveer", "Protik"]
names.append('Asib')
print(names)
letters = ['a','b','c']
letters.extend(['d','e','f'])
print(letters)
nums = [1,2,3,4]
nums.insert(2,'Hello')
print(nums)
popped_item = nums.pop(2)
print(nums)
print(popped_item)
nums.pop()
print(nums)
names.remove('Protik')
print(names)
print(letters[1:])
print(letters[1:3])
print( [num*2 for num in nums] )
print( [num+2 for num in range(1,6) ] )
friends = [ 'tanveer', 'protik', 'asib' ]
c_friends = [ friend[0].upper() for friend in friends ]
print(c_friends)
seasons = [ 'Summer', 'Autumn', 'Winter', 'Spring' ]
print( seasons[::-1] )
print( [item[::-1].lower() for item in seasons] )
numbers2 = [1,2,3,4]
numbers3 = [3,4,5,6]
answer = [ num for num in numbers2 if num in numbers3 ]
print(answer)
numbers4 = list( range(1,4) )
numbers5 = [ list( range(1,4) ) for num in numbers4 ]
print(numbers5)
print([ list( range(1,11) ) for num in list( range(1,11) ) ])