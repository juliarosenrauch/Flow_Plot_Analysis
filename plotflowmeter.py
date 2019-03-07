import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# # testing parser
# string = "3.168329E+1;4.375000E-2;3.168329E+1;0.000000E+0;3.168329E+1;0.000000E+0"
# string_split = string.split(';')
# if (len(string_split) is not 6):
#     print("Error in split")
# time = float(string_split[0])
# value = float(string_split[1])
#
# print("time:",time,", value:", value)



data = []
time = []

dataCF = []
timeCF = []


filename = './ignite_g_and_p_data/IP3plotdata20190301131619.txt'

with open(filename,'r') as f:
    # creating data for overall plot
    for line in f:
        if(line[0] is not '='):
            line_split = line.split(';')
            if (len(line_split) != 6):
                continue
            time.append(float(line_split[0]))
            data.append(float(line_split[1]))

# creating data for curve fit
with open(filename,'r') as f:
    for line in f:
        if(line[0] is not '='):
            line_split = line.split(';')
            if (len(line_split) != 6):
                continue
            if ((float(line_split[1]) > 1) and (float(line_split[1]) < 5)):
                timeCF.append(float(line_split[0]))
                dataCF.append(float(line_split[1]))
            if (float(line_split[1]) > 5):
                break


data = np.array(data)
time = np.array(time)
plt.plot(time, data, "bo", markersize=1)
plt.xlabel("Time (seconds)")
plt.ylabel("Flow (ml/min)")
plt.title("Flow approaching 6ml/min with 5ml plastic syringe" )


dataCF = np.array(dataCF)
timeCF = np.array(timeCF)

def fit_func(x, a, b):
    return a*x + b

params = curve_fit(fit_func, timeCF, dataCF)

[a, b] = params[0]
print ("a is,", a)
print ("b is,", b)

label = str(round(a,4))+"*x"+str(round(b,4))

plt.plot(timeCF, a*timeCF+b, "c-", markersize=1, label=label)
plt.legend(loc='lower right')

plt.show()
