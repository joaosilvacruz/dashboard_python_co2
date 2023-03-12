#!/usr/bin/env python
# coding: utf-8

# In[3]:


#mmq linear
def linear(x,y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)

    def g(x):
        return a*x+b

    lista_xy = []
    for i in range(0,n):
        xy = x[i] * y[i]
        lista_xy.append(xy)

    lista_x_qd = []
    for i in range(0,n):
        x_qd = x[i] * x[i]
        lista_x_qd.append(x_qd)

    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(lista_xy)
    soma_x_qd= sum(lista_x_qd)

    a = (n*soma_xy - soma_x*soma_y)/(n*soma_x_qd - (soma_x **2))
    b = (soma_x*soma_xy-soma_y*soma_x_qd)/((soma_x**2)-n*soma_x_qd)

    new_y = []
    for i in range(0,n):
        x_= x[i]
        new_y.append(g(x_))

    lista_SQREG =[]
    for i in range(0,n):
        sqreg = ((g(x[i]) - np.mean(y))**2)
        lista_SQREG.append(sqreg)
  
    lista_SQTOT = []
    for i in range(0,n):
        sqtot = (((y[i]) - np.mean(y))**2)
        lista_SQTOT.append(sqtot)  

    soma_sqREG = sum(lista_SQREG)
    soma_sqTOT = sum(lista_SQTOT)
    r_qd = soma_sqREG/soma_sqTOT
    
    valor_estimado = 1
    if estimar == True:
        valor_estimado = g(valor) 
    
    fx = f'({a}*x) + ({b})'


    return a, b, soma_x, soma_y, soma_xy, soma_x_qd, new_y, r_qd, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[6]:


#mmq logaritmica


def log(x, y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(x):
        return a*np.log(x)+b

    new_x = []
    for i in range(0,n):
        x_ = np.log(x[i])
        new_x.append(x_)

    lista_xy = []
    for i in range(0,n):
        xy = new_x[i] * y[i]
        lista_xy.append(xy)

    lista_x_qd = []
    for i in range(0,n):
        x_qd = new_x[i] * new_x[i]
        lista_x_qd.append(x_qd)

    soma_x = sum(new_x)
    soma_y = sum(y)
    soma_xy = sum(lista_xy)
    soma_x_qd= sum(lista_x_qd)

    a = (n*soma_xy - soma_x*soma_y)/(n*soma_x_qd - (soma_x **2))
    b = (soma_x*soma_xy-soma_y*soma_x_qd)/((soma_x**2)-n*soma_x_qd)

    new_y = []
    for i in range(0,n):
        y_ = a*new_x[i]+b
        new_y.append(y_)
  
    new_x2 = []
    for i in range(0,n):
        x_2 = np.exp(x[i])
        new_x2.append(x_2)

    lista_SQREG =[]
    for i in range(0,n):
        sqreg = ((g(x[i]) - np.mean(y))**2)
        lista_SQREG.append(sqreg)
    
    lista_SQTOT = []
    for i in range(0,n):
        sqtot = (((y[i]) - np.mean(y))**2)
        lista_SQTOT.append(sqtot)  

    soma_sqREG = sum(lista_SQREG)
    soma_sqTOT = sum(lista_SQTOT)
    r_qd = soma_sqREG/soma_sqTOT
    
    fx = f'({a}*ln(x) + ({b})'
    
    valor_estimado = 1
    if estimar == True:
        valor_estimado = g(valor) 
    
    #return  a, b, soma_x, soma_y, soma_xy, soma_x_qd, new_y, r_qd
    return  a, b, soma_x, soma_y, soma_xy, soma_x_qd, new_y, r_qd, new_x, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[5]:


#mmq exponencial
def exp(x,y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(x):
        return a*x+b_

    new_y = []
    for i in range(0,n):
        ####SE INFORMAR SE ISSO ESTÁ CORRETO####
        if y[i] == 0:
            y[i] = 1
        ####SE INFORMAR SE ISSO ESTÁ CORRETO####
        y_ = np.log(y[i])
        new_y.append(y_)

    lista_xy = []
    for i in range(0,n):
        xy = x[i] * new_y[i]
        lista_xy.append(xy)

    lista_x_qd = []
    for i in range(0,n):
        x_qd = x[i] * x[i]
        lista_x_qd.append(x_qd)

    soma_x = sum(x)
    soma_y = sum(new_y)
    soma_xy = sum(lista_xy)
    soma_x_qd= sum(lista_x_qd)

    a = (n*soma_xy - soma_x*soma_y)/(n*soma_x_qd - (soma_x **2))
    b_ = (soma_x*soma_xy-soma_y*soma_x_qd)/((soma_x**2)-n*soma_x_qd)
    b = np.exp(b_)

    lista_SQREG =[]
    for i in range(0,n):
        sqreg = ((g(x[i]) - np.mean(new_y))**2)
        lista_SQREG.append(sqreg)
    
    lista_SQTOT = []
    for i in range(0,n):
        sqtot = (((new_y[i]) - np.mean(new_y))**2)
        lista_SQTOT.append(sqtot)  

    soma_sqREG = sum(lista_SQREG)
    soma_sqTOT = sum(lista_SQTOT)
    r_qd = soma_sqREG/soma_sqTOT

    new_y2 = []
    for i in range(0,n):
        y_2 = b*np.exp(a*x[i])
        new_y2.append(y_2) 
        
    fx = f'{b}*e^({a}*x)'
    
    valor_estimado = 1
    if estimar == True:
        valor_estimado = b*np.exp(a*valor)
    
    return a, b, soma_x, soma_y, soma_xy, soma_x_qd, new_y2, r_qd, new_y, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[7]:



def pot(x,y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(x):
        return a*x+b_

    new_y = []
    for i in range(0,n):
        y_ = np.log(y[i])
        new_y.append(y_)

    new_x = []
    for i in range(0,n):
        x_ = np.log(x[i])
        new_x.append(x_)

    y2 = y.copy()

    lista_xy = []
    for i in range(0,n):
        xy = new_x[i] * new_y[i]
        lista_xy.append(xy)

    lista_x_qd = []
    for i in range(0,n):
        x_qd = new_x[i] * new_x[i]
        lista_x_qd.append(x_qd)

    soma_x = sum(new_x)
    soma_y = sum(new_y)
    soma_xy = sum(lista_xy)
    soma_x_qd= sum(lista_x_qd)

    a = (n*soma_xy - soma_x*soma_y)/(n*soma_x_qd - (soma_x **2))
    b_ = (soma_x*soma_xy-soma_y*soma_x_qd)/((soma_x**2)-n*soma_x_qd)
    b = np.exp(b_)

    new_y2 = []
    for i in range(0,n):
        y_a_usar2 = b*(x[i]**a)
        new_y2.append(y_a_usar2) 

    lista_SQREG =[]
    for i in range(0,n):
        sqreg = ((g(new_x[i]) - np.mean(new_y))**2)
        lista_SQREG.append(sqreg)
      
    lista_SQTOT = []
    for i in range(0,n):
        sqtot = (((new_y[i]) - np.mean(new_y))**2)
        lista_SQTOT.append(sqtot)  

    soma_sqREG = sum(lista_SQREG)
    soma_sqTOT = sum(lista_SQTOT)
    r_qd = soma_sqREG/soma_sqTOT
    
    fx=f'{b}*x^{a}'
            
    valor_estimado = 1
    if estimar == True:
        valor_estimado = b*(valor**a)


    return a, b, soma_x, soma_y, soma_xy, soma_x_qd, new_x, r_qd, new_y, new_y2, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado
  


# In[ ]:




