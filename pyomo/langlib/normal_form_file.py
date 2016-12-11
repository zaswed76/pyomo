# -*- coding: utf-8 -*-

'''


'''


import re
import sys
import fileinput
import paths

try:
    arg = sys.argv[1]
except IndexError:
    pass
    # print('нет аргументов')



def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]

def words_to_file(file, lst):
    """
    сохранить список слов в файл

    :param file: str path
    :param lst: list
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write('\n'.join(lst))




def len_filter(lst, length: int):
    """

    :param lst:
    :param length: не менее этой длины
    :return: list
    """
    return [x for x in lst if len(x) > length]

def unique(lst):
    """
     убирает повторы
    :param lst: list
    :return: list
    """
    return sorted(list(set(lst)))

def normalize_words(lst):
    """
    убирает  не буквенные символы в спмске
    :param lst:
    :return: list
    """
    pattern = re.compile('[\d\W]+\Z|^[\d\W]+')
    return [re.sub(pattern, '', line) for line in lst]

def del_word_tire(lst, pat):
    """
    убирает составные слова пишушиеся через тире
    :param lst:
    :param pat:
    :return: list
    """
    pattern = re.compile(pat)
    return [x for x in lst if re.search(pattern, x) is None]

def uniq_files(path_list):
    res = set()
    for line in fileinput.FileInput(path_list, openhook=fileinput.hook_encoded("utf-8")):
        res.add(line.strip())
    return sorted(list(res))

def sub_dubble_letter(words):
    p = re.compile(r'(\w)\1+')
    return [re.sub(p, '\g<1>', w) for w in words]

def main():
    source = file_to_words(paths.dict_source('Про-Линг_sort.txt'))
    target_path = paths.dict_work('Про-Линг.txt')
    norm = normalize_words(source)
    words_not_tire = del_word_tire(norm, '-')
    norm_len = len_filter(words_not_tire, 2)
    uniq = unique(norm_len)

    words_to_file(target_path, uniq)

def sub_dubble_letter_words():
    path = paths.dict_work('result.txt')
    target_path = paths.dict_work('result_not_dubble.txt')
    source_list = file_to_words(path)
    sub_list = sub_dubble_letter(source_list)
    words_to_file(target_path, sub_list)





if __name__ == '__main__':
    sub_dubble_letter_words()
    # file_1 = paths.dict_work('Про-Линг.txt')
    # file_2 = paths.dict_work('zdf-win.txt')
    # target = paths.dict_work('result.txt')
    # uniq = uniq_files([file_1, file_2])
    # words_to_file(target, uniq)
    # source = file_to_words(paths.dict_source('Про-Линг.txt'))
    # words_to_file(paths.dict_source('Про-Линг_sort.txt'), sorted(source))
    # main()
    # d1 = paths.dict_source('test.txt')
    # source = file_to_words(d1)
    # lst = len_filter(source, 2)
    # uniq = unique(lst)
    # print(source)
    # print(uniq)
    # print(normalize_words(source))
    # print(d1)
    # print(del_word_tire(lst, '[-]'))