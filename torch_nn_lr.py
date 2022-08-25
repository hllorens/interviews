''' 
  1) Design: input, output size, forward pass
  2) loss and optimizer
  3) Training loop:
      -forward compute prediction (and loss)
      -backward (grads)
      -update weights aka parameters
'''


# from https://github.com/python-engineer/pytorchTutorial/blob/master/05_1_gradientdescent_manually.py

import torch
import torch.nn as nn

# Compute every step manually

# Linear regression
# f = w * x 

# here : f = 2 * x
X = torch.tensor([[1], [2], [3], [4]], dtype=torch.float32)
Y = torch.tensor([[2], [4], [6], [8]], dtype=torch.float32)
X_test = torch.tensor([5],dtype=torch.float32)
n_samples,n_features=X.shape
print(n_samples,n_features)
input_size=n_features
output_size=n_features

model=nn.Linear(input_size,output_size)

#w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

# model output
#def forward(x):
#    return w * x

# loss = MSE
#def loss(y, y_pred):
#    return ((y_pred - y)**2).mean()
# Torch has standard gradients already implemented
# J = MSE = 1/N * (w*x - y)**2
# dJ/dw = 1/N * 2x(w*x - y)
#def gradient(x, y, y_pred):
#    return np.dot(2*x, y_pred - y).mean()

print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

# Training
learning_rate = 0.01
n_iters = 300
loss=nn.MSELoss()
optimizer=torch.optim.SGD(model.parameters(), lr=learning_rate)


for epoch in range(n_iters):
    # predict = forward pass
    y_pred = model(X)

    # loss
    l = loss(Y, y_pred)

    # gradients = backward pass
    l.backward() # dl/dw

    # update weights
    #with torch.no_grad():
    #    w -= learning_rate * w.grad
    optimizer.step()

    # zero grads
    #w.grad.zero_()
    optimizer.zero_grad()

    if epoch % 10 == 0:
        [w, b] = model.parameters() # unpack parameters
        print(f'epoch {epoch+1}: w (model.params) = {w[0][0].item():.3f}, loss = {l:.8f}')
     
print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')
