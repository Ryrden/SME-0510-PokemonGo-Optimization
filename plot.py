import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import networkx as nx

def plotTSP(sol, points):
    '''
    Função para plotar o gráfico do TSP
    '''
    x = []; y = []
    for i in sol:
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y, 'co')
    
    a_scale = float(max(x))/float(100)

    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width = a_scale, color ='g', length_includes_head=True)
    for i in range(0,len(x)-1):
        plt.arrow(x[i], y[i], (x[i+1] - x[i]), (y[i+1] - y[i]), 
            head_width = a_scale, color = 'g', length_includes_head = True)

    plt.xlim(min(x)*0.95, max(x)*1.05)
    plt.ylim(min(y)*0.95, max(y)*1.05)
    plt.show()
