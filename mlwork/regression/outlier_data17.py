import numpy as np
import matplotlib.pyplot as plt

def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    """Here's something a little more robust than filtering out billionaires 
    - it filters out anything beyond two standard deviations of 
    the median value in the data set:"""
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

def random_data_process():
    incomes = np.random.normal(27000, 15000, 10000) #mean, std, sample
    incomes = np.append(incomes, [1000000000])  #wrong data is added so this is the outlier
    plt.hist(incomes, 50)
    plt.show()

    print(incomes.mean())

    filtered = reject_outliers(incomes)
    plt.hist(filtered, 50)
    plt.show()

    print(np.mean(filtered))

if __name__ == '__main__':
    random_data_process()