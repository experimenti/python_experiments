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

    def test_transpose_and_softmax(self):

        tensor = torch.FloatTensor([[[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1]]])

        # pytorch ctc prob form
        log_probabilites_torch = tensor.transpose(0, 1).log_softmax(2).detach().requires_grad_()

        if(self.DEBUG):
            Debug.printClassAndFunction(self)
            # 1) Compare Shape
            print("Shape of log_probablities_torch: {}".format(log_probabilites_torch.shape))
            print("log_probablities_torch: {}".format(log_probabilites_torch))

