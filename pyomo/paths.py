from os import path

root = path.dirname(__file__)

def dict_source(base_name):
    return path.join(root, 'resource/dictionaries/source', base_name)

def dict_work(base_name):
    return path.join(root, 'resource/dictionaries/work', base_name)