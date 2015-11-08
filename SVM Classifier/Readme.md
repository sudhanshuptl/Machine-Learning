# __Support Vector Machine__

Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

##The advantages of support vector machines are:

 * Effective in high dimensional spaces.
 * Still effective in cases where number of dimensions is greater than the number of samples.
 * Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
 * Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

##The disadvantages of support vector machines include:


 * If the number of features is much greater than the number of samples, the method is likely to give poor performances.
 * SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

 # The Digit Dataset
 This dataset is made up of 1797 8x8 images. Each image, like the one shown below, is of a hand-written digit. In order to utilize an 8x8 figure like this, we’d have to first transform it into a feature vector with length 64.
 
  * Total 64 feature extracted from 8x8 image.
  * Label vector have 9 classes . Each for Identify hand-written digit from [0,1,2,3,4,5,6,7,8,9].
  
### Notes
These arguments used to customise you kernels 
 * kernel : Used to convert low dimensional feature space to high dimensional space in order to make it separable.
 * C  :- Controls trade off between smooth decision boundary and classify training point correctly. High value leads to over-fitting that is not good for generalisation
 * gamma :- Defines how far influence of a single training example reach.(high value of gamma leads to over fitting) so for generalise classification we need low value of gamma .
 * cache_size
 * class_weight
 * coef0
 * decision_function_shape
 * max_iter
 * probability
 * random_state
 * shrinking
 * tol
 * verbose