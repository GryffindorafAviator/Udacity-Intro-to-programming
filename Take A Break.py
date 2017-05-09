import time
import webbrowser

countBreak = 0
totalBreaks = 3

while countBreak < totalBreaks:
    time.sleep(10)
    webbrowser.open("https://classroom.udacity.com/nanodegrees/nd000-cn-basic/parts/d68d0f74-cd2d-4a7d-b06e-3e0396bccc31/modules/c443093a-31ee-4a80-afb1-3c174b482b9e/lessons/7f8296ed-a0c1-4d72-b690-ccf3ebb0e9a8/concepts/9977893140923")
    countBreak += 1
