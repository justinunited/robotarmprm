from math import atan2, cos,sin,sqrt,pi
def inverseKinematics(x,y,z,facing_angle):
    l1 = 340
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 83
    x5 = x - l6 * cos(facing_angle)
    y5 = y - l6 * sin(facing_angle)
    r = sqrt(x5**2 + y5**2)
    q1 = atan2(y5, x5)
    q5 = facing_angle - q1
    A = z - l1
    B = r - l2 - l5
    cos_q3m3pi = (A ** 2 + B ** 2 - l3 ** 2 - l4 ** 2) / (2 * l3 * l4)
    print(cos_q3m3pi)
    sin_q3m3pi = sqrt(1 - cos_q3m3pi ** 2)
    print(sin_q3m3pi)
    print(atan2(sin_q3m3pi, cos_q3m3pi))
    q3 = atan2(sin_q3m3pi, cos_q3m3pi) + 3 * pi / 4
    print(q3)
    sin_q2 = -(A * l3 ** 2 + B * l3 ** 2 + 2 * A * l4 ** 2 * cos(q3) ** 2 - 2 * B * l4 ** 2 * cos(q3) * sin(q3) - 2 * 2 ** (
                1 / 2) * A * l3 * l4 * cos(q3) - 2 ** (1 / 2) * B * l3 * l4 * cos(q3) + 2 ** (1 / 2) * B * l3 * l4 * sin(
                q3)) / ((2 ** (1 / 2) * l3 - 2 * l4 * cos(q3)) * (
                l3 ** 2 + l4 ** 2 - 2 ** (1 / 2) * l3 * l4 * cos(q3) + 2 ** (1 / 2) * l3 * l4 * sin(q3)))
    cos_q2 = (2 ** (1 / 2) * A * l3 - 2 ** (1 / 2) * B * l3 + 2 * B * l4 * cos(q3) + 2 * A * l4 * sin(q3)) / (
                2 * (l3 ** 2 + l4 ** 2 - 2 ** (1 / 2) * l3 * l4 * cos(q3) + 2 ** (1 / 2) * l3 * l4 * sin(q3)))
    q2 = atan2(sin_q2, cos_q2)
    print('q2',q2)
    if q2 < atan2(z,r):
        q2+=135*pi/180
        q3 = q3 - 270 * pi / 180
    q4 = - q2 - q3
    return(q1,q2,q3,q4,q5)
