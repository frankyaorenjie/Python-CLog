__author__ = 'frankyao'
import inspect
import logging
import os

def get_class_from_frame(fr):
    args, _, _, value_dict = inspect.getargvalues(fr)
    if len(args) and args[0] == 'self':
        instance = value_dict.get('self', None)
        if instance:
            return getattr(instance, '__class__', None)
    return None


class Log(object):
    def __init__(self, log_file_path='./test.log'):
        logging.basicConfig(filename=log_file_path,
                            level=logging.DEBUG, filemode='aw',
                            format='%(asctime)s [%(chain)s] %(message)s')
    def get_meta_data(self):
        frame = inspect.stack()[2][0]
        current_frame = inspect.currentframe()
        caller_frame = inspect.getouterframes(current_frame, 2)
        args, _, _, value_dict = inspect.getargvalues(frame)
        caller_class_name = get_class_from_frame(frame).__name__
        caller_list = []
        for frame in caller_frame[-2:0:-1]:
            caller_list.append(frame[3])
        return '-->'.join([caller_class_name] + caller_list)

    def write(self, message):
        chain = self.get_meta_data()
        logging.info(message,
                     extra={'chain': chain}
        )
