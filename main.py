import numpy as np
import scipy.stats 

def testStatistic( data, mu0 ) :
  # This fucntion should calcualte and return the test statistic T that is 
  # described in the panel on the right.  In order to do so you will need to
  # compute the standard deviation.
  

def pvalue( data, mu0 ) : 
  # You need to write code to determine the pvalue here.  This code will need to
  # include a call to test statistic
  
  
data = np.loadtxt("mydata.dat")
print("Null hypothesis: the data points in mydata.dat are all samples from a")
print("distribution with an expectation of 4")
print("Alternative hypothesis: the data points in mydata.dat are not all samples")
print("from a distribution with an expectation of 4")
print("The p-value for this hypothsis test is", pvalue( data, 4 ) )
