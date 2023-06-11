# Splines_approximator

Approximate the function  $f_{real}(x)= \frac{\sin(12(x+0.2))}{(x+0.2)}$ using natural cubic splines as described in Chapter 5.2.1 of [The Elements of Statistical Learning](https://link.springer.com/book/10.1007/978-0-387-84858-7).


![figure](https://github.com/antvas98/Splines_approximator/assets/115734703/bb5c8322-ba0c-4144-a47d-6ef6ca802fe2)

## Equations

1. \(f(x) = \sum_{j=1}^{N} N_j(x) \theta_j\)

2. \(N_1(X) = 1\), \(N_2(X) = X\), \(N_{k+2}(X) = d_k(X) - d_{K-1}(X)\)

3. \(d_k(X) = \frac{{(X - \xi_k)^3 - (X - \xi_K)^3}}{{\xi_K - \xi_k}}\)

4. \(RSS(f, \lambda) = \sum_{i=1}^{N} (y_i - f(x_i))^2 + \lambda \int (f''(t))^2 dt\)

5. \(RSS(\theta, \lambda) = (y - N\theta)^T (y - N\theta) + \lambda \theta^T \Omega_N \theta\)

6. \(RSS(\theta, \lambda) = (y - N\theta)^T (y - N\theta) + \lambda \theta^T \Omega_N \theta\)

7. \(f\hat(x) = \sum_{j=1}^{N} N_j(x) \hat{\theta}_j\)

8. \(\hat{\theta} = (N^T N + \lambda \Omega_N)^{-1} N^T y\)
