from math import *

def Len (v):
    return sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def Norm (v):
    if (v[0] == v[1] == v[2] == 0):
        return v
    else:
        l = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        x = v[0]/l
        y = v[1]/l
        z = v[2]/l
        norm = (x, y, z)
        return norm

def VxR (v, const):
    x = v[0]*const
    y = v[1]*const
    z = v[2]*const
    newV = (x, y, z)
    return newV

def VplusV (v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    z = v1[2] + v2[2]
    newV = (x, y, z)
    return newV

def VminusV (v1, v2):
    x = v1[0] - v2[0]
    y = v1[1] - v2[1]
    z = v1[2] - v2[2]
    newV = (x, y, z)
    return newV

def VdotV (v1, v2):
    res = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    return res

def numAfterPoint(num):
    return float("{0:.2f}".format(num))

def VxV (v1, v2):
    x = numAfterPoint(v1[1]*v2[2] - v1[2]*v2[1])
    y = numAfterPoint(v1[2]*v2[0] - v1[0]*v2[2])
    z = numAfterPoint(v1[0]*v2[1] - v1[1]*v2[0])
    newV = (x, y, z)
    return newV

def mI ():
    return ((1.00, 0.00, 0.00),
             (0.00, 1.00, 0.00),
             (0.00, 0.00, 1.00))

def MxR (matr, num):
    return ((matr[0][0]*num, matr[0][1]*num, matr[0][2]*num),
             (matr[1][0]*num, matr[1][1]*num, matr[1][2]*num),
             (matr[2][0]*num, matr[2][1]*num, matr[2][2]*num))

def MplusM (m1, m2):
    return ((m1[0][0] + m2[0][0], m1[0][1] + m2[0][1], m1[0][2] + m2[0][2]),
            (m1[1][0] + m2[1][0], m1[1][1] + m2[1][1], m1[1][2] + m2[1][2]),
            (m1[2][0] + m2[2][0], m1[2][1] + m2[2][1], m1[2][2] + m2[2][2]))

def MminusM (m1, m2):
    return ((m1[0][0] - m2[0][0], m1[0][1] - m2[0][1], m1[0][2] - m2[0][2]),
            (m1[1][0] - m2[1][0], m1[1][1] - m2[1][1], m1[1][2] - m2[1][2]),
            (m1[2][0] - m2[2][0], m1[2][1] - m2[2][1], m1[2][2] - m2[2][2]))

def MxV (m, v):
    return (m[0][0]*v[0] + m[0][1]*v[1] + m[0][2]*v[2],
            m[1][0]*v[0] + m[1][1]*v[1] + m[1][2]*v[2],
            m[2][0]*v[0] + m[2][1]*v[1] + m[2][2]*v[2])

def MxM (m1, m2):
    return((m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0] + m1[0][2]*m2[2][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1] + m1[0][2]*m2[2][1], m1[0][0]*m2[0][2] + m1[0][1]*m2[1][2] + m1[0][2]*m2[2][2]),
           (m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0] + m1[1][2]*m2[2][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1] + m1[1][2]*m2[2][1], m1[1][0]*m2[0][2] + m1[1][1]*m2[1][2] + m1[1][2]*m2[2][2]),
           (m1[2][0]*m2[0][0] + m1[2][1]*m2[1][0] + m1[2][2]*m2[2][0], m1[2][0]*m2[0][1] + m1[2][1]*m2[1][1] + m1[2][2]*m2[2][1], m1[2][0]*m2[0][2] + m1[2][1]*m2[1][2] + m1[2][2]*m2[2][2]))

def MRot (v, rad):
    m = ((0, v[2], -v[1]),
         (-v[2], 0, v[0]),
         (v[1], -v[0], 0))
    matrPov = MplusM(mI(), MxR(m, sin(rad)))
    m1 = MxR(MxM(m, m), 1 - cos(rad))
    return MplusM(matrPov, m1)
