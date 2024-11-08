import daceypy_import_helper
from daceypy import DA,array
import numpy

# Make a function that performs the polar transformation (take in and then return an array) --DONE
# Separate Jacobian function (takes in DA array, outputs Jacobian matrix (1st coefficients of DA array)) --DONE
# getCoefficient, deriv, look for other QofL functions in DA class --DONE
# For second order tensors, the coefficient is spit among the number of permutationss --DONE
# da.linear should produce the same output as jacobian... use this to double check your work --DONE
# By next week, push code and let Dr. Kulik know when it's pushed --DONE

# Then make the Jacobian applicable  in higher orders (multi-dimensional array)

def first_order_jacobian(array):
    jacobian = []
    for i in range(len(array)):
        x_i = ([])
        x_i.append(array[i].getCoefficient([1,0]))
        x_i.append(array[i].getCoefficient([0,1]))
        jacobian.append(x_i)
    return jacobian

def sopdt(array): # Second-Order-Partial_Derivative_Tensor
    tensor = []
    for i in range(len(array)):
        matrix_i = []
        x_i = []
        y_i = []
        x_i.append(array[i].getCoefficient([2,0]))
        x_i.append(array[i].getCoefficient([1,1])/2)  #Since these 2 terms reference the same coefficient, they need to be split among each other
        y_i.append(array[i].getCoefficient([1, 1])/2)
        y_i.append(array[i].getCoefficient([0, 2]))
        matrix_i.append(x_i)
        matrix_i.append(y_i)
        tensor.append(matrix_i)
    return tensor

def polar_transformation(coords):
    r = (coords[0].sqr() + coords[1].sqr()).sqrt()
    theta = (coords[0]/coords[1]).arctan()
    polar_coords = [r,theta]
    return polar_coords


def main():

    DA.init(2, 2)

    cartesian = [1 + DA(1), 1+ DA(2)]
    polar = polar_transformation(cartesian)

    print(f"x\n{cartesian[0]}\n")
    print(f"y\n{cartesian[1]}\n")

    print(f"r\n{polar[0]}\n")
    print(f"theta\n{polar[1]}\n")

    jacobian = first_order_jacobian(polar)

    print(jacobian)
    print(sopdt(polar))
    ## Uncomment these to test first order Jacobian
    # print(polar[0].linear())
    # print(polar[1].linear())

if __name__ == "__main__":
    main()
