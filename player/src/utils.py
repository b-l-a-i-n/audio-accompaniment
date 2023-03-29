import os
import cv2
import requests
import uuid
import logging

def get_predictions(url, timestamp):
    image = get_image_from_timestamp(url, timestamp)
    response = post_request_to_server(image) 
    data = response.json()
    
    return data['predictions']

def post_request_to_server(image):
    url = 'http://91.185.84.110:81/predict'
    file = open(image, 'rb')
    files = {'file': file}
    predictions = requests.post(url, files=files)
    file.close()
    os.remove(image)
    return predictions

def get_image_from_timestamp(url:str, timestamp):
    '''
    :url: video link
    :timestamp: video timestamp in seconds
    :return: image path
    '''
    cap = cv2.VideoCapture(url)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        # print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = cap.get(cv2.CAP_PROP_FPS)
        # print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    
    
    time_in_frames = int(fps * timestamp)
    counter = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if counter == time_in_frames:
            cap.release()
            cv2.destroyAllWindows()
            uniqe_text = str(uuid.uuid4())
            name = f'tmp/{uniqe_text}.jpg'
            cv2.imwrite(name, frame)
            
            return name

        counter += 1

    cap.release()
    cv2.destroyAllWindows()
    return frame
    

if __name__ == "__main__":
    # Test
    url = 'https://www.sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'
    timestamp = 1
    get_predictions(url, timestamp)
    
