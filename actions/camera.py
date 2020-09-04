import cv2

def get_qr_value():
    camera = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    try:
        _, img = camera.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if(bbox is not None):
            return data
    except:
        return None
    finally:
        print("Exit..")
        camera.release()
        cv2.destroyAllWindows()
