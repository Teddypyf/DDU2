import torch
import numpy as np

# 创造tensor
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)

# tenser维度
shape = (
    3,
    3,
)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(2, 2, 2, 2)  # 维度可以超过3

print({rand_tensor})
print({ones_tensor})
print({zeros_tensor})
