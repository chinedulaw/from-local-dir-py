# cifar-10-py
A utility program based on python 3 that loads CIFAR-10 datasets  from local directory/file

The CIFAR-10 dataset
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images. 

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.
the dataset can be downloaded from this site https://www.cs.toronto.edu/~kriz/cifar.html. 

the program returns the following from the dataset.
train_data,train_labels,test_data,test_labels,train_filenames,test_filenames,label_names
