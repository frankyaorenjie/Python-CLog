__author__ = 'baniu.yao'


import inspect
import logging
import re


def get_class_from_frame(fr):
    args, _, _, value_dict = inspect.getargvalues(fr)
    if len(args) and args[0] == 'self':
        instance = value_dict.get('self', None)
        if instance:
            return getattr(instance, '__class__', None)
    return None


class CLog(object):
    def __init__(self, log_file_path='./test.log'):
        logging.basicConfig(filename=log_file_path,
                            level=logging.DEBUG, filemode='aw',
                            format='%(asctime)s [%(chain)s] %(message)s')

    def get_file_name_in_full_path(self, file_path):
        return file_path.split('/')[-1]

    def get_meta_data(self):
        frames = inspect.stack()
        chain_list = []
        for i in range(0, len(frames)):
            _, file_path, _, func_name, _, _ = frames[i]
            file_name = self.get_file_name_in_full_path(file_path)
            try:
                args = re.findall('\((.*)\)', frames[i+1][-2][0])[0]
            except IndexError, e:
                func_name = get_class_from_frame(frames[2][0]).__name__
                args = ''
            current_chain = '%s:%s(%s)' % (file_name, func_name, args)
            chain_list.append(current_chain)
        chain_list.reverse()
        print ' --> '.join(chain_list[:-2])

    def write(self, message):
        chain = self.get_meta_data()
        logging.info(message, extra={'chain': chain})
