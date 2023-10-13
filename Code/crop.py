from ultralytics import YOLO

DATA = '/project/arcc-students/dwalton5/miniconda/assignment4/basketball/Downloads/test/images'
model = YOLO('/project/arcc-students/dwalton5/miniconda/assignment4/basketball/Videos/runs/detect/train5/weights/best.pt')
model.predict(source=DATA, save=True, imgsz=320, conf=0.2, show=True, save_crop=True)