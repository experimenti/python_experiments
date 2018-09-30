import inspect
from termcolor import colored
from typing import Dict


class Debug:
    r"""Utility class to help with running the tutorial and unit tests.
    Note: Not especially for study, review
    """
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def fakeFunction(*nArray):
        return nArray

    def printClassAndFunction(self):
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        the_method = stack[1][0].f_code.co_name
        print()
        print(colored("----------------------------------------------", 'yellow'))
        print(colored(the_class + ":", 'green'), colored(the_method, 'blue'))
        #print(colored("  Test Class/Method {0}.{1}".format(str(the_class), the_method), 'green')
        print(colored("----------------------------------------------", 'yellow'))
        print(colored("OUTPUT:", "magenta"))


    def getClass(self):
        fr = inspect.stack()[1][3]
        args, _, _, value_dict = inspect.getargvalues(fr)
        if len(args) and args[0] == 'self':
            instance = value_dict.get('self', None)
            if instance:
                return getattr(instance, '__class__', None)
        return None


class Debug:

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    #  Utility Functions for Testing / Displaying 

    def fakeFunction(*nArray):
        return nArray

    def printClassAndFunction(self):
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        the_method = stack[1][0].f_code.co_name
        print()
        print(colored("----------------------------------------------", 'yellow'))
        print(colored(the_class + ":", 'green'), colored(the_method, 'blue'))
        #print(colored("  Test Class/Method {0}.{1}".format(str(the_class), the_method), 'green')
        print(colored("----------------------------------------------", 'yellow'))
        print(colored("OUTPUT:", "magenta"))


    def getClass(self):
        fr = inspect.stack()[1][3]
        args, _, _, value_dict = inspect.getargvalues(fr)
        if len(args) and args[0] == 'self':
            instance = value_dict.get('self', None)
            if instance:
                return getattr(instance, '__class__', None)
        return None

# class pythonPrimer(object):

#     def __init__(self, f):
#         print("inside my_decorator.__init__()")

#         f() # Prove that function definition has completed

#     def __call__(self):
#         print("inside x my_decorator.__call__()")

