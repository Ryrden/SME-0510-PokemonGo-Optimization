import gurobipy as gp
from gurobipy import GRB
import time
import math

from plot import plotTSP

def find_next(X, j):
	for i in range(n):
		if round(X[j,i].X) == 1:
			next = i		
	return next

def ver_subtour(X,j):
	subtour = [j]
	next = find_next(X,j)
	while next != j:
		subtour.append(next)
		next = find_next(X,next)
	return subtour

def escreve_sol(X):
	solucao = []
	for j in range(n):
		j_sol = 0
		for i in range(len(solucao)):
			if j in solucao[i]:
				j_sol = 1			
		if j_sol == 0:
			subtour = ver_subtour(X,j)
			solucao.append(subtour)
	return solucao

with open('burma14.tsp', 'r') as f:
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

def exemplo1():
    model = gp.Model("Dantzig")
    gp.setParam('LogToConsole', 0)

    X = {}
    X = model.addVars(n,n,vtype=GRB.BINARY)

    distance = sum(X[j,i]*d[j][i] for j in range(n) for i in range(n))
    model.setObjective(distance, GRB.MINIMIZE)

    model.addConstrs(sum(X[j,i] for i in range(n)) == 1 for j in range(n))
    model.addConstrs(sum(X[j,i] for j in range(n)) == 1 for i in range(n))
    model.addConstrs(X[j,j] == 0 for j in range(n))
    model.update()

    start_time = time.time()

    while True:
        model.optimize()	
        solucao = escreve_sol(X)
        n_rotas = len(solucao)
        print("\nNúmero de rotas: "+str(n_rotas))
        print(solucao)
        print("Valor: "+str(model.objVAL))

        if n_rotas != 1:
            for r in range(n_rotas):
                model.addConstr(sum(X[j,i] for j in solucao[r] for i in solucao[r]) <= len(solucao[r]) - 1)
                model.update()
            else:
                break

    end_time = time.time()
    print("\nTempo total: "+str(round(end_time-start_time,2)))

def exemplo2():
    model = gp.Model("Dantzig")
    gp.setParam('LogToConsole', 0)

    X = {}
    X = model.addVars(n,n,vtype=GRB.BINARY)

    distance = sum(X[j,i]*d[j][i] for j in range(n) for i in range(n))
    model.setObjective(distance, GRB.MINIMIZE)

    model.addConstrs(sum(X[j,i] for i in range(n)) == 1 for j in range(n))
    model.addConstrs(sum(X[j,i] for j in range(n)) == 1 for i in range(n))
    model.addConstrs(X[j,j] == 0 for j in range(n))
    model.update()

    start_time = time.time()

    while True:
        model.optimize()	
        solucao = escreve_sol(X)
        n_rotas = len(solucao)
        print("\nNúmero de rotas: "+str(n_rotas))
        print(solucao)
        print("Valor: "+str(model.objVAL))
        if n_rotas != 1:
            for r in range(n_rotas):
                model.addConstr(sum(X[j,i] for j in solucao[r] for i in solucao[r]) <= len(solucao[r]) - 1)
                model.update()
        else:
            break

    end_time = time.time()
    print("\nTempo total: "+str(round(end_time-start_time,2)))

def exemplo3():
    model = gp.Model("MTZ")
    gp.setParam('LogToConsole', 0)

    X = {}
    X = model.addVars(n,n,vtype=GRB.BINARY)
    u = {}
    u = model.addVars(n,vtype=GRB.CONTINUOUS,lb=0)

    distance = sum(X[j,i]*d[j][i] for j in range(n) for i in range(n))
    model.setObjective(distance, GRB.MINIMIZE)

    model.addConstrs(sum(X[j,i] for i in range(n)) == 1 for j in range(n))
    model.addConstrs(sum(X[j,i] for j in range(n)) == 1 for i in range(n))
    model.addConstrs(X[j,j] == 0 for j in range(n))

    model.addConstrs(u[i] - u[j] <= n*(1-X[i,j]) - 1 
                    for j in range(n) for i in range(1,n) if i != j)

    model.update()

    start_time = time.time()
    model.optimize()	
    solucao = escreve_sol(X)
    n_rotas = len(solucao)
    print(solucao)
    print("Valor: "+str(model.objVAL))
    end_time = time.time()
    print("\nTempo total: "+str(round(end_time-start_time,2)))

    plotTSP(solucao[0], coord)


exemplo3()