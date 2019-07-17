# Mandelbrot
Autor : Arkaitz Bidaurrazaga Barrueta

This is a Python based program that computes and plots the Mandelbrot set. Different parameters can be determined, like cutoff parameters or colormap for the figure. 

REQUIREMENTS:
  -matplotlib
  -numpy
  
 INITIALIZE:
 
 The Mandelbrot set is the set of complex numbers "a" that do not diverge this expression : ![](https://latex.codecogs.com/gif.latex?z_%7Bi&plus;1%7D%20%3D%20z_i%5E2%20&plus;a)
 
 Thus we can use different criteria to determine if a number diverges that expression or not. In this program a number of iterations are computed untill a max_iter is achieved. Many initial values for z can also be chosen (z_0), and we can cut the iteration defining a maximum modulus (theoretically if ![](https://latex.codecogs.com/gif.latex?2%3C%7Cz_i%7C), then the expression will always diverge). All these parameters can be changed when initializing the Mandelbrot object, or with the reset() method (when reset is used, any parameter that is not specified will be set to the DEFAULT value.
 
 The grid in which the Mandelbrot set is calculated is specified with l_vertex and r_vertex, describing the rectangle in which the complex numbers will be considered. Also there are discretitation parameters: N_square, N_x and N_y; if N_square is determined the other to are ignored, and the same number of points are considered for both directions.
 
 Finally, we can choose the colormap for the figure with the parameter cm. In order to see which colormap you would like to use see: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
 
 DEFAULT VALUES:
 
 - start = complex(0,0)
 - max_iter = 500
 - ax_modul = 2
 - N_square = 301
 - N_x = 301, N_y = 301
 - l_vertex = (-1.5,-1), r_vertex = (0.5,1)
 - cm = plt.cm.RdBu
 
 *Stimated time needed to compute the set with the DEFAULT values = 7 s*
 
 METHODS:
 
 - compute_save(directory = os.path.join(os.getenv("HOME"),"Mandelbrot"),
 name = "Mandelbrot", title = "Mandelbrot", file_format = "png",verbose = 0) : Computes the set and saves the plot. 
 With verbose = 1 prints the time it took to compute the set.
 
 - make_set() : Generates the set of points that describe the complex numbers.
 
 - compute_set() : Calculates the Mandelbrot set.
 
 - plot(size = (12,12) : Plots the Mandelbrot set without saving in file (size describes the size in which will be ploted in screen). make_set() and compute_set() must be called before using this method.
 
 - save_fig(directory = os.path.join(os.getenv("HOME"),"Mandelbrot"),name = "Mandelbrot", title = "Mandelbrot", file_format = "png") : Saves the figure, same requirement as plot().
 
 -reset_cm(cm): Reset the colormap, this helps if you have already computed the Mandelbrot set and you want to try different colormaps on the plot.
 
 
