# Splines_approximator

Approximate the function  $f_{real}(x)= \frac{\sin(12(x+0.2))}{(x+0.2)}$ using natural cubic splines as described in Chapter 5.2.1 of [The Elements of Statistical Learning](https://link.springer.com/book/10.1007/978-0-387-84858-7).


![figure](https://github.com/antvas98/Splines_approximator/assets/115734703/bb5c8322-ba0c-4144-a47d-6ef6ca802fe2)

## Equations

1. ![Equation 1](https://latex.codecogs.com/svg.latex?f(x)%20%3D%20%5Csum_%7Bj%3D1%7D%5EN%20N_j(x)%20%5Ctheta_j)

2. ![Equation 2](https://latex.codecogs.com/svg.latex?N_1(X)%20%3D%201%2C%20N_2(X)%20%3D%20X%2C%20N_%7Bk%2B2%7D(X)%20%3D%20d_k(X)%20-%20d_%7BK-1%7D(X))

3. ![Equation 3](https://latex.codecogs.com/svg.latex?d_k(X)%20%3D%20%5Cfrac%7B(X%20-%20%5Cxi_k)%5E3%20-%20(X%20-%20%5Cxi_K)%5E3%7D%7B%5Cxi_K%20-%20%5Cxi_k%7D)

4. ![Equation 4](https://latex.codecogs.com/svg.latex?RSS(f%2C%20%5Clambda)%20%3D%20%5Csum_%7Bi%3D1%7D%5EN%20%5Cleft(y_i%20-%20f(x_i)%5Cright)%5E2%20%2B%20%5Clambda%20%5Cint%20%5Cleft(f%27%27(t)%5Cright)%5E2%20dt)

5. ![Equation 5](https://latex.codecogs.com/svg.latex?RSS(%5Ctheta%2C%20%5Clambda)%20%3D%20(y%20-%20N%5Ctheta)%5ET%20(y%20-%20N%5Ctheta)%20%2B%20%5Clambda%20%5Ctheta%5ET%20%5COmega_N%20%5Ctheta)

6. ![Equation 6](https://latex.codecogs.com/svg.latex?RSS(%5Ctheta%2C%20%5Clambda)%20%3D%20(y%20-%20N%5Ctheta)%5ET%20(y%20-%20N%5Ctheta)%20%2B%20%5Clambda%20%5Ctheta%5ET%20%5COmega_N%20%5Ctheta)

7. ![Equation 7](https://latex.codecogs.com/svg.latex?f%5Chat(x)%20%3D%20%5Csum_%7Bj%3D1%7D%5EN%20N_j(x)%20%5Chat%7B%5Ctheta%7D_j)

8. ![Equation 8](https://latex.codecogs.com/svg.latex?%5Chat%7B%5Ctheta%7D%20%3D%20%5Cleft(N%5ET%20N%20%2B%20%5Clambda%20%5COmega_N%5Cright)%5E%7B-1%7D%20N%5ET%20y)

