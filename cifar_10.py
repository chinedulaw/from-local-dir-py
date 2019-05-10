# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:51:54 2019

@author: Chinedu Anigbogu
Project Description:
    A utility program that loads cifar-10-py data from local directory/file
"""
#DEPENDENCIES NEEDED
import pickle
import numpy as np

"""
please note the cifar_dir containes the decompressed 
cifar-10 files in batches,i.e. 
batches.meta,data_batch_1,data_batch_2,data_batch_3,
data_batch_4,data_batch_5 and test_batch"""

def unpickle(file):
    '''this fn unpickles a particular batch
    in the cifar data batches'''
    with open(file,'rb') as fileobject:
        data=pickle.load(fileobject,encoding='bytes')
        return data
    
def load_cifar_10_py(cifar_dir):
    
    print('Extracting cifar-10-py .............')
    batches_meta_dict=unpickle(cifar_dir+'\\batches.meta')
    label_names=[a.decode('utf-8') for a in batches_meta_dict[b'label_names']]
    
#    each batch contains:
#    b'labels' which is of type list
#    b'data' which is of type numpy.ndarray
#    b'filenames which is of type list
    
    for a in range(1,6):
         template=cifar_dir+'\\data_batch_{}'.format(a)
         train_data_dict=unpickle(template)
         if a==1:
            train_data=train_data_dict[b'data']
            train_labels=train_data_dict[b'labels']
            train_filenames=train_data_dict[b'filenames']
            
         else:
            train_data=np.vstack((train_data,train_data_dict[b'data']))
            train_labels += train_data_dict[b'labels']
            train_filenames +=train_data_dict[b'filenames']
            
    train_filenames=np.array([b.decode('utf-8') for b in train_filenames])
    train_labels=np.array(train_labels)       
    test_data_dict=unpickle(cifar_dir+'\\test_batch')
    test_data=test_data_dict[b'data']
    test_labels=np.array(test_data_dict[b'labels'])
    test_filenames=np.array([b.decode('utf-8') for b in test_data_dict[b'filenames']])
    print('Done!')
    
    return train_data,train_labels,test_data,test_labels,train_filenames,test_filenames,label_names

        
    
    
    
    
