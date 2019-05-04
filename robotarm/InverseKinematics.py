from math import atan2, cos,sin,sqrt,pi
from ForwardKinematics import Px, Py, Pz
def inverseKinematics(x,y,z,facing_angle):
    l1 = 373
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
    off = 120*pi/180
    cos_q3moff = (A ** 2 + B ** 2 - l3 ** 2 - l4 ** 2) / (2 * l3 * l4)
    sin_q3moff = sqrt(1 - cos_q3moff ** 2)
    q3 = atan2(-sin_q3moff, cos_q3moff) + off
    # print(atan2(-sin_q3moff, cos_q3moff),atan2(sin_q3moff, cos_q3moff))
    sin_q2 = (A*l3*cos(off) + A*l4*cos(q3) - B*l3*sin(off) - B*l4*sin(q3))/(l3**2 + 2*cos(off - q3)*l3*l4 + l4**2)
    cos_q2 = (B*l3*cos(off) + B*l4*cos(q3) + A*l3*sin(off) + A*l4*sin(q3))/(l3**2 + 2*cos(off - q3)*l3*l4 + l4**2)
    q2 = atan2(sin_q2, cos_q2)
    # print(q2+2*pi/3,atan2(z,r))
    if q2+2*pi/3 < atan2(z,r):
        q3 = atan2(sin_q3moff, cos_q3moff) + off
        sin_q2 = (A * l3 * cos(off) + A * l4 * cos(q3) - B * l3 * sin(off) - B * l4 * sin(q3)) / (
                    l3 ** 2 + 2 * cos(off - q3) * l3 * l4 + l4 ** 2)
        cos_q2 = (B * l3 * cos(off) + B * l4 * cos(q3) + A * l3 * sin(off) + A * l4 * sin(q3)) / (
                    l3 ** 2 + 2 * cos(off - q3) * l3 * l4 + l4 ** 2)
        q2 = atan2(sin_q2, cos_q2)
    q4 = - q2 - q3
    # q1 = q1*180/pi
    # q2 = q2 * 180 / pi
    # q3 = q3 * 180 / pi
    # q4 = q4 * 180 / pi
    # q5 = q5 * 180 / pi
    return(q1,q2,q3,q4,q5)


#
# q1,q2,q3,q4,q5 = inverseKinematics(651.74,371.22,776.66,0)
# # x = Px(0,0,0,0,0)
# # y = Py(0,0,0,0,0)
# # z = Pz(0,0,0,0,0)
# # q1,q2,q3,q4,q5 = inverseKinematics(x,y,z,0)
# print(q1,q2,q3,q4,q5)
# print(Px(q1,q2,q3,q4,q5),Py(q1,q2,q3,q4,q5),Pz(q1,q2,q3,q4,q5))

