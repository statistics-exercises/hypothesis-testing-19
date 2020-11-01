# Hypothesis tests with unknown variance

Well done on remembering how to compute the variance.  Now that you have demonstrated that you know how to do this we are ready to consider how we determine whether or not I am lying when I tell you that:

_The input file `mydata.dat` contains a set of samples of from a distribution with expectation 4._

Notice that I have not provided a value for the standard deviation of the distribution that I am alleging that I  sampled the data from.  You thus need to calculate the sample variance from the data in order to compute the test __statistic__:

![](https://render.githubusercontent.com/render/math?math=T=\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^{n}(X_i-\mu_0))

__You now need to write code to perform the hypothesis test on the data in `mydata.dat` described above.__  I have written some functions that you should complete in order to get you started.  These functions are:

1. `testStatistic` - this function takes two arguments in input an NumPy array called `data` that contains the samples and a scalar called `mu0` which is the expectation of the distribution that is assumed under the null hypothesis.  This function should return the test statistic, T, that is defined using the formula above.  You will need to compute the sample variance within this function.
2. `pvalue` - this function takes two arguments in input an NumPy array called `data` that contains the samples and a scalar called `mu0` which is the expectation of the distribution that is assumed under the null hypothesis.  To complete this function you need to call `testStatistic` and you then need to calculate and return the __p-value__ based on the value of the __statistic__ that is returned by this function.

_We can just calculate the sample variance here because we have a large number of samples.  If the number of samples is small we need to do a different type of test.  We will cover this in more detail next week, however._ 
