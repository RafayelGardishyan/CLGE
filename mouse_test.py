from clge import MouseDetector

m = MouseDetector("left")
mr = MouseDetector("right")
mm = MouseDetector("middle")

while True:
    if m.detect():
        print("Left is pressed")
    elif mr.detect():
        print("Right is pressed")
    elif mm.detect():
        print("Middle is pressed")