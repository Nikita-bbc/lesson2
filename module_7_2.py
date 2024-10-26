def custom_write(file_name, strings):
    f = open(file_name, 'a', encoding='utf-8')
    my_list = []
    my_dict = dict()
    for i in range(len(strings)):
        my_list.append(strings.index(strings[i]) + 1)
        my_list.append(f.tell())
        f.write(f'{strings[i]}\n')
        my_dict[tuple(my_list)] = strings[i]
        my_list.remove(my_list[1])
        my_list.remove(my_list[0])
    f.close()
    return my_dict


file_name = 'test.txt'
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write(file_name, info)
print(result)
