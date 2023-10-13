import os
import cv2
import helper_functions
import supervision as sv
from typing import List
import roboflow
from groundingdino.util.inference import Model
import torch

# Path to directory where you want to store images
HOME = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff'
# DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
SOURCE_DIRECTORY_PATH = os.path.join(HOME, "data/basketball_clip")  # Add folder to hold images
CONFIG_PATH = os.path.join(HOME, "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py")
WEIGHTS_PATH = os.path.join(f"{HOME}/weights", "groundingdino_swint_ogc.pth")
model = Model(model_config_path=CONFIG_PATH, model_checkpoint_path=WEIGHTS_PATH)
# model = Model(model_checkpoint_path=WEIGHTS_PATH)
# Get all valid image files
images = helper_functions.list_image_files(SOURCE_DIRECTORY_PATH)

# Calculate split for images, validation calculated implicitly
train_images = int(0.7 * len(images))
test_images = int(0.15 * len(images))


CLASSES = ['player']  # Objects for GroudingDINO to detect in images
BOX_THRESHOLD = 0.35
TEXT_THRESHOLD = 0.25

print(SOURCE_DIRECTORY_PATH)

def enhance_class_name(class_names: List[str]) -> List[str]:
    return [
        f"all {class_name}s"  # Changes classes names passed to have all "object's"
        # i.e 'apple' -> 'all apples' to increase number of objects detected
        for class_name in class_names
    ]


rf = roboflow.Roboflow(api_key='Put key here')
PROJECT_NAME = "ARCCModels"  # Whatever your workspace name is
project = rf.project("basketball-clip")
print(project)
for i, image_name in enumerate(images):
    image_path = os.path.join(SOURCE_DIRECTORY_PATH, image_name)
    image = cv2.imread(image_path)
    height, width, depth = image.shape
    xml_name = helper_functions.image_name_to_xml_name(image_name=image_name)
    xml_path = os.path.join(SOURCE_DIRECTORY_PATH, xml_name)

    detections = model.predict_with_classes(
        image=image,
        classes=enhance_class_name(class_names=CLASSES),
        box_threshold=BOX_THRESHOLD,
        text_threshold=TEXT_THRESHOLD
    )

    detections = detections[detections.class_id != None]  # Get rid of all images with detections
    # Get rid of images where entire image is detected as object
    detections = detections[(detections.area / (height * width)) < 0.9]

    xml_string = sv.detections_to_voc_xml(
        detections=detections,
        classes=CLASSES,
        filename=image_name,
        width=width,
        height=height,
        depth=depth
    )

    helper_functions.save_voc_xml(xml_string=xml_string, file_path=xml_path)

    if i < test_images:
        split = "test"
    elif i < test_images + train_images:
        split = "train"
    else:
        split = "valid"

    project.upload(image_path=image_path, annotation_path=xml_path, split=split,
                   overwrite=True)
