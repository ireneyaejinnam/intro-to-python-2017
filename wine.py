"""
HW 5
Irene Nam
UNI: yn2334
Sorry for the 4 seconds runtime!
"""

import numpy as np
from matplotlib import pyplot as plt

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))


def load_data(csv_filename):

    data = np.genfromtxt(csv_filename, delimiter=';', skip_header=1)
    return data[:,0:11]


def split_data(dataset, ratio = 0.9):
    
    n = int(ratio * len(dataset))
    train = dataset[:n]
    test = dataset[n:]
    return (train,test)
    

def compute_centroid(data):
    
    return sum(data[:,:]) / len(data)


def experiment(ww_train, rw_train, ww_test, rw_test):

    ww_centroid = compute_centroid(ww_train)
    rw_centroid = compute_centroid(rw_train)
    
    correct = 0
    total = 0
    
    for x in ww_test:
        total += 1
        if euclidean_distance(ww_centroid, x) < euclidean_distance(rw_centroid, x):
            correct += 1
        else:
            correct = correct
        
    for y in rw_test:
        total += 1
        if euclidean_distance(rw_centroid, y) < euclidean_distance(ww_centroid, y):
            correct += 1
        else:
            correct = correct

    accuracy = correct/total
    
    return accuracy

    
def learning_curve(ww_training, rw_training, ww_test, rw_test):
    
    np.random.shuffle(ww_training)
    np.random.shuffle(rw_training)
    accuracy_list = []
    n_list = []
 
    for n in range(len(ww_training)):
        accuracy_list.append(experiment(ww_training[0:n+1], rw_training[0:n+1], ww_test, rw_test))
        n_list.append(int(n))
        
        
    plt.xlabel("number of training items")
    plt.ylabel("accuracy")
    plt.plot(n_list,accuracy_list)
        

    
def cross_validation(ww_data, rw_data, k):
    
    accuracy_list = []

    subset_size = int(len(ww_data)/k)
    
    for i in range(k):
        ww_testing = ww_data[i*subset_size:][:subset_size]
        ww_training = np.vstack((ww_data[:i*subset_size], ww_data[(i+1)*subset_size:]))
        rw_testing = rw_data[i*subset_size:][:subset_size]
        rw_training = np.vstack((rw_data[:i*subset_size], rw_data[(i+1)*subset_size:]))
        
        accuracy_list.append(experiment(ww_training, rw_training, ww_testing, rw_testing))
        
    sum_accuracy = sum(accuracy_list)
    
    accuracy = sum_accuracy/k
    
    return accuracy
    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')

    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    experiment(ww_train, rw_train, ww_test, rw_test)

    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    learning_curve(ww_train, rw_train, ww_test, rw_test)

    k = 10
    acc = cross_validation(ww_data, rw_data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))

    