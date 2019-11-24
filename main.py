import numpy as np
class Calculate:
    n = 1
    matrix = []
    def __init__(self,matrix):
        self.matrix = matrix
    def calculate(self):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])-1):
                # a = float(self.matrix[i][j])
                while self.matrix[i][j]!=1:
                    self.matrix[i][len(self.matrix)-1] = float(float(self.matrix[i][len(self.matrix)-1]) / float(self.matrix[i][j]))
                    self.matrix[i][j] = float(self.matrix[i][j] * 1/self.matrix[i][j])
        print(self.matrix)
class onStartup:
    @staticmethod
    def size(n):
        mainMatrix = np.zeros((int(n),int(n)))
        # r = float(0)  
        # mainMatrix = []
        # for i in range(n):
        #     mainMatrix.append([])
        #     for j in range(n):
        #         mainMatrix[i].append(r)
        print(type(mainMatrix))
        for i in range(len(mainMatrix)):
            for j in range(len(mainMatrix[i])):
                mainMatrix[i][j] = float(input("matrix[][] = "))
        print(mainMatrix)
        print(mainMatrix[0][1])
        main = Calculate(mainMatrix)
        main.calculate()
n = int(input("n:"))
onStartup.size(n)