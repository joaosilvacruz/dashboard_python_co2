#!/usr/bin/env python
# coding: utf-8

# In[201]:


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
    
    lista_x = x.copy()
    lista_x.append(soma_x)
    lista_y = y.copy()
    lista_y.append(soma_y)
    lista_xy.append(soma_xy)
    lista_x_qd.append(soma_x_qd)
    lista_SQREG.append(soma_sqREG)
    lista_SQTOT.append(soma_sqTOT)

    return a, b, new_y, r_qd, lista_x, lista_y, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[159]:


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
    
    lista_x = x.copy()
    lista_x.append(sum(x))
    lista_new_x = new_x.copy()
    lista_new_x.append(soma_x)
    lista_y = y.copy()
    lista_y.append(sum(y))
    lista_xy.append(soma_xy)
    lista_x_qd.append(soma_x_qd)
    lista_SQREG.append(soma_sqREG)
    lista_SQTOT.append(soma_sqTOT)
    
    return a, b, new_x, new_y, r_qd, lista_x, lista_new_x, lista_y, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[1]:


#mmq exponencial
def exp(x,y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(x):
        return a*x+b_

    new_y = []
    for i in range(0,n):
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
    
    lista_x = x.copy()
    lista_x.append(sum(x))
    lista_new_y = new_y.copy()
    lista_new_y.append(soma_y)
    lista_y = y.copy()
    lista_y.append(sum(y))
    lista_xy.append(soma_xy)
    lista_x_qd.append(soma_x_qd)
    lista_SQREG.append(soma_sqREG)
    lista_SQTOT.append(soma_sqTOT)
    
    return a, b, new_y, new_y2, r_qd, lista_x, lista_y, lista_new_y, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[211]:



def pot(x,y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(x):
        return a*x+b_
    
    lista_y = y.copy()

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
    
    lista_x = x.copy()
    lista_x.append(sum(x))
    lista_new_y = new_y.copy()
    lista_new_y.append(soma_y)
    lista_new_x = new_x.copy()
    lista_new_x.append(sum(new_x))
    lista_y.append(sum(y))
    lista_xy.append(soma_xy)
    lista_x_qd.append(soma_x_qd)
    lista_SQREG.append(soma_sqREG)
    lista_SQTOT.append(soma_sqTOT)

    return a, b, new_x, new_y, new_y2, r_qd, lista_x, lista_new_x, lista_y, lista_new_y, lista_xy, lista_x_qd, lista_SQREG, lista_SQTOT, fx, valor_estimado


# In[139]:


def subs_retro(A,b):
    n = len(A)
    x = n * [0]
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j] * x[j]
        x[i] = (b[i] - soma)/A[i][i]         
    return x


# In[140]:


def elim_gauss(A,b):
    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            pivo = A[k][k]
            mult_linha = A[i][k]/pivo
            for j in range(k+1, n):
                A[i][j] = A[i][j] - mult_linha *  A[k][j] 
            b[i] = b[i] - mult_linha * b[k]
            A[i][k] = 0
    x = subs_retro(A,b)
    return x


# In[236]:


def log_2grau(x, y, valor = 1, estimar = False):
    import numpy as np
    n = len(x)
    def g(a,b,c,x):
        return a*x**2+b*x+c

    lista_xy = []
    for i in range(0,n):
        xy = x[i] * y[i]
        lista_xy.append(xy)

    lista_x_qd = []
    for i in range(0,n):
        x_qd = x[i]**2
        lista_x_qd.append(x_qd)
    
    lista_x_qdy = []
    for i in range(0,n):
        x_qdy = x[i]**2 * y[i]
        lista_x_qdy.append(x_qdy)
        
    lista_x_cb = []
    for i in range(0,n):
        x_cb = x[i]**3
        lista_x_cb.append(x_cb)
    
    lista_x_quarta = []
    for i in range(0,n):
        x_quarta = x[i]**4
        lista_x_quarta.append(x_quarta)
        
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(lista_xy)
    soma_x_qd= sum(lista_x_qd)
    soma_x_qdy= sum(lista_x_qdy)
    soma_x_cb= sum(lista_x_cb)
    soma_x_quarta= sum(lista_x_quarta)

    matriz_a = [[],[],[]]
    matriz_b = []
    
    matriz_a[0].append(soma_x_quarta)
    matriz_a[0].append(soma_x_cb)
    matriz_a[0].append(soma_x_qd)
    
    matriz_a[1].append(soma_x_cb)
    matriz_a[1].append(soma_x_qd)
    matriz_a[1].append(soma_x)
    
    matriz_a[2].append(soma_x_qd)
    matriz_a[2].append(soma_x)
    matriz_a[2].append(n)
    
    matriz_b.append(soma_x_qdy)
    matriz_b.append(soma_xy)
    matriz_b.append(soma_y)
    
    matriz_x = elim_gauss(matriz_a,matriz_b)
    
    c = matriz_x[2]
    b = matriz_x[1]
    a = matriz_x[0]
    
    new_y = []
    for i in range(0,n):
        newy = g(a,b,c,x[i])
        new_y.append(newy)

    lista_SQREG =[]
    for i in range(0,n):
        sqreg = ((g(a,b,c,x[i]) - np.mean(y))**2)
        lista_SQREG.append(sqreg)
      
    lista_SQTOT = []
    for i in range(0,n):
        sqtot = (((y[i]) - np.mean(y))**2)
        lista_SQTOT.append(sqtot)  

    soma_sqREG = sum(lista_SQREG)
    soma_sqTOT = sum(lista_SQTOT)
    r_qd = soma_sqREG/soma_sqTOT
    fx=f'{a}*x²+{b}*x+{c}'
    
    lista_x = x.copy()
    lista_x.append(sum(x))
    lista_y = y.copy()
    lista_y.append(sum(y))
    lista_xy.append(soma_xy)
    lista_x_qdy.append(soma_x_qdy)
    lista_x_qd.append(soma_x_qd)
    lista_x_cb.append(soma_x_cb)
    lista_x_quarta.append(soma_x_quarta)
    lista_SQREG.append(soma_sqREG)
    lista_SQTOT.append(soma_sqTOT)
    
    return a, b, c, new_y, lista_x, lista_y, lista_xy, lista_x_qd, lista_x_qdy, lista_x_cb, lista_x_quarta, lista_SQREG, lista_SQTOT, r_qd, fx

