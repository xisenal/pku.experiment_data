import numpy as np
#屮，最离谱的一集
#未知变量为a1,a2,a3,a4,b1,b2,b3,b4,b5,b6,c1,c2,c3,c4,c5,c6.
A = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1/2,0,1/2,0,0,0,0,0,0,0,0,1,0,0,0,0],
              [0,1/2,0,1/2,0,0,0,0,0,0,0,0,0,0,1,0],
              [0,1/2,0,1/2,0,0,0,0,1,0,0,0,0,0,0,0],
              [1/2,0,1/2,0,0,1,0,0,0,0,0,0,0,0,0,0],
              [1/4,1/4,1/4,1/4,0,1/2,0,0,1/2,0,1/2,0,1/2,-1/2,0,1/2],
              [1/4,1/4,1/4,1/4,1/2,1/2,1/2,1/2,1/2,1/2,0,0,0,0,0,0],
              [1/4,1/4,1/4,1/4,1/2,0,0,0,0,1/2,0,1/2,1/2,1/2,1/2,0],
              [1/4,1/4,1/4,1/4,0,0,-1/2,1/2,0,0,1/2,1/2,0,0,1/2,1/2],
              [1/2,1/2,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
              [1/2,1/2,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1/2,1/2,0,0,0,0,0,1,0,0,0,0,0,0],
              [0,0,1/2,1/2,0,0,0,0,0,0,0,0,0,0,0,1]])
sum_cal=np.mean([54,74,41,48,41])+np.mean([2739,2657,2746,2763,2709])+np.mean([62,57,52,59,72])+np.mean([2220,2275,2178,2200])
b = np.array([[np.mean([54,74,41,48,41])],
              [np.mean([2739,2657,2746,2763,2709])],
              [np.mean([62,57,52,59,72])],
              [np.mean([2220,2275,2178,2200])],
              [np.mean([1456,1412,1402,1464,1372])],
              [np.mean([1091,1082,1057,1111,1028])],
              [np.mean([1422,1384,1408,1444,1390])],
              [np.mean([1314,1326,1368,1321,1318])],
              [np.mean([2271,2266,2377,2221,2326])],
              [np.mean([2427,2486,2420,2349,2349])],
              [np.mean([589,630,601,570,549])],
              [np.mean([2152,2210,2294,2256,2188])],
              [np.mean([1700,1658,1705,1685,1675])],
              [np.mean([1334,1394,1332,1292,1412])],
              [np.mean([1354,1329,1355,1358,1397])],
              [np.mean([949,951,916,880,898])]])
b=b/sum_cal
x = np.linalg.solve(A, b)
a1,a2,a3,a4,b1,b2,b3,b4,b5,b6,c1,c2,c3,c4,c5,c6=x
a1=float(a1)
a2=float(a2)
a3=float(a3)
a4=float(a4)
b1=float(b1)
b2=float(b2)
b3=float(b3)
b4=float(b4)
b5=float(b5)
b6=float(b6)
c1=float(c1)
c2=float(c2)
c3=float(c3)
c4=float(c4)
c5=float(c5)
c6=float(c6)
rho=np.matrix([[a1,b1+c1*1j,b2+c2*1j,b3+c3*1j],
              [b1-c1*1j,a2,b4+c4*1j,b5+c5*1j],
              [b2-c2*1j,b4-c4*1j,a3,b6+c6*1j],
              [b3-c3*1j,b5-c5*1j,b6-c6*1j,a4]])
print(rho)
