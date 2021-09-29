import cameratransform as ct
class PositionConverter:
    def __init__(self,imageX,ImageY ):
        # intrinsic camera parameters
        f = 2.8    # in mm
        sensor_size = (6.17, 4.55)    # in mm
        imageSize = (imageX, ImageY)    # in px
        # initialize the camera
        self.cam = ct.Camera(ct.RectilinearProjection(focallength_mm=f,sensor=sensor_size,image=imageSize),ct.SpatialOrientation())
        self.cam.elevation_m = 5
        self.cam.tilt_deg = 45
        self.cam.roll_deg = 0

    def GetPostion(self,x,y):
        return self.cam.spaceFromImage([x, y])

 