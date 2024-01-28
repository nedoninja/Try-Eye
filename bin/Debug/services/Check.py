import speech_recognition
import cv2
import os
import urllib.request


class Check:
    
    def check_microphone(self):
        micro_list = speech_recognition.Microphone.list_microphone_names()
        if "Input" in micro_list[0]:
            return True
        elif "Output" in micro_list[0]:
            return False
        
    def check_camera(self):
        is_working = True
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            is_working = False

        return is_working
    
    def check_internet(self):
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False

print("загрузка приложения")

CheckHardware = Check()

microphone = CheckHardware.check_microphone()
camera = CheckHardware.check_camera()
internet = CheckHardware.check_internet()

print(microphone, camera, internet)