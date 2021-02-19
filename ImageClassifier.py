import os, shutil

original_dataset_dir ='/Users/jacob/OneDrive/Desktop/GitHub/Deep-Learning-With-Python-Exercises/'

base_dir = '/Users/jacob/OneDrive/Desktop/GitHub/Deep-Learning-With-Python-Exercises/cats_and_dogs_small'


train_dir = os.path.join(base_dir, '/train')
# os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, '/validation')
# os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, '/test')
# os.mkdir(test_dir)

train_cats_dir = os.path.join(train_dir, '/cats')
# os.mkdir(train_cats_dir)

train_dogs_dir = os.path.join(train_dir, '/dogs')
# os.mkdir(train_dogs_dir)

validation_cats_dir = os.path.join(validation_dir, '/cats')
# os.mkdir(validation_cats_dir)

validation_dogs_dir = os.path.join(validation_dir, '/dogs')
# os.mkdir(validation_dogs_dir)

test_cats_dir = os.path.join(test_dir, '/cats')
# os.mkdir(test_cats_dir)

test_dogs_dir = os.path.join(test_dir, 'dogs')
# os.mkdir(test_dogs_dir)

fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src, dst)

print('Done')