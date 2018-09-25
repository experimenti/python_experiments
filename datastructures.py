import nose
import unittest
import inspect
import numpy as np
from termcolor import colored


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


class TestsLists(unittest.TestCase):

    def setUp(self):
        self.DEBUG = True

    # del function on a list
    def test_del(self):
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[0]
        self.assertEqual(len(a), 5)

    # funny : operator
    def test_colon(self):
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        b = [-1, 1, 66.25, 333, 333, 1234.5]

        del a[:]
        b.clear()

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print(a)
            print(b)

        self.assertEqual(a, b)

    # test list with index function for a range
    def test_list_index_slice(self):
        a = [-1, 1, 66.25, 333, 333, 1234.5]

        # get the first 333 starting at pos 4
        result = a.index(333, 4, len(a))

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print(result)

        self.assertNotEqual(result, 3)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()


class TestLanguageFundamental(unittest.TestCase):

    # used for DEBUG = True
    # def printFunctionName(self):
    #     print ("********************")
    #     print (inspect.stack()[1][3])
    #     print ("Output:")
    #     print ("********************")

    def setUp(self):
        self.DEBUG = True

      # fundamentals ref vs. value
      # a = b is not a copy, but ref
    def test_ref_vs_value(self):
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        b = [12, 1, 8, 333, 333, 1234.5]

        a = b
        del a[0]

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print(a)
            print(b)

        self.assertEqual(b[0], a[0])


class TestNumpyArrays(unittest.TestCase):

    def setUp(self):
        self.DEBUG = True

    # Point here: length is # of rows, not dimensions 
    def testBasicArrayProps(self):

        np.random.seed(0)
        twoDim = np.random.randint(10, size=(3, 4)) 

        ndim_twoDim = twoDim.ndim
        len_twoDim = len(twoDim)

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("the numpy array: {0}".format(twoDim))
            print("ndim: {0}".format(ndim_twoDim))
            print("len(ndim): {0}".format(len_twoDim))

        self.assertNotEqual(ndim_twoDim, len_twoDim)

    def testBasicNumpyArrayReference(self):
        """ Point here: Referencing 2D arrays is row x column,
            with negative as the move back n operator.
        """ 

        twoD = np.array([[3, 5, 2, 4],
            [7, 6, 8, 8],
            [1, 6, 7, 7]])

        #first row, first column
        array_0_result = twoD[0, 0]

        #second row, second column from last
        array_1_result = twoD[2, -1]

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("the numpy array: {0}".format(twoD))
            print("twoD[0, 0]: {0}".format(array_0_result))
            print("twoD[2, -1]: {0}".format(array_1_result))

        self.assertEqual(array_0_result, 3)
        self.assertEqual(array_1_result, 7)


    def testBasicNumpyArraySlice(self):
        """ Point here: Slice referencing is x[start:stop:step]
            note - assert uses np.all function to make arrays with
            multiple elements comparable (any would be another option)
        """ 

        oneD = np.array([3, 5, 2, 4,
            7, 6, 8, 9,
            1, 11, 7, 4])

        # start 3, stop 10, step 2
        array_0_result = oneD[3:10:2]

        # start 3, stop end, step 2
        array_1_result = oneD[3::2]


        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("the numpy array: {0}".format(oneD))
            print("oneD[3:10:2]: {0}".format(array_0_result))
            print("oneD[3::2]: {0}".format(array_1_result))

        # TODO: remember last week
        # self.assertEqual(np.all(array_0_result, [4, 6, 9, 11]))
        # self.assertEqual(np.all(array_1_result, [4, 6, 9, 11]))

    def testSplatOperator(self):
        """ Point here: A mysterious operator is demystified 
            note - not a point - not a pointer - not a pointer 
            - splat function param preced with * AND the call to the function (*variable)
        """ 

        twoD = np.array([[3, 5, 2, 4],
            [7, 6, 8, 8],
            [1, 6, 7, 7]])

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            splatted = Debug.fakeFunction(*twoD)
            print("TwoD Numpy Array without splatification: {}".format(twoD))
            print()
            print("TwoD Numpy Array with splatification (i.e. *twoD ) : {}".format(splatted))


if __name__ == '__main__':
    unittest.main()
