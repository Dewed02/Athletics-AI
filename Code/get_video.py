from pytube import YouTube

SAVE_PATH = '/project/arcc-students/dwalton5/miniconda/Atheltics_Stuff/videos'


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download successful")


link = input("Provide YouTube URL: ")
download(link)
