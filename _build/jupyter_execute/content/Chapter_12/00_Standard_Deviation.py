# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
%matplotlib inline
import math
from scipy import stats
from scipy import misc

# Standard Deviation #

The expected value $\mu_X$ of a random variable $X$ is a measure of the center of the distribution of $X$. But we know that $X$ need not be equal to $\mu_X$; indeed, $\mu_X$ need not even be a possible value of $X$.

How far from $\mu_X$ can $X$ be? This chapter develops an answer to that question.

As a starting point, it is natural to look at the *deviation from the mean*

$$
X - \mu_X
$$

and try to get a sense of what we expect that to be. By the linear function rule,

$$
E(X - \mu_X) = E(X) - \mu_X = \mu_X - \mu_X = 0
$$

For every random variable, the expected deviation from the mean is 0. The positive deviations exactly cancel out the negative ones.

This cancellation prevents us from understanding how big the deviations are regardless of their sign. But that's what we need to measure, if we want to measure the distance between the random variable $X$ and its expectation $\mu_X$.

We have to get rid of the sign of the deviation somehow. One time-honored way of getting rid of the sign of a number is to take the absolute value. The other is to square the number. That's the method we will use. As you will see, it results in a measure of spread that is crucial for understanding the sums and averages of large samples.




```{toctree}
:hidden:
:titlesonly:


01_Definition
02_Prediction_and_Estimation
03_Bounds
04_Heavy_Tails
```
