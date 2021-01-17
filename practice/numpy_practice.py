
import numpy as np


# Main:
if __name__== "__main__":
    # https://towardsdatascience.com/building-linear-regression-least-squares-with-linear-algebra-2adf071dd5dd
    # best fit for [0,3],[1,5], is y = 2x + 3
    # X betas = y -> XT X betas = XT y -> betas = (XT X) XT y
    X = np.array([[0, 1], [1, 1]])
    XT = np.matrix.transpose(X)
    y = np.array([[3], [5]])
    XT_X = np.matmul(XT, X)
    XT_y = np.matmul(XT, y)
    #[m b] = (XT X)**-1 XT Y
    b_array = np.matmul(np.linalg.inv(np.matmul(np.matrix.transpose(X), X)), np.matmul(np.matrix.transpose(X), y))
    print("b_array =", b_array)
    betas = np.matmul(np.linalg.inv(XT_X), XT_y)
    print("betas =", betas)

