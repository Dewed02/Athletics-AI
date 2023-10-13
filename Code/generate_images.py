import supervision as sv

VIDEO_PATH = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff'
IMAGE_PATH = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/basketball_clip'
FRAME_STRIDE = 5 # Number frames passed between image generation
video_paths = sv.list_files_with_extensions(
    directory=VIDEO_PATH,
    extensions=['mov', 'mp4'])

with sv.ImageSink(target_dir_path=IMAGE_PATH, image_name_pattern= 'frame{}.jpg') as sink:
    for image in sv.get_video_frames_generator(source_path='/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/basketball_clip.mp4', stride=FRAME_STRIDE):
        print('hi')
        sink.save_image(image=image)