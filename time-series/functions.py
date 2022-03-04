import numpy as np

def mae(y, y_hat):
    return np.mean(np.abs(y - y_hat))

def mse(y, y_hat):
    return np.mean(np.square(y - y_hat))

def rmse(y, y_hat):
    return np.sqrt(np.mean(np.square(y - y_hat)))

def mape(y, y_hat):
    return np.mean(np.abs((y - y_hat)/y)*100)

# SMAPE proposed by Makridakis (1993): 0%-200%
def smape_original(y, y_hat):
    return 1/len(y) * np.sum(2 * np.abs(y_hat-y) / (np.abs(y) + np.abs(y_hat))*100)


# adjusted SMAPE version to scale metric from 0%-100%
def smape_adjusted(y, y_hat):
    return (1/y.size * np.sum(np.abs(y_hat-y) / (np.abs(y) + np.abs(y_hat))*100))

def mdrae(y, y_hat, bnchmrk):
    return np.median(np.abs(y - y_hat)/np.abs(y - bnchmrk))

def gmrae(y, y_hat, bnchmrk):
    
    abs_scaled_errors = np.abs(y - y_hat)/np.abs(y - bnchmrk)
    return np.exp(np.mean(np.log(abs_scaled_errors)))

def mase(y, y_hat, y_train):
    ## MAE
    mae = np.mean(np.abs(y - y_hat))
    
    ## Naive in-sample Forecast
    naive_y_hat = y_train[:-1] #all values except the last one
    naive_y = y_train[1:] #all values except the frist one

    ## Calculate MAE (in sample)
    mae_in_sample = np.mean(np.abs(naive_y - naive_y_hat))
    
    return mae/mae_in_sample

def seasonal_mase(y, y_hat, y_train, m):
    ## MAE
    mae = np.mean(np.abs(y - y_hat))
    
    ## Naive in-sample Forecast
    naive_y_hat = y_train[:-m] #all values except the last one
    naive_y = y_train[m:] #all values except the frist one

    ## Calculate MAE (in sample)
    mae_in_sample = np.mean(np.abs(naive_y - naive_y_hat))
    
    return mae/mae_in_sample

'''
#From scratch implementation
def euclidean_distance(y, y_hat):
    return np.sqrt(np.sum(np.power(y-y_hat, 2)))
'''

def euclidean_distance(y, y_hat):
    return np.linalg.norm(y - y_hat)

def pearson_corr(y, y_hat):
    num = np.sum(np.multiply(y-np.mean(y), y_hat-np.mean(y_hat)))
    denom = np.sqrt(np.sum(np.square(y-np.mean(y)))) * np.sqrt(np.sum(np.square(y_hat-np.mean(y_hat))))
    if np.isclose(denom, 0, atol = 10e-3): 
        print("Close to 0 denominator. Invalid correlation.")
        return "Indetermined correlation"
    else:
        return num / denom
