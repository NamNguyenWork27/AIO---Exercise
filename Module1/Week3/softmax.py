import torch 
import torch.nn as nn 

class SoftMax(nn.Module):
    def __init__(self):
        super().__init__() 
    
    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition 
    
# data1 = torch.Tensor([1, 2, 3])
# my_softmax = SoftMax()
# output1 = my_softmax(data1)
# print(output1)  

class StableSoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition 
    
data2 = torch.Tensor([1, 2, 3])
stable_softmax = StableSoftMax()
output = stable_softmax(data2)
print(output)

