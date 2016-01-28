import sympy as sy
import numpy as np

def fun_1( 1100252):
    ans = hex(1100252)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-(sinx)**4), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,1,5,3,8,8,3,4,4,7], [1,2,6,6,4,3,9,2,5,1],[2,5,5,4,4,7,7,8,2,2],[7,7,2,3,6,7,1,8,8,5],[2,7,8,9,6,3,3,1,5,4],[1,1,5,6,6,9,9,4,3,8],[2,4,5,8,8,7,3,6,9,1],[4,5,1,2,3,8,9,7,7,7],[5,4,2,5,5,8,7,3,1,1],[4,4,6,3,8,2,5,9,6,6]] )
    b = np.array([9,8,6,5,2,2,3,3,1,7])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1100252
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
