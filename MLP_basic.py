import torch
EPOCHS = 1
learning_rate = 0.05

# The input/output tensor dose not require gradient modification
x = torch.tensor([[2, 3]], dtype = torch.float, requires_grad = False) 

y = torch.tensor([[1]], dtype = torch.float, requires_grad = False)

w1 = torch.tensor([[0.11, 0.12], [0.21,0.08]], dtype = torch.float, requires_grad = False)

w1 = torch.tensor([[0.14],[0.15]], dtype = torch.float, requires_grad = False)

for i in range(EPOCHS):
    y_pred = x.mm(w1).mm(w2)
    loss = (1/2)*(y-y_pred).pow(2).sum()
    
    print( 'LOSS : ', loss)
    loss.backward() # back propagation
    
    with torch.no_grad(): # auto gradient tracking off
        w1 -= w1.grad * learning_rate # Renewal of gradient
        w2 -= w2.grad * learning_rate
        
        # For next epoch, Initialize gradient
        w1.grad.zero_()
        w2.grad.zero_()
        
    
