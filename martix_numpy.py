import numpy as np

def random_3d_matrix(rand, size):
    return np.random.randint(rand, size=(size,size,size))

def max_sum_over_axis(M):
    """
    Calculates indices of an element with max sum over orthogonal axes

    >>> import numpy as np; M = np.arange(10**3).reshape(10,10,10); max_sum_over_axis(M)
    (9, 9, 9)

    :param M: 3-dimensional ndarray
    :return: x, y, z - coordinates of an element with max sum over orthogonal axes
    """
    n = len(M)
    z_axis_sum = M.sum(0)
    y_axis_sum = M.sum(1)
    x_axis_sum = M.sum(2)
    i,j,k = 0,0,0
    max = 0
    for z in range(n):
        for y in range(n):
            for x in range(n):
                sum = z_axis_sum[y][x] + y_axis_sum[z][x] + x_axis_sum[z][y]
                if sum > max:
                    max = sum
                    i,j,k = x,y,z
    return i,j,k

if __name__=="__main__":
    import doctest
    doctest.testmod()
    M = random_3d_matrix(10,10)
    print(max_sum_over_axis(M))