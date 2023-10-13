from ultralytics import YOLO
import supervision as sv
def main():
    model = YOLO('/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/basketball_clip/data2/runs/detect/train/weights/best.pt')
    # box_annotator = sv.BoxAnnotator(
    #     thickness=2,
    #     text_thickness=1,
    #     text_scale=0.5
    # )
    for result in model.track(source='/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/basketball_clip.mp4', show=True, stream=True, save=True):
        frame = result.orig_img
        detections = sv.Detections.from_yolov8(result)
        if result.boxes.id is not None:
            detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
        # labels = [
        #     f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
        #     for _, confidence, class_id, tracker_id
        #     in detections
        # ]
        # frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
if __name__ == "__main__":
    main()

#https://www.youtube.com/watch?v=rNRsz7mWWsc