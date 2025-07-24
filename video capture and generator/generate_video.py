from PIL import Image
import os
import cv2
base_dir = os.getcwd()
# RESIZING ALL THE IMAGE
path=os.path.join('static','uploads')
os.chdir(path)
no_of_image=len([file for file in os.listdir('.')])
mean_width=0
mean_height=0

#fetching wioth and height
for file in os.listdir('.'):
    if file.endswith(".jpg"):
        im=Image.open(file)
        h,w=im.size
        mean_height+=h
        mean_width+=w
        


mean_width=int(mean_width/no_of_image)
mean_height=int(mean_height/no_of_image)

# resizing
for file in os.listdir('.'):
    if file.endswith(".jpg"):
        im=Image.open(file)
        im_resize=im.resize((mean_width,mean_height),)
        im_resize.save(file,"JPEG")
 


# GENERATING VIDEO
def generate():
    image_folder=path
    video_name="MyGenratedVideo.mp4"
    images=[img for img in os.listdir('.')]

    #SETING 1ST Frame
    frame=cv2.imread(images[0])
    h,w,c=frame.shape

    #VIDEO WRITER
    video=cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*"mp4v"),fps=1,frameSize=(w,h))

    for image in images:
        video.write(cv2.imread(image))

    video.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"Video Generated successfully")

def view_video():
    path=r'static\uploads\MyGenratedVideo.mp4'
    cap=cv2.VideoCapture(path)
    if cap.isOpened()==False:
        print("Unable to identify video")
        return
    while (cap.isOpened()):
        ret,frame=cap.read()
        if ret==True:
            cv2.imshow('Generated Video',frame)

            if cv2.waitKey(251) & 0XFF==ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

generate()
os.chdir(base_dir)
view_video()