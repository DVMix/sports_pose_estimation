class DroneHeight:

    def __init__(self, drone):
        self.drone = drone
        self.current_height = None

    def get(self):
        # @TODO check for drone "takeoff"
        if self.drone.is_flying:
            # @TODO get current height of drone
            self.current_height = None

    def set(self, x):
        self.current_height = x
        # @TODO send command to drone with target height


class Obj2DroneDistance:

    def __init__(self, drone):
        self.drone = drone
        self.current_distance = None

    def get(self):
        # @TODO check for drone "takeoff"
        if self.drone.is_flying:
            # @TODO calculate current distance and orientation of drone
            self.current_distance = None

    def set(self, x):
        self.current_distance = x
        # @TODO send command to drone with target distance and orientation


class DroneOrientation(DroneHeight, Obj2DroneDistance):

    def __init__(self, drone):
        super(DroneOrientation, self).__init__(drone=drone)
        a = 1
        pass

    def fn(self):
        pass


def main():
    from djitellopy import Tello
    tello = Tello()
    tello.connect()
    a = DroneOrientation(drone=tello)
    print(1)


if __name__ == '__main__':
    main()
