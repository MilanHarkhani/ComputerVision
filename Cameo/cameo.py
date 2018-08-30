import cv2
from manager import CaptureManager,WindowManager
import filters
from pafy import pafy
class Cameo(object):
    def __init__(self,link=0,youtubelink=False):
        if(youtubelink and link!=0):
            pf = pafy.new(link)
            best = pf.getbest(preftype="mp4")
            link = best.url

        self._windowManager = WindowManager('Cameo',self.onKeyPress)
        self._captureManager = CaptureManager(cv2.VideoCapture(link),self._windowManager,False)
        self._filter = filters.BlurFilter()
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame=self._captureManager.frame
            self._captureManager.exitFrame()
            self._windowManager.processEvent()


    def onKeyPress(self,keycode):
        """Handle a keypress.
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.   """
        if keycode == 32:
            print('space pressed')
            self._captureManager.writeImage('screenshot.png')

        elif keycode == 9:
            if not self._captureManager.isWrittingVideo:
                self._captureManager.startWrittingVideo('screencat.avi')
            else:
                self._captureManager.stopWrittingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()

if __name__=="__main__":
    Cameo(link='https://www.youtube.com/watch?v=1MVQYSlgXrI',youtubelink=True).run()
