def Task1(): 
    # Task 1
    f = open('nums.txt', 'w')
    f.write(input())
    f.close()
    f1 = open('nums.txt', 'r')
    data = f1.read()
    data = list(map(int, data.split()))
    print(sum(data))

def Task2():
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

def Task3 ():
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

# Task 4
def Task4():
 # input text
    letter = """
    «Восстань, пророк, и виждь, и внемли,
    Исполнись волею моей,
    И, обходя моря и земли,
    Глаголом жги сердца людей»."""
    symbol_to_remove = "«»"
    chars = 0
    worlds = 0

     # Adding, reading and writing a file
    f = open('letter.txt', 'w')
    f.write(letter)
    f.close()
    f1 = open('letter.txt', 'r')
    new_letter = f1.read()
    f1.close()


     # Delete unncessary symbols
    for i in symbol_to_remove:
        new_letter = new_letter.replace(i, "")
     # Divide into lines and remove first element
    spisok = new_letter.split("\n")
    spisok.pop(0)

     # Can be replaced on f"{i+1})" in print() 
    d = ["1)", "2)", "3)", "4)"]
    for i in range(len(spisok)):
        chars = len(spisok[int(i)])
        worlds = len(spisok[int(i)].split())
        print(d[i], f"Символов в строке: {chars}, слов в строке: {worlds}")

def Task5 ():
    print()