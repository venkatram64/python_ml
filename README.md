step 1: create virtual environment
coda create -n chatbot python=3.5 anacoda
step 2: activate virtual environment
activate My_chatbot

step 3: install tensorflow
pip install tensorflow==1.0.0

pip install numpy
pip install pandas
pip install seaborn
pip install missingno

pip install datalab

pip install --upgrade pip

step 4: anaconda-navigator

step 5: from anaconda navigator dropdown, select chatbot

python -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl


********************************

Logistic Regression:

1. Softmax as activation function.
2. Cross entropy as cost funtion.

p = e^(a+bX)/(1+e^(a+bX)

where e = 2.7182
a = Intercept
b = Regression Coefficent

Given value of 'x' we predict probability of 'y' given by p(y) and 'y'
must be categorical.
To solve a logistic function, we could use a log function on the
equation this would make the relationship linear.
The odds of '(y) is given by:

odds(p) = p/(1-p)
where p = e^(a+bX)/(1+e^(a+bX)

ln(odds(p)) is called the logit function.
logit(p) = ax + b