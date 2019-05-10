# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:48:58 2019

@author: Chinedu Anigbogu
"""
import idx2numpy

''' The mnist dataset contains the followig data batches
train-labels.idx1-ubyte
train-images.idx3-ubyte
t10k-images.idx3-ubyte
t10k-labels.idx1-ubyte '''

def convert(file):
    with open(file,'rb') as filehandle:
        data_ndarr=idx2numpy.convert_from_file(filehandle)
    return data_ndarr
    
def load_mnist(data_dir):
    filenames=['train-labels-idx1-ubyte','train-images-idx3-ubyte',\
               't10k-images-idx3-ubyte','t10k-labels-idx1-ubyte' ]
    
    filenames2=['train-labels.idx1-ubyte','train-images.idx3-ubyte',\
               't10k-images.idx3-ubyte','t10k-labels.idx1-ubyte' ]
    try:
        train_images=convert(data_dir+'\{}'.format(filenames[1]))
        train_labels=convert(data_dir+'\{}'.format(filenames[0]))
        test_images=convert(data_dir+'\{}'.format(filenames[2]))
        test_labels=convert(data_dir+'\{}'.format(filenames[3]))
        
    except:
        train_images=convert(data_dir+'\{}'.format(filenames2[1]))
        train_labels=convert(data_dir+'\{}'.format(filenames2[0]))
        test_images=convert(data_dir+'\{}'.format(filenames2[2]))
        test_labels=convert(data_dir+'\{}'.format(filenames2[3]))
        
    return train_images,train_labels,test_images,test_labels
    
        
