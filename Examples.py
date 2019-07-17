m = Mandelbrot() #Create Mandelbrot object
zoom = [[(-2,-1),(1,1)],[(-0.25,0.6),(0,0.9)],[(-0.15,0.84),(-0.08,0.9)],[(-0.145,0.885),(-0.135,0.895)],[(-0.145,0.887),(-0.143,0.889)]] #Define the vertex for different zooms
i = 0
for z in zoom:
    i+=1
    m.reset(max_iter = 400, N_square = 701, l_vertex = z[0], r_vertex = z[1])
    m.compute_save(name = "Mandelbrot_"+str(i)+"_RedBlue")
    m.reset_cm(plt.cm.gnuplot)
    m.save_fig(name = "Mandelbrot_"+str(i)+"_gnuplot")