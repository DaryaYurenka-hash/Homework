# file = open('import_1.py', 'r')
# file.read()
# file.close()


# with open('lesson10\\example\\import_1.py', 'r', encoding='utf-8') as file:
    # data = file.read()
    
    # lines = file.readlines()
    # print(lines)
    # print(lines[5])
    
    # for line in file:
    #     print(line)
    
    
# with open('lesson10\\example\\123.txt', 'w') as file:
with open('lesson10\\example\\123.txt', 'a', encoding='utf-8') as file:
    file.write("Hello Python\n")
    file.write("Hello Пайтон\n")


# print('ok')    

