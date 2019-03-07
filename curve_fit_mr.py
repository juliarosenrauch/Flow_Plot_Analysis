import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import data_file
import fit_file

# add all the data to one array and then curve fit it
masterdata = []
mastertime = []

# ************************ NABT RUNS ***************************
# PLASTIC 3ML/MIN
# files = ['./g_and_p_data/P3plotdata20190221152613.txt',
#         './g_and_p_data/P3plotdata20190222094927.txt',
#         './g_and_p_data/P3plotdata20190222095256.txt']
# 'P3plotdata20190222095141.txt' this file is a bad run

# # PLASTIC 6ML/MIN
# files = ['./g_and_p_data/P6plotdata20190221151706.txt',
#         './g_and_p_data/P6plotdata20190221151827.txt',
#         './g_and_p_data/P6plotdata20190221152020.txt']
# # 'P6plotdata20190221152357.txt' this file is a bad run

# # PLASTIC 9ML/MIN
# files = ['./g_and_p_data/P9plotdata20190221153424.txt',
#         './g_and_p_data/P9plotdata20190222094320.txt',
#         './g_and_p_data/P9plotdata20190222094505.txt',
#         './g_and_p_data/P9plotdata20190222094616.txt']

# # GLASS 3ML/MIN
# files = ['./g_and_p_data/G3plotdata20190222100405.txt',
#         './g_and_p_data/G3plotdata20190222100627.txt',
#         './g_and_p_data/G3plotdata20190222101951.txt',
#         './g_and_p_data/G3plotdata20190222102300.txt']

# # GLASS 6ML/MIN
# files = ['./g_and_p_data/G6plotdata20190222102751.txt',
#         './g_and_p_data/G6plotdata20190222102840.txt',
#         './g_and_p_data/G6plotdata20190222104604.txt',
#         './g_and_p_data/G6plotdata20190222104712.txt']

# # GLASS 9ML/MIN
# files = ['./g_and_p_data/G9plotdata20190222105046.txt',
#         './g_and_p_data/G9plotdata20190222105227.txt',
#         './g_and_p_data/G9plotdata20190222105306.txt',
#         './g_and_p_data/G9plotdata20190222105434.txt']


# ************************ IGNITE RUNS ***************************
# PLASTIC 3ML/MIN
# files = ['./ignite_g_and_p_data/IP3plotdata20190301131619.txt',
#         './ignite_g_and_p_data/IP3plotdata20190301131737.txt',
#         './ignite_g_and_p_data/IP3plotdata20190301131830.txt',
#         './ignite_g_and_p_data/IP3plotdata20190301133410.txt']

# # PLASTIC 6ML/MIN
files = ['./ignite_g_and_p_data/IP6plotdata20190301133759.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133500.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133642.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133720.txt']

# # PLASTIC 9ML/MIN
# files = ['./ignite_g_and_p_data/IP9plotdata20190301133946.txt',
#         './ignite_g_and_p_data/IP9plotdata20190301134026.txt',
#         './ignite_g_and_p_data/IP9plotdata20190301134140.txt',
#         './ignite_g_and_p_data/IP9plotdata20190301134212.txt']

# # GLASS 3ML/MIN
# files = ['./ignite_g_and_p_data/IG3plotdata20190301134437.txt',
#         './ignite_g_and_p_data/IG3plotdata20190301134545.txt',
#         './ignite_g_and_p_data/IG3plotdata20190301134639.txt',
#         './ignite_g_and_p_data/IG3plotdata20190301140345.txt']

# # GLASS 6ML/MIN
# files = ['./ignite_g_and_p_data/IG6plotdata20190301140512.txt',
#         './ignite_g_and_p_data/IG6plotdata20190301140916.txt',
#         './ignite_g_and_p_data/IG6plotdata20190301141403.txt',
#         './ignite_g_and_p_data/IG6plotdata20190301141723.txt']

# # GLASS 9ML/MIN
# files = ['./ignite_g_and_p_data/IG9plotdata20190301141828.txt',
#         './ignite_g_and_p_data/IG9plotdata20190301141902.txt',
#         './ignite_g_and_p_data/IG9plotdata20190301142046.txt',
#         './ignite_g_and_p_data/IG9plotdata20190301142114.txt']

# ****** plotting 1 group of runs (interpolated) at the same setting (with fitting) ******
for filename in files:
    file = data_file.data_file(filename)
    file.interpolate()

    for i in range(len(file.idata)):
        masterdata.append(file.idata[i])
        mastertime.append(file.itime[i])

# IGNITE
purple = "#40128E"
magenta = "#E361EE"
orange = "#F07A23"
red = "r"

cf_file = fit_file.fit_file(mastertime, masterdata)
# cf_file.standard_fit(0.01, 1, "time", "logarithmic")
cf_file.theoretical_fit(6,8, orange, red,"plastic","6ml/min")

plt.show()
# ****************************************************************************************
