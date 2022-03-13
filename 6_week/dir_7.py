with open(r'.\Test\test.txt') as file1, open(r'.\Test\test2.txt','a') as file2:
    for x in file1:
            file2.write(x)