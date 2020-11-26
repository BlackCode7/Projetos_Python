#!/usr/bin/env python
# coding: utf-8

# In[3]:


vogais = ['a', 'e', 'i', 'o', 'u']
palavra = input('Digite uma palavra qualquer: ')
palavraVazia = []

# função para caçar vogais dentro de palavras
def cacaPalavra():
    #verificação de vogais dentro da variável palavra
    for letra in palavra:
        # se a letra estiver dentro da variável vogais
        if letra in vogais:
            # se a letra não estiver dentro da variável palavraVazia
            if letra not in palavraVazia:
                # se a letra foi achada fazer o apendice dela detro da variavel palavravazia.append(letra)
                palavraVazia.append(letra)
    # Se letra estiver dentro da palavraVazia vai mostrar o que achou
    for letra in palavraVazia:
        print(letra)
        
cacaPalavra()


# In[ ]:





# In[ ]:




