import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import data_file
import fit_file
from matplotlib.lines import Line2D

# ***** PLASTIC 3 ML/MIN *****
filesP3 = ['./g_and_p_data/P3plotdata20190221152613.txt',
        './g_and_p_data/P3plotdata20190222094927.txt',
        './g_and_p_data/P3plotdata20190222095256.txt']

# ***** PLASTIC 6 ML/MIN *****
filesP6 = ['./g_and_p_data/P6plotdata20190221151706.txt',
        './g_and_p_data/P6plotdata20190221151827.txt',
        './g_and_p_data/P6plotdata20190221152020.txt']

 # ***** PLASTIC 9 ML/MIN *****
filesP9 = ['./g_and_p_data/P9plotdata20190221153424.txt',
        './g_and_p_data/P9plotdata20190222094320.txt',
        './g_and_p_data/P9plotdata20190222094505.txt',
        './g_and_p_data/P9plotdata20190222094616.txt']

# ***** GLASS 3 ML/MIN *****
filesG3 = ['./g_and_p_data/G3plotdata20190222100405.txt',
        './g_and_p_data/G3plotdata20190222100627.txt',
        './g_and_p_data/G3plotdata20190222101951.txt',
        './g_and_p_data/G3plotdata20190222102300.txt']

# ***** GLASS 6 ML/MIN *****
filesG6 = ['./g_and_p_data/G6plotdata20190222102751.txt',
        './g_and_p_data/G6plotdata20190222102840.txt',
        './g_and_p_data/G6plotdata20190222104604.txt',
        './g_and_p_data/G6plotdata20190222104712.txt']

# ***** GLASS 9 ML/MIN *****
filesG9 = ['./g_and_p_data/G9plotdata20190222105046.txt',
        './g_and_p_data/G9plotdata20190222105227.txt',
        './g_and_p_data/G9plotdata20190222105306.txt',
        './g_and_p_data/G9plotdata20190222105434.txt']

# **************************** IGNITE ****************************

# PLASTIC 3ML/MIN
filesIP3 = ['./ignite_g_and_p_data/IP3plotdata20190301131619.txt',
        './ignite_g_and_p_data/IP3plotdata20190301131737.txt',
        './ignite_g_and_p_data/IP3plotdata20190301131830.txt',
        './ignite_g_and_p_data/IP3plotdata20190301133410.txt']

# # PLASTIC 6ML/MIN
filesIP6 = ['./ignite_g_and_p_data/IP6plotdata20190301133759.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133500.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133642.txt',
        './ignite_g_and_p_data/IP6plotdata20190301133720.txt']

# # PLASTIC 9ML/MIN
filesIP9 = ['./ignite_g_and_p_data/IP9plotdata20190301133946.txt',
        './ignite_g_and_p_data/IP9plotdata20190301134026.txt',
        './ignite_g_and_p_data/IP9plotdata20190301134140.txt',
        './ignite_g_and_p_data/IP9plotdata20190301134212.txt']

# # GLASS 3ML/MIN
filesIG3 = ['./ignite_g_and_p_data/IG3plotdata20190301134437.txt',
        './ignite_g_and_p_data/IG3plotdata20190301134545.txt',
        './ignite_g_and_p_data/IG3plotdata20190301134639.txt',
        './ignite_g_and_p_data/IG3plotdata20190301140345.txt']

# # GLASS 6ML/MIN
filesIG6 = ['./ignite_g_and_p_data/IG6plotdata20190301140512.txt',
        './ignite_g_and_p_data/IG6plotdata20190301140916.txt',
        './ignite_g_and_p_data/IG6plotdata20190301141403.txt',
        './ignite_g_and_p_data/IG6plotdata20190301141723.txt']

# # GLASS 9ML/MIN
filesIG9 = ['./ignite_g_and_p_data/IG9plotdata20190301141828.txt',
        './ignite_g_and_p_data/IG9plotdata20190301141902.txt',
        './ignite_g_and_p_data/IG9plotdata20190301142046.txt',
        './ignite_g_and_p_data/IG9plotdata20190301142114.txt']

# IGNITE
purple = "#40128E"
magenta = "#E361EE"
orange = "#F07A23"
red = "r"

# ****** SET CONDITIONS FOR THE GRAPH ******
instrument = "NABT and IGNITE"         # options: "NABT", "IGNITE", "NABT and IGNITE"
syringe = "glass and plastic"            # options: "glass", "plastic", "glass and plastic"
flowrate = "all"            # options: 3, 6, 9, "all"

# data files and formats
if (instrument == "NABT and IGNITE"):
    if (syringe == "glass and plastic"):
        mastertime = [[] for i in range(12)]
        masterdata = [[] for i in range(12)]
        allfiles = [filesG3, filesG6, filesG9,
                    filesP3, filesP6, filesP9,
                    filesIG3, filesIG6, filesIG9,
                    filesIP3, filesIP6, filesIP9]
        formats = [['g.', 'y'], ['g.', 'y'], ['g.', 'y'],
                    ['b.', 'c'], ['b.', 'c'], ['b.', 'c'],
                    [orange, red], [orange, red], [orange, red],
                    [purple, magenta], [purple, magenta], [purple, magenta]]

    elif (syringe == "glass"):
        mastertime = [[] for i in range(6)]
        masterdata = [[] for i in range(6)]
        allfiles = [filesG3, filesG6, filesG9,
                    filesIG3, filesIG6, filesIG9]
        formats = [['g.', 'y'], ['g.', 'y'], ['g.', 'y'],
                    [orange, red], [orange, red], [orange, red]]

    elif (syringe == "plastic"):
        mastertime = [[] for i in range(6)]
        masterdata = [[] for i in range(6)]
        allfiles = [filesP3, filesP6, filesP9,
                    filesIP3, filesIP6, filesIP9]
        formats = [['b.', 'c'], ['b.', 'c'], ['b.', 'c'],
                    [purple, magenta], [purple, magenta], [purple, magenta]]

    else:
        print("Invalid syringe setting")

