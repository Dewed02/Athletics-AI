import os
import shutil

IMAGES = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/train/images'
LABELS = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/train/labels'
VALID = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/Train/images'
TEST = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/test/images'
TRAIN = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/valid/images'
valid_labels_folder = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/valid/labels'
test_labels_folder = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/test/labels'
train_labels_folder = '/project/arcc-students/dwalton5/miniconda/assignment4/football_dataset/Train/labels'

# os.mkdir(VALID)
# os.mkdir(TRAIN)
# os.mkdir(TEST)
# os.mkdir(valid_labels_folder)
# os.mkdir(test_labels_folder)
# os.mkdir(train_labels_folder)


# Get all file names
image_filenames = os.listdir(IMAGES)
label_filenames = os.listdir(LABELS)

# Calculate the split
total_images = len(image_filenames)
total_labels = len(label_filenames)
train_ratio = 0.7
valid_ratio = 0.15
train_count = int(total_images * train_ratio)
train_labels = int(total_labels * train_ratio)
valid_count = int(total_images * valid_ratio)
valid_labels = int(total_labels * valid_ratio)


# Split images into train, test, and valid sets
train_images = image_filenames[:train_count]
valid_images = image_filenames[train_count:train_count+valid_count]
test_images = image_filenames[train_count+valid_count:]

# Split Labels into train, test, and valid sets
train_label = label_filenames[:train_labels]
valid_label = label_filenames[train_labels:train_labels+valid_labels]
test_label = label_filenames[train_labels+valid_labels:]
print(total_images)
print(total_labels)
# Move files to their new folders
# for filename in train_images:
#     src = os.path.join(IMAGES, filename)
#     dst = os.path.join(TRAIN, filename)
#     shutil.copy(src, dst)
#     print('Train')
#
# for filename in valid_images:
#     src = os.path.join(IMAGES, filename)
#     dst = os.path.join(VALID, filename)
#     shutil.copy(src, dst)
#     print('Valid')
#
# for filename in test_images:
#     src = os.path.join(IMAGES, filename)
#     dst = os.path.join(TEST, filename)
#     shutil.copy(src, dst)
#     print('Test')
#
# # Move labels to folders
# for filename in train_label:
#     src = os.path.join(LABELS, filename)
#     dst = os.path.join(train_labels_folder, filename)
#     shutil.copy(src, dst)
#     print('Train label')
#
# for filename in valid_label:
#     src = os.path.join(LABELS, filename)
#     dst = os.path.join(valid_labels_folder, filename)
#     shutil.copy(src, dst)
#     print('Valid label')
#
# for filename in test_label:
#     src = os.path.join(LABELS, filename)
#     dst = os.path.join(test_labels_folder, filename)
#     shutil.copy(src, dst)
#     print('Test label')
#

