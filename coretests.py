import unittest
import inspect
import numpy as np

from testutils import Debug 
from termcolor import colored
from typing import Dict


DEBUG = True

# These have no class
def imAFunctionInAFunction(name="mycos"):
    def codeit():
        return "now you are in the codeit() function"

    def testit():
        return "now you are in the testit() function"

    if name == "qa":
        return testit 
    else:
        return codeit 


class TestLists(unittest.TestCase):

    def setUp(self):
        self.DEBUG = True

    # del function on a list
    def test_del(self):
        """ Point here: Lists are predictable - java, c#, etc. 
        """ 
        a = [-1, 1, 66.25, 333, 333, 1234.5]
        del a[0]
        self.assertEqual(len(a), 5)

    # funny : operator
        """ Used *alot* in python
        """ 
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
        """ Slicing with lists... get ready for numpy 
        """

        a = [-1, 1, 66.25, 333, 333, 1234.5]

        # get the first 333 starting at pos 4
        result = a.index(333, 4, len(a))

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print(result)

        self.assertNotEqual(result, 3)
        self.assertEqual(result, 4)

    
    # test list with index function for a range
    def test_none_slice(self):
        """ Slicing with none... 
        """

        a = np.random.rand(10)

        # get the first 333 starting at pos 4
        result = a[None, :]
        result_2 = a[:, None]

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("a: {}".format(a))
            print("result = a[None, :]")
            print(result)
            print("result_2 = a[:, None]")
            print(result_2)



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

    def test_imAFunctionInAFunction(self, name="mycos"):
        def codeit():
            return "now you are in the codeit() function"

        def testit():
            return "now you are in the testit() function"

        if name == "qa":
            return testit 
        else:
            return codeit 

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print(self.test_imAFunctionInAFunction())
            print(self.test_imAFunctionInAFunction("qa"))



class TestNumpyArrays(unittest.TestCase):

    def setUp(self):
        self.DEBUG = True

    def testdoubleSlashOperator(self):

        res = 12 * 3 * 2 // 2
        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("12 * 3 * 2 // 2")
            print("Result: {0}".format(res))



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

    def test3DNumpyArrayReference(self):
            """ 
                Point here: Referencing 3D arrays is "create
                2 arrays, containing 3 rows, with 4 values each
            """

            threeD = np.random.rand(2, 3, 4)

            #first row, first column
            array_0_result = threeD[0, 0]

            #second row, second column from last
            array_1_result = threeD[0, 0, 0]

            if (self.DEBUG):
                Debug.printClassAndFunction(self)
                print("the numpy array: {0}".format(threeD))
                print("threeD[0, 0]: {0}".format(array_0_result))
                print("threeD[2, -1]: {0}".format(array_1_result))

            # self.assertEqual(array_0_result, 3)
            # self.assertEqual(array_1_result, 7)


    def test3DComplete(self):
        probs = np.array([[[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1]]])

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("Probs shape: {}".format(probs.shape))
            print("probs: {}".format(probs))
            print("probs [0][0][0]: {}".format(probs[0][0][0]))
            print("probs [0][1][0]: {}".format(probs[0][1][0]))
            print("probs [0][0][1]: {}".format(probs[0][0][1]))


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

    def test3DSliceComplete(self):
        probs   = np.array([[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1]])
        probs_1 = np.array([[[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1]], [[.4, .4, .5, .9], [.9, .1, .2, .3]]])
        probs_2 = np.array([[[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1], [.4, .4, .5, .9], [.9, .1, .2, .3]]])

        if (self.DEBUG):
            Debug.printClassAndFunction(self)
            print("Probs shape: {}".format(probs.shape))
            print("probs: {}".format(probs))
            print("probs [0][1]: {}".format(probs[0:1]))
            print("Probs_1 shape: {}".format(probs_1.shape))
            print("probs_1 = np.array([[[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1]], [[.4, .4, .5, .9], [.9, .1, .2, .3]]])")
            print("probs [0][1]: {}".format(probs_1[0:1]))
            print("Probs_2 shape: {}".format(probs_2.shape))
            print("Probs_2: np.array([[[0.1, 0.6, 0.8, 0.4, 0.9], [0.2, 0.1, 0.6, 0.6, 0.1], [.4, .4, .5, .9], [.9, .1, .2, .3]]])")
            print("probs_2 [0][1]: {}".format(probs_2[0:1]))





def test_jsonStrDict():
    
    intensity : Dict[str, float] = { 'mild': 2.0, 'medium': 5.0, 'hot': 9.0, 'insane': 27 }

    #Same story for tuples
    # x: Tuple[int, str, float] = (3, "yes", 7.5)

    if (DEBUG):
        Debug.printClassAndFunction()
        print("Our hotsauce on the Marville Scale is rated: {}".format(intensity.get('insane')))


# I am the decorator
class pythonPrimer(object):

    def another_f(self, passed_func):
        print("""Function called from from a decorator via the decorator's init with
            a parameter {}""".format(passed_func("qa")))

    def __init__(self, f):
        print("inside my_decorator.__init__()")

        # self.another_f(f) # Prove that function definition has completed
        print("End decorator init")

    def __call__(self, f):
        print("F is: {}".format(f))
        print("inside my_decorator.__call__()")
        print("Post Call")


# PythonDecorators/entry_exit_class.py
class indirection_decorators(object):

    def __init__(self, f):
        self.f = f

    def hijack(self, someVar):
        print("Hijacked! {}".format(someVar))

    def __call__(self, f):
        function = self.f(f)
        print(function)
        function()
        self.hijack(f)


@indirection_decorators
def func1(var):
    print("inside func1() with var: {}".format(var))

    def welcome():
        print("TOTAL CHAOS")

    def wow():
        print("CHAOS")

    if var == "snake":
        return wow 
    else:
        return welcome


if __name__ == '__main__':
    #unittest.main()
    print("After decoration which happens at init")
    #test_decorated_function("dev")
    func1("snake")
    func1("rat")
