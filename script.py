import gurobipy as gp
from gurobipy import GRB
import time
import math

from plot import plotTSP

def find_next(X, j):
    '''
    Essa função retorna o próximo ponto focal a ser visitado
    '''
    for i in range(n):
        if round(X[j,i].X) == 1:
            next = i		
    return next

def display_subtour(X,j):
    '''
    Essa função retorna a rota a ser percorrida
    '''
    subtour = [j]
    next = find_next(X,j)
    while next != j:
        subtour.append(next)
        next = find_next(X,next)
    return subtour

def write_solution(X):
    '''
    Essa função retorna a solução do problema
    '''
    solution = []
    for j in range(n):
        j_sol = 0
        for i in range(len(solution)):
            if j in solution[i]:
                j_sol = 1			
        if j_sol == 0:
            subtour = display_subtour(X,j)
            solution.append(subtour)
    return solution

# Le as coordenadas do arquivo e salva na variável data
with open('coordinates_map.tsp', 'r') as f:
    data = [[num for num in line.split()] for line in f]

n = int(data[3][-1])

coord = []
for j in range(n):
    coord.append([])
    coord[j].append(float(data[j+6][-2]))
    coord[j].append(float(data[j+6][-1]))
d = []

for j in range(n):
    d.append([])
    for i in range(n):
        dist = math.sqrt( ((coord[j][0]-coord[i][0])**2)+((coord[j][1]-coord[i][1])**2) )
        d[j].append(dist)

def addConstraints(model, X, u):
     # Essa constraint garante que exista uma viagem de chegada para cada ponto focal
    model.addConstrs(sum(X[j,i] for i in range(n)) == 1 for j in range(n))

    # Essa constraint garante que exista uma viagem saindo de cada ponto focal
    model.addConstrs(sum(X[j,i] for j in range(n)) == 1 for i in range(n))

    # Essa constraint garante que não exista uma viagem de um ponto X ao mesmo ponto X
    model.addConstrs(X[j,j] == 0 for j in range(n))

    # Essa constraint garante a sequência de idas a pontos focais descrita no início do documento
    model.addConstrs(X[i,i+1] == 1 for i in range(4, 11))

    # Essa constraint garante a inexistência de subtours descritos no documento
    model.addConstrs(u[i] - u[j] <= n*(1-X[i,j]) - 1
                    for j in range(n) for i in range(1,n) if i != j)

    model.update()


def solve():
    model = gp.Model("Dantzig")
    gp.setParam('LogToConsole', 0)

    X = {}
    X = model.addVars(n,n,vtype=GRB.BINARY)
    u = {}
    u = model.addVars(n,vtype=GRB.CONTINUOUS,lb=0)

    distance = sum(X[j,i]*d[j][i] for j in range(n) for i in range(n))

    # Objetivo é minimizar a distância (distance)
    model.setObjective(distance, GRB.MINIMIZE)

    addConstraints(model, X, u)

    start_time = time.time()

    while True:
        model.optimize()	
        solution = write_solution(X)
        number_of_routes = len(solution)
        print("\nNúmero de rotas: "+str(number_of_routes))
        print(solution)
        print("Valor: "+str(model.objVAL))
        if number_of_routes != 1:
            for r in range(number_of_routes):
                model.addConstr(sum(X[j,i] for j in solution[r] for i in solution[r]) <= len(solution[r]) - 1)
                model.update()
        else:
            break

    end_time = time.time()
    print("\nTempo total: "+ str(round(end_time-start_time,2)) + "segundos")

    plotTSP(solution[0], coord)

solve()