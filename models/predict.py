import cv2
import numpy as np

from models.model import load_model
from test import traffic_sign

class processing_data():
    def __init__(self, image):
        self.image = image

  # đưa kích thước image về 64 * 64 * 3
    def resize_image(self, size = (64, 64)):
        self.image = cv2.resize(src = self.image, dsize = size)

    # cân bằng ánh sáng
    def extract_color_histogram(self): 
        img_yuv = cv2.cvtColor(self.image, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

        # convert the YUV image back to RGB format
        img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        self.image = img_output

    # trả về ảnh kích thước 48*48*3 sau khi cân bằng sáng
    def convert_image(self):
        self.resize_image()
        self.extract_color_histogram()
        self.image = np.array(self.image)
        return self.image

model = load_model()

labels = ['00029', '00035', '00006', '00034', '00003', '00038', '00007', '00009', '00036', '00001', '00011', '00032', '00033', '00005']
dic = traffic_sign()

def predict(image_link):
    image = cv2.imread(image_link)
    new_img = processing_data(image).convert_image()
    new_img = new_img / 255.0
    tmp = np.array([new_img])
    tmp = model.predict(tmp)
    return {"answer": dic[labels[np.argmax(tmp, axis=1)[0]]]}



