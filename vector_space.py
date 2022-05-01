import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp
import scipy.linalg
import sympy as sy
sy.init_printing() 

def vecSpaceAx7(u, v, c):
    fig, ax = plt.subplots(figsize = (7, 7))
    '''Syntax vecSpaceAx7(u, v, c), to demonstrate Axiom 7.'''
    ax.arrow(0, 0, u[0], u[1], color = 'red', width = .08, 
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)
    
    ax.arrow(0, 0, v[0], v[1], color = 'blue', width = .08, 
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)
    
    ax.arrow(0, 0, u[0]+v[0], u[1]+v[1], color = 'green', width = .08, 
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)
    
    ax.arrow(0, 0, c*u[0], c*u[1], color = 'red', width = .08, alpha=.5, 
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)
    
    ax.arrow(0, 0, c*v[0], c*v[1], color = 'blue', width = .08, alpha=.5, 
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)    
    ax.arrow(0, 0, c*(u[0]+v[0]), c*(u[1]+v[1]), color = 'green', width = .08, alpha=.5,  
         length_includes_head = True,
         head_width = .3, # default: 3*width
         head_length = .6,
         overhang = .4)
    
    ###########################Dashed Lines#################################
    point1 = [u[0], u[1]]
    point2 = [u[0] + v[0], u[1] + v[1]]
    line = np.array([point1, point2])
    ax.plot(line[:,0], line[:,1], ls = '--', lw = 3, color = 'red', alpha = .5)
    
    point1 = [v[0], v[1]]
    point2 = [u[0] + v[0], u[1] + v[1]]
    line = np.array([point1, point2])
    ax.plot(line[:,0], line[:,1], ls = '--', lw = 3, color = 'blue', alpha = .5)

    point1 = [c*v[0], c*v[1]]
    point2 = [c*(u[0] + v[0]),c*(u[1] + v[1])]
    line = np.array([point1, point2])
    ax.plot(line[:,0], line[:,1], ls = '--', lw = 3, color = 'blue', alpha = .5)

    point1 = [c*u[0], c*u[1]]
    point2 = [c*(u[0] + v[0]), c*(u[1] + v[1])]
    line = np.array([point1, point2])
    ax.plot(line[:,0], line[:,1], ls = '--', lw = 3, color = 'blue', alpha = .5)
    
    ####################################Text###############################
    
    ax.text(x = u[0], y = u[1], s = '$(%.0d, %.0d)$' % (u[0], u[1]), size = 16)
    ax.text(x = v[0], y = v[1], s = '$(%.0d, %.0d)$' % (v[0], v[1]), size = 16)
    ax.text(x = u[0]+v[0], y = u[1]+v[1], s = '$(%.0d, %.0d)$' % (u[0]+v[0], u[1]+v[1]), size = 16)    
    ax.text(x = c*u[0], y = c*v[1], s = '$(%.0d, %.0d)$' % (c*u[0], c*u[1]), size = 16) 
    ax.text(x = c*v[0], y = c*v[1], s = '$(%.0d, %.0d)$' % (c*v[0], c*v[1]), size = 16)     
    ax.text(x = c*(u[0]+v[0]), y = c*(u[1]+v[1]), s = '$(%.0d, %.0d)$' % (c*(u[0]+v[0]), c*(u[1]+v[1])), size = 16)     
    
    ax.set_title('Axiom: $c(\mathbf{u}+\mathbf{v})=c \mathbf{u}+c \mathbf{v}$', size = 19, color = 'red')
    
    ax.axis([0, np.max(c*u)+6, 0, np.max(c*v)+6])
    ax.grid(True)

    plt.show()
    
if __name__ == '__main__':
    u = np.array([2,3])
    v = np.array([3,1])
    c = 2
    vecSpaceAx7(u, v, c)