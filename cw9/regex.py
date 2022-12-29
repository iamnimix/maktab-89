import re


#1
# x = re.findall(r'exercises', 'python exercises, PHP exercises, C# exercises')
# for i in x:
#     print(i)


#2

# res = re.search(r'exercises', 'python exercises, PHP exercises, C# exercises')
# print(res.group())
# print(res.span())

#3

# def convert_case(match_obj):
#     if match_obj.group(1) is not None:
#         return "_"
#     if match_obj.group(2) is not None:
#         return " "
#
#
# str1 = " "
# str = "hello group_4"
# print(re.sub(r"( )|(_)", convert_case, str))

#4
# res = re.match(r'^([1-9]|0[1-9]|1[012])[/]([1-9]|0[1-9]|[12][0-9]|3[01])[/]\d{2}(\d{2})?$', "04/18/2022")
# print(res)

#5
# res = re.split(r'-', 'yyyy-mm-dd')
# res.reverse()
# print("-".join(res))

#6
# lst = ['Pazzell', 'Pizza', 'Nima', 'farhad']
# flag = 0
# for i in lst:
#     if re.findall(r'^P', i):
#         flag += 1
#
# if flag == 2:
#     print("match")


#7

# res = re.findall(r'\d+', '51648dver846')
# print(res)

#8
# res = re.findall(r'\b[a|e]\w+', "egg is an expensive")
# print(res)


#9
# res = re.finditer(r'\d+', '48516dver846')
# for i in res:
#     print(i)


#10
# res = re.sub(r'\b([A-Z])[a-z]*([a-z])\b', r'\1\2.', 'Mohammad Hossein Nima')
# print(res)