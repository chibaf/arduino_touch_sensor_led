import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0.0]*100

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  line = ser.readline()
  line1=line.strip().decode('utf-8')
  line2=line1.split(',')
  d=float(line2[1])
  print(d)
  data.pop(-1)
  data.insert(0,d)
  plt.clf()
  plt.ylim([-1.0,1500.0])
  plt.plot(x,data)
  plt.pause(0.1)
