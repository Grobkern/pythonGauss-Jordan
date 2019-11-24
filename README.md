# Gauss-Jordan python

## Introduction

> Example,nothing more

## Code Samples

    n = 1
    matrix = []
    def __init__(self,matrix):
        self.matrix = matrix
    def calculate(self):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])-1):
                while self.matrix[i][j]!=1:
                    self.matrix[i][len(self.matrix)-1] = float(float(self.matrix[i][len(self.matrix)-1]) / float(self.matrix[i][j]))
                    self.matrix[i][j] = float(self.matrix[i][j] * 1/self.matrix[i][j])
        print(self.matrix)

## Installation

> https://git-scm.com/docs/user-manual.html

https://git-scm.com/docs/user-manual.html