elif (instrument == "NABT"):
    if (syringe == "glass and plastic"):
        mastertime = [[] for i in range(6)]
        masterdata = [[] for i in range(6)]
        allfiles = [filesG3, filesG6, filesG9,
                    filesP3, filesP6, filesP9,]
        formats = [['g.', 'y'], ['g.', 'y'], ['g.', 'y'],
                    ['b.', 'c'], ['b.', 'c'], ['b.', 'c']]

    elif (syringe == "glass"):
        mastertime = [[] for i in range(3)]
        masterdata = [[] for i in range(3)]
        allfiles = [filesG3, filesG6, filesG9]
        formats = [['g.', 'y'], ['g.', 'y'], ['g.', 'y']]

    elif (syringe == "plastic"):
        mastertime = [[] for i in range(3)]
        masterdata = [[] for i in range(3)]
        allfiles = [filesP3, filesP6, filesP9]
        formats = [['b.', 'c'], ['b.', 'c'], ['b.', 'c']]
    else:
        print("Invalid syringe setting")

elif (instrument == "IGNITE"):
    if (syringe == "glass and plastic"):
        mastertime = [[] for i in range(6)]
        masterdata = [[] for i in range(6)]
        allfiles = [filesIG3, filesIG6, filesIG9,
                    filesIP3, filesIP6, filesIP9]
        formats = [[orange, red], [orange, red], [orange, red],
                    [purple, magenta], [purple, magenta], [purple, magenta]]

    elif (syringe == "glass"):
        mastertime = [[] for i in range(3)]
        masterdata = [[] for i in range(3)]
        allfiles = [filesIG3, filesIG6, filesIG9]
        formats = [[orange, red], [orange, red], [orange, red]]

    elif (syringe == "plastic"):
        mastertime = [[] for i in range(3)]
        masterdata = [[] for i in range(3)]
        allfiles = [filesIP3, filesIP6, filesIP9]
        formats = [[purple, magenta], [purple, magenta], [purple, magenta]]

    else:
        print("Invalid syringe setting")

else:
    print("Invalid instrument setting")

for i in range(len(allfiles)):
    for filename in allfiles[i]:
        file = data_file.data_file(filename)
        file.interpolate()

        for j in range(len(file.idata)):
            masterdata[i].append(file.idata[j])
            mastertime[i].append(file.itime[j])

    cf_file = fit_file.fit_file(mastertime[i], masterdata[i])
    cf_file.theoretical_fit(2, 3, formats[i][0], formats[i][1], syringe, "3, 6, and 9ml/min, on "+instrument)

# legend settings
if (instrument == "NABT and IGNITE"):
    if (syringe == "glass and plastic"):
        custom_lines = [Line2D([0], [0], color=red, lw=2),
                        Line2D([0], [0], color="y", lw=2),
                        Line2D([0], [0], color=magenta, lw=2),
                        Line2D([0], [0], color="c", lw=2),
                        Line2D([0], [0], color="k", lw=1)]
                        
        plt.legend(custom_lines,['Glass syringe on IGNITE',
                                'Glass syringe on NABT',
                                'Plastic syringe on IGNITE',
                                'Plastic syringe on NABT',
                                'Residuals'],
                                    loc="center right")

    elif (syringe == "glass"):
        custom_lines = [Line2D([0], [0], color="y", lw=2),
                        Line2D([0], [0], color=red, lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Glass syringe on NABT',
                                    'Glass syringe on IGNITE',
                                    'Residuals'],
                                    loc="center right")

    elif (syringe == "plastic"):
        custom_lines = [Line2D([0], [0], color="c", lw=2),
                        Line2D([0], [0], color=magenta, lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Plastic syringe on NABT',
                                    'Plastic syringe on IGNITE',
                                    'Residuals'],
                                    loc="center right")

elif (instrument == "NABT"):
    if (syringe == "glass and plastic"):
        custom_lines = [Line2D([0], [0], color="y", lw=2),
                        Line2D([0], [0], color="c", lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Glass syringe on NABT',
                                    'Plastic syringe on NABT',
                                    'Residuals'],
                                    loc="center right")

    elif (syringe == "glass"):
        custom_lines = [Line2D([0], [0], color="y", lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Glass syringe on NABT',
                                    'Residuals'],
                                    loc="center right")

    elif (syringe == "plastic"):
        custom_lines = [Line2D([0], [0], color="c", lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Plastic syringe on NABT',
                                    'Residuals'],
                                    loc="center right")

elif (instrument == "IGNITE"):
    if (syringe == "glass and plastic"):
        custom_lines = [Line2D([0], [0], color=red, lw=2),
                        Line2D([0], [0], color=magenta, lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Glass syringe on IGNITE',
                                    'Plastic syringe on IGNITE',
                                    'Residuals'],
                                    loc="center right")

    elif (syringe == "glass"):
        custom_lines = [Line2D([0], [0], color=red, lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Glass syringe on IGNITE',
                                    'Residuals'],
                                    loc="center right")

    elif (syringe == "plastic"):
        custom_lines = [Line2D([0], [0], color=magenta, lw=2),
                        Line2D([0], [0], color="k", lw=1)]

        plt.legend(custom_lines, ['Plastic syringe on IGNITE',
                                    'Residuals'],
                                    loc="center right")


plt.show()
