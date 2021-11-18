import re

myFile = open(input(),'r',encoding='utf8')
str_book = myFile.read()
str_x = re.sub(r'[^\w\s]','',str_book)
str_x = str_x.split()


n = 1
s_dic = {}
uniqlist = []
for item in str_x:
    itemExist = False
    if len(item) > 3:
        for i in uniqlist:
            if i == item:
                itemExist = True
                n += 1
                s_dic[item] = n
                break
            n = 1  
        if not itemExist: 
            uniqlist.append(item)
if s_dic != {}:
    max_value = max(s_dic.values())
    f_dic = {k:v for k,v in s_dic.items() if v == max_value}
    print(f'Самые часто встречающиеся слова: {list(f_dic.keys())}')     
else:
    print('Все слова уникальны.')


r = re.compile("[a-zA-Z]+")
ing_book = [w for w in filter(r.match, str_x)]

max = 0
for i in range(len(ing_book)):
    if len(ing_book[i]) > len(ing_book[max]):
        max = i

print(f'Cамое длинное английское слово: {ing_book[max]}')  

myFile.close()
