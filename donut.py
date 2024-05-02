from screeninfo import get_monitors
import math
theta_spacing = 0.07
phi_spacing = 0.02

r1 = 1
r2 = 2
k2 = 5

monitor_width = get_monitors()[0].width
monitor_height = get_monitors()[0].height


k1 = monitor_width*k2*3/(8*(r1+r2))

def render_frame(A,B):
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    return
