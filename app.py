from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2

class Root_Layout(GridLayout):
    def grading_pear(self):
        camera_view = self.ids.camera_view
        if camera_view.frame is not None:
            image_frame = camera_view.frame
            print("Frame captured for grading:", image_frame.shape)

        # self.ids.navigation.text = "Clicked !!"

class CameraView(Image):
    def __init__(self, **kwargs):
        super(CameraView, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30)
    
    def update(self, dt):
        ret, self.frame = self.capture.read()
        if ret:
            buf = cv2.flip(self.frame, 0).tobytes()
            texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt="bgr")
            texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
            self.texture = texture

    def on_stop(self):
        self.capture.release()

class Main_app(App):
    title = "GUI Application"

if __name__ == "__main__":
    Main_app().run()