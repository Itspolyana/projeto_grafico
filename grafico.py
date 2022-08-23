import matplotlib.pyplot as plt
import numpy 

nome_das_suas_colunas = ['JavaScript','Python','Java','C/C++']
valor_das_suas_colunas = [16.4, 11.3, 9.6,7.5]


#Estilo do tema
plt.style.use('dark_background')


# Barras na vertical
plt.barh(nome_das_suas_colunas,valor_das_suas_colunas , color = 'aqua')



plt.ylabel("Linguagens")
plt.title('LINGUAGENS MAIS USADAS')
plt.show()
