step 1: create virtual environment
conda create -n My_chatbot python=3.5 anacoda
step 2: activate virtual environment
activate My_chatbot

deactivate 

step 3: install tensorflow
pip install tensorflow==1.10.0

pip install numpy
pip install pandas
pip install seaborn
pip install missingno

pip install datalab
pip install quandl
pip install pandas_datareader
pip install xlrd
pip install statsmodels
pip install patsy
pip install grphviz
pip install pydot
pip install pydotplus
pip install keras

for spark add the following into classpath
\python\lib\py4j-0.9-src.zip
\bin\python\lib\pyspark.zip

to install https://graphviz.gitlab.io/_pages/Download/Download_windows.html
set the path C:\Program Files (x86)\Graphviz2.38\bin

pip install --upgrade pip

step 4: anaconda-navigator

step 5: from anaconda navigator dropdown, select chatbot

python -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl


for windows:

conda create --name tensorflow python=3.5
activate tensorflow
pip install tensorflow-gpu

pip install mpl_finance    (for candle stick)
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


https://iextrading.com/developer/docs/#chart   (finanace data)

https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/
https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/