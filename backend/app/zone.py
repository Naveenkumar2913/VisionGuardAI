import cv2
import numpy as np

ZONE = np.array([[200,100],[500,100],[500,400],[200,400]], dtype=np.int32)

def draw_zone(frame):
    cv2.polylines(frame,[ZONE],True,(0,0,255),2)

def inside_zone(point):
    return cv2.pointPolygonTest(ZONE,point,False) >= 0