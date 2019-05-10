# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:03:08 2019

@author: Chinedu Anigbogu
"""

from mnist_loader import load_mnist
from cifar_10 import load_cifar_10_py

#cifar_dir='your local cifar-10 directory'
#mnist_dir='your local mnist directory'

cifar_dir=r'C:\Users\Chinedu\Desktop\mnist\cifar-10-batches-py'
mnist_dir=r'C:\Users\Chinedu\Desktop\mnist'

# for mnist
train_images,train_labels,test_images,test_labels=load_mnist(mnist_dir)

# for ciar-10
train_data,train_labels,test_data,test_labels,train_filenames,\
test_filenames,label_names=load_cifar_10_py(cifar_dir)