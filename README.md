# BROIL_ALP

This project has 3 main goals:

* Combine Robust Inverse Reinforcement Learning (RIRL) with Approximate Linear Programming (ALP)
* Extend this concept to combine ALP and Bayesian Robust Optimization for Imitation Learning (BROIL)
* Use these methods to solve COVID-19 lockdown strategy as a control problem

We can title the overarching strategy Robust Value Approximation (RoVA).
We first use Approximate Robust Linear Programming for Imitation Learnin wherein we combine RIRL and ALP, which can be solved as a linear program
We then further discuss and show how this concept could be applied to extend BROIL, which uses Conditional Value at Risk (CVaR) instead of a minmax problem

Finally we justify COVID-19 lowdown strategy as an ideal candidate for these methods, as there are many possible reward functions that a government may try to optimize when constructing a lockdown policy. In this case on may want to find a lockdown policy that is robust to the worst case scenarios for each of these possible reward functions.

All code and formalized paper can be found on [GitHub](https://github.com/brendanjcrowe/BROIL_ALP)

