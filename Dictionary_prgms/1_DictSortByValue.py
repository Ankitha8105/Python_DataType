dict_ele = {0:9,8:7}
small = dict_ele[0]
for items in dict_ele:
    if dict_ele[items] >= small:
        temp = small
        small = items
        items = temp
print(dict_ele)
