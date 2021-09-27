import cv2, queue, threading

# bufferless VideoCapture
class VideoCapture:
  width=0
  height=0
  fps=0
  def __init__(self, name):
    if name==0:
      self.isStream=False
    else:
      self.isStream = name.startswith('rtsp') or name.startswith('http') or name.endswith('.txt')
    self.cap = cv2.VideoCapture(name)
    self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
    if self.isStream:
      self.q = queue.Queue()
      t = threading.Thread(target=self._reader)
      t.daemon = True
      t.start()

  # read frames as soon as they are available, keeping only most recent one
  def _reader(self):
    while True:
      ret, frame = self.cap.read()
      
      if not self.q.empty():
        try:
          self.q.get_nowait()   # discard previous (unprocessed) frame
        except queue.Empty:
          pass
      self.q.put((ret,frame))
      if not ret:
        break
  def read(self):
    if self.isStream:
      return self.q.get()
    else:      
      return self.cap.read()