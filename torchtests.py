import torch
import torch.nn as nn
import nose
import unittest

from testutils import Debug


class TestTorchBasics(unittest.TestCase):

    DEBUG = True

    def test_arange_view(self):
        input = torch.arange(1, 5)
        viewed = input.view(1, 1, 2, 2).float()
        viewed_2 = input.view(2, 2, 1, 1).float()

        if(self.DEBUG):
            Debug.printClassAndFunction(self)
            print(input)
            print("input type: {}".format(type(input)))
            print("input shape: {}".format(input.shape))
            print(input)
            print()
            print("viewed type: {}".format(type(viewed)))
            print("viewed shape: {}".format(viewed.shape))
            print(viewed)
            print()
            print("viewed_2 type: {}".format(type(viewed_2)))
            print("viewed_2 shape: {}".format(viewed_2.shape))
            print(viewed_2)
            print()

    def test_arange_view_minus(self):
        input = torch.arange(1, 5)
        viewed = input.view(1, 1, 2, 2).float()
        viewed_2 = input.view(-1)

        if(self.DEBUG):
            Debug.printClassAndFunction(self)
            print(input)
            print("input type: {}".format(type(input)))
            print("input shape: {}".format(input.shape))
            print(input)
            print()
            print("viewed type: {}".format(type(viewed)))
            print("viewed shape: {}".format(viewed.shape))
            print(viewed)
            print()
            print("viewed_2 type: {}".format(type(viewed_2)))
            print("viewed_2 shape: {}".format(viewed_2.shape))
            print(viewed_2)
            print()

    def test_transpose_and_softmax(self):

        tensor = torch.FloatTensor([[[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1]]])

        # pytorch ctc prob form
        log_probabilites_torch = tensor.transpose(0, 1).log_softmax(2).detach().requires_grad_()

        if(self.DEBUG):
            Debug.printClassAndFunction(self)
            # 1) Compare Shape
            print("Shape of log_probablities_torch: {}".format(log_probabilites_torch.shape))
            print("log_probablities_torch: {}".format(log_probabilites_torch))


    def test_softmax_v_logsoftmax(self):
         tensor = torch.ones(2, 10, 5)

         x = tensor.softmax(2) 
         sum_sm = torch.sum(x[0:1:])
         y = tensor.log_softmax(2) 
         sum_slm = torch.sum(y[0:1:])

         if(self.DEBUG):
            Debug.printClassAndFunction(self)

            print("tensor [0][0][:]")
            print(tensor[0][0][:])
            print(x)
            print("Post softmax sum: {}".format(sum_sm))
            print("Post log_softmax sum: {}".format(sum_slm))