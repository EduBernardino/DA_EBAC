import pandas as pd
import matplotlib.pyplot as plt

# Criando Data Frame
gasolina_csv = "gasolina.csv"
df_gasolina = pd.read_csv(gasolina_csv)

# Separando os dados para montar o grafico
x = df_gasolina['dia']
y = df_gasolina['venda']

# Montando e salvando o Grafico
plt.plot(x, y, marker='o') 
plt.title('Gráfico Gasolina')  
plt.xlabel('Dia')  
plt.ylabel('Preço Gasolina') 
plt.grid(True) 
plt.savefig('gasolina.png')
plt.show() 
