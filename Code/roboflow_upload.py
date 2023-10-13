import roboflow
import os

IMAGE_PATH = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/reupload/test/images'
XML_PATH = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/reupload/test/labels'

images = os.listdir(IMAGE_PATH)
xmls = os.listdir(XML_PATH)

rf = roboflow.Roboflow(api_key='IcukSAxORpooF3IBUNsS')
PROJECT_NAME = "ARCCModels"  # Whatever your workspace name is
project = rf.project("uwyo-basketball-player-detection")
print(project)

sorted_images = sorted(images)
sorted_xmls = sorted(xmls)

for image, xml in zip(sorted_images, sorted_xmls):
    image_path = os.path.join(IMAGE_PATH, image)
    xml_path = os.path.join(XML_PATH, xml)
    project.upload(image_path=image_path, annotation_path=xml_path, split='train', overwrite=True)
    delete_image = os.path.join(IMAGE_PATH, image)
    delete_xml = os.path.join(XML_PATH, xml)
    os.remove(delete_image)
    os.remove(delete_xml)


