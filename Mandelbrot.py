import os
import matplotlib.pyplot as plt
import random
import numpy as np
import time


#Object to obtain and plot Mandelbrot set by : Arkaitz Bidaurrazaga Barrueta
#z0 will be the initial value and a will be the varying complex number that will be checked : z_i+1=z_i^2+a
#The cutoff criteria may depend on the modulus and interation number
class Mandelbrot():
    
    def __init__(self,start = complex(0,0), max_iter = 500, max_modul = 2, N_square = 301, 
                 N_x = 301, N_y = 301, l_vertex = (-1.5,-1), r_vertex = (0.5,1), cm = plt.cm.RdBu):
        self.start = start #Where to start the iteration : z0
        self.set = list() #Here the set will be saved in order to later plot
        self.max_iter = max_iter #Iteration cutoff
        self.max_modul = max_modul #Modulus cutoff
        self.N_square = N_square #Square discretitation for both xy direction
        if N_square != 301 : 
            self.N_x = N_square
            self.N_y = N_square
        else:
            self.N_x = N_x
            self.N_y = N_y
        self.left_vertex = l_vertex #The vertex of the rectangle in the left-downside
        self.right_vertex = r_vertex #The vertex of the rectangle in the right-upside
        self.cm = cm #Defines the colormap used to plot the set
        
    def reset(self,start = complex(0,0), max_iter = 500, max_modul = 2, N_square = 301, 
              N_x = 301, N_y = 301, l_vertex = (-1.5,-1), r_vertex = (0.5,1), cm = plt.cm.RdBu):
        self.start = start #Where to start the iteration : z0
        self.set = list() #Here the set will be saved in order to later plot
        self.max_iter = max_iter #Iteration cutoff
        self.max_modul = max_modul #Modulus cutoff
        self.N_square = N_square #Square discretitation for both xy direction
        if N_square != 301 : 
            self.N_x = N_square
            self.N_y = N_square
        else:
            self.N_x = N_x
            self.N_y = N_y
        self.left_vertex = l_vertex #The vertex of the rectangle in the left-downside
        self.right_vertex = r_vertex #The vertex of the rectangle in the right-upside
        self.cm = cm #Defines the colormap used to plot the set
        
    def reset_cm(self,cm): #This helps trying different colormaps after a set has been computed
        self.cm = cm
        
    def make_set(self): #Generates the set of complex points, the value in the dictionary will be the iteration number obtained from cutoff criteria
        diff_x = (self.right_vertex[0]-self.left_vertex[0])/self.N_x
        diff_y = (self.right_vertex[1]-self.left_vertex[1])/self.N_y
        self.set = [[self.left_vertex[0]+i*diff_x,self.left_vertex[1]+j*diff_y,0] 
                    for j in range(self.N_y) for i in range(self.N_x)]
        
    def plot(self,size = (12,12)): #Plots the set
        fig = plt.figure(figsize=size)
        im = plt.imshow(np.array(self.set)[:,-1].reshape((self.N_x,self.N_y)),cmap=self.cm,
                        extent=(self.left_vertex[0], self.right_vertex[0], self.right_vertex[1],self.left_vertex[1]))
        plt.gca().invert_yaxis()
        plt.colorbar(im)
        plt.title('Mandelbrot')
        plt.show()
        
    def save_fig(self,directory = os.path.join(os.getenv("HOME"),"Mandelbrot"),
                 name = "Mandelbrot", title = "Mandelbrot", file_format = "png"):
        os.makedirs(directory, exist_ok=True)
        fig = plt.figure(figsize=(12,12))
        im = plt.imshow(np.array(self.set)[:,-1].reshape((self.N_x,self.N_y)),cmap=self.cm, 
                        extent=(self.left_vertex[0], self.right_vertex[0], self.right_vertex[1],self.left_vertex[1]))
        plt.gca().invert_yaxis()
        plt.colorbar(im)
        plt.title(title)
        plt.savefig(fname = os.path.join(directory,name),format = file_format)
        
    def next_iter(self,z,a): #Computes next number to check
        return z**2+a
    
    def check(self,index): #Checks if a complex number is in the Mandelbrot set
        z_i = self.start
        a = complex(self.set[index][0],self.set[index][1])
        iteration = 0
        while iteration < self.max_iter and abs(z_i)<self.max_modul:
            z_i = self.next_iter(z_i,a)
            iteration+=1
        self.set[index][-1] = iteration/float(self.max_iter)
    
    def compute_set(self,verbose = 1): #Checks every point
        start = time.time()
        for index in range(len(self.set)):
            self.check(index)
        end = time.time()
        if verbose:
            print("Time: %s s ; %s min " %((end-start),(end-start)/60))
            
    def compute_save(self,directory = os.path.join(os.getenv("HOME"),"Mandelbrot"),
                     name = "Mandelbrot", title = "Mandelbrot", file_format = "png",verbose = 0): #Compute and save at once
        self.make_set()
        self.compute_set(verbose)
        self.save_fig(directory,name,title,file_format)