import time
import random
import math
import matplotlib.pyplot as plt


#This Program has been written by-
# Mrinal Kanti Sadhukhan, NIT Bhopal
# M.Tech CSE (Advanced Computing) 2021-2023
# Scholar Number- 212112313


'''
Uncomment The Required Test Function and
Comment out Unnecessary Functions to
Work with this
'''
#Currently working with Beale Function
dimension=1
def func(X):
    s=0 
    x=X[0]
    y=X[1]
    '''
    #SPHERE FUNC
    for i in range(len(X)):
        s+=X[i]*X[i]
    
    #ROSENBROCK FUNC
    for i in range(len(X)-1):
        s+=100*pow(X[i+1]-X[i]*X[i],2)+pow(1-X[i],2)

    #RASTRIGIN FUNC
    for x in X:
        s+=pow(x,2)-10*math.cos(2*math.pi*x);
    s+=10*dimension
    '''
    
    #BEALE FUNC 
    s=pow(1.5-x+x*y,2)+pow(2.25-x+x*y*y,2)+pow(2.625-x+x*pow(y,3),2)
    
    '''
    #BOOTH FUNC
    s=pow(x+2*y-7,2)+pow(2*x+y-5,2)
    
    #Himmelblau's function
    s=pow(x*x+y-11,2)+pow(x+y*y-7,2)
    
    #EASOM Func
    s=-math.cos(x)*math.cos(y)*math.exp(-(pow(x-math.pi,2)+pow(y-math.pi,2)))
    
    #Egg holder Func
    s=-(y+47)*math.sin(math.sqrt(abs(x/2+y+47)))-x*math.sin(math.sqrt(abs(x-y+47)))
    
    #HOLDER TABLE Func
    s=-abs(math.sin(x)*math.cos(y)*math.exp(abs(1-math.sqrt(x*x+y*y)/math.pi)))
    '''
    
    return s



pop=int(input('Enter Population:'))  #Initial population size
dimension=c=int(input('Enter Dimension:')) #Dimension
lowBound=-4.5
upperBound=4.5
#startTime = time.perf_counter()
matrix=[]
solution=[]

#Generating Initial Random Solutions:
for i in range(pop):
    rows=[]
    for j in range(c):
        rows.append(random.uniform(lowBound,upperBound))
    
    matrix.append(rows)
    solution.append(func(rows))

itr=int(input('Iteration:'))


xvals=[]
yvals=[]
itrCount=0
b=0
w=0

while itr:
    itr-=1
    
    #Finding index of best and worst solution
    for i in range(pop):
        if(solution[i]<solution[b]):b=i
        if(solution[i]>solution[w]):w=i
    
    #Update all solutions according to the best and worst;
    #when new solutions are better
    for i in range(pop):
        newSolution=[]
        flag=True
        for j in range(c):
            r1=random.random()
            r2=random.random()
            temp=(matrix[i][j]+r1*(matrix[b][j]-abs(matrix[i][j]))-r2*(matrix[w][j]-abs(matrix[i][j])))
            if(temp>upperBound or temp <lowBound):
                flag=False
                break;
            else: newSolution.append(temp)
        if(flag):
            newSolutionValue=func(newSolution)
            if(newSolutionValue<solution[i]):
                matrix[i]=newSolution
                solution[i]=newSolutionValue

    xvals.append(itrCount)
    yvals.append(solution[b])
    itrCount+=1
    
    print("*******After ",itrCount,"********")
    for i in range(pop):
        for j in range(c):
            print(matrix[i][j],end=' ')
        print(solution[i])
        print()
    print("Previous Best value:",solution[b]," Worst: ",solution[w])
    
print('Best Solution found :')
for i in range(c):
    print(f'{matrix[b][i]:.20f}',end=' ')
print(f'{solution[b]:.20f}')
plt.plot(xvals,yvals,'-b')
plt.show()
            
        
        
