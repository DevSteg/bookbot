def get_file_contents(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_char(text):
    lowercase_file = text.lower()
    char_dict = {}
    for i in lowercase_file:
        char_count = lowercase_file.count(i)
        char_dict[i] = char_count
    return char_dict

def sort_on(items):
    return items["count"]

def sort_dict(dict):
    dict_list = [{"char": key, "count": value} for key,value in dict.items() if key.isalpha()]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
