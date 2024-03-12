"""
 # Task 1
f = open('nums.txt', 'w')
f.write(input())
f.close()
f1 = open('nums.txt', 'r')
data = f1.read()
data = list(map(int, data.split()))
print(sum(data))

# Task 2
f = open('data.txt', 'w')
f.write("22\n70\n41\n94\n3")
f.close()
f1 = open('data.txt', 'r')
file_len = f1.read()
f1.close()
print(file_len)
numbers = {
    22:'Двадцать два',
    70:'Семьдесят',
    41:'Сорок один',
    94:'Девяносто четыре',
    3:'Три'
}
file_list = list(map(int, file_len.strip(' \n').split()))
# print(file_list)
for i in file_list:
    print(numbers.get(i))

# Task 3
d = []
# for i in range(3):
#     d.append(int(input()))
f = open('nums.txt', 'w')
for i in range(3):
    x = input()
    f.write(x)
    d.append(x)
f.close()
f1 = open('nums.txt', 'r')
nums= f1.read()
f1.close()
# in_nums = list(map(int, nums.split()))
# print(d)
for i in d:
    print(int(i)**2)

"""
# Task 4    
