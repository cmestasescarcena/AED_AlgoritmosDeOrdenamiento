import matplotlib.pyplot as plt
import numpy as np

size = ['100', '1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000', '20000', '30000', '40000', '50000']

dataBubble = [
[5.3e-05, 2.5e-05, 2.4e-05, 2e-05, 3e-05, 3e-05, 2.1e-05, 2e-05, 2e-05, 2e-05, 1.7e-05, 1.8e-05, 1.8e-05, 2.9e-05, 2e-05],
[0.001585, 0.00158, 0.001621, 0.001546, 0.001546, 0.001654, 0.001535, 0.001564, 0.001537, 0.001601, 0.001553, 0.001523, 0.001654, 0.001497, 0.001539],
[0.005985, 0.006425, 0.005894, 0.006141, 0.005948, 0.006398, 0.005951, 0.006094, 0.006217, 0.005622, 0.006934, 0.005935, 0.006791, 0.006119, 0.005939],
[0.01336, 0.013241, 0.013632, 0.014295, 0.014532, 0.013634, 0.013636, 0.013415, 0.014046, 0.013455, 0.013959, 0.013965, 0.014104, 0.014212, 0.013785],
[0.025238, 0.025293, 0.025452, 0.024234, 0.024363, 0.024531, 0.024564, 0.024762, 0.024951, 0.026484, 0.024272, 0.024178, 0.025352, 0.024504, 0.025729],
[0.041534, 0.039455, 0.039471, 0.040928, 0.041278, 0.038777, 0.038667, 0.039542, 0.038448, 0.040875, 0.0407, 0.04011, 0.040056, 0.040407, 0.038612],
[0.068046, 0.069391, 0.063753, 0.059015, 0.066335, 0.059864, 0.058953, 0.058758, 0.058155, 0.05816, 0.057057, 0.059241, 0.060255, 0.060486, 0.058739],
[0.08464, 0.083235, 0.080713, 0.081645, 0.082677, 0.083966, 0.080234, 0.081549, 0.082576, 0.082994, 0.084271, 0.082252, 0.081668, 0.081693, 0.082797],
[0.123089, 0.114476, 0.111587, 0.111571, 0.11083, 0.111809, 0.109987, 0.109382, 0.109043, 0.111535, 0.110164, 0.110336, 0.110352, 0.109559, 0.11114],
[0.142479, 0.141629, 0.147152, 0.14155, 0.142298, 0.141954, 0.143338, 0.144298, 0.14318, 0.144133, 0.145594, 0.14488, 0.14423, 0.147176, 0.144127],
[0.179872, 0.180779, 0.18155, 0.180168, 0.179284, 0.179317, 0.185087, 0.182115, 0.176608, 0.182965, 0.181745, 0.182259, 0.180036, 0.179151, 0.180938],
[0.806817, 0.803312, 0.804324, 0.802648, 0.803495, 0.803279, 0.801135, 0.800443, 0.805587, 0.81417, 0.802271, 0.80915, 0.797409, 0.802927, 0.810377],
[1.89302, 1.89429, 1.88486, 1.8967, 1.88044, 1.91193, 1.88516, 1.88808, 1.89086, 1.89018, 1.88612, 1.89087, 1.88127, 1.8844, 1.88553],
[3.43299, 3.428, 3.42994, 3.44781, 3.44608, 3.42651, 3.43094, 3.43591, 3.41578, 3.42373, 3.42811, 3.42121, 3.43968, 3.4381, 3.43587],
[5.43486, 5.43973, 5.44149, 5.43678, 5.41911, 5.44679, 5.43344, 5.44535, 5.44592, 5.44927, 5.45873, 5.41968, 5.41548, 5.43948, 5.44679]
]

dataTree = [
[0.000119, 9.8e-05, 0.000213, 0.000803, 0.000567, 0.000398, 0.000282, 0.000134, 0.006187, 0.00625, 0.006757, 0.006037, 0.005786, 0.00656, 0.005577],
[0.049606, 0.038518, 0.028487, 0.018413, 0.008526, 0.00096, 0.000504, 0.000483, 0.000785, 0.00069, 0.000561, 0.00051, 0.000498, 0.0005, 0.00048],
[0.001059, 0.001048, 0.001057, 0.00104, 0.001246, 0.00115, 0.001072, 0.001083, 0.001041, 0.00107, 0.001129, 0.001052, 0.001034, 0.001465, 0.001108],
[0.001864, 0.001774, 0.001769, 0.001733, 0.001736, 0.00183, 0.001943, 0.001749, 0.001732, 0.00191, 0.001742, 0.001816, 0.001764, 0.001732, 0.001811],
[0.00233, 0.003028, 0.002646, 0.002298, 0.002358, 0.002794, 0.002323, 0.002492, 0.00231, 0.002167, 0.002523, 0.002207, 0.002326, 0.002178, 0.00233],
[0.003545, 0.003552, 0.003653, 0.003703, 0.003466, 0.003584, 0.003857, 0.003447, 0.003447, 0.003637, 0.003507, 0.003427, 0.003926, 0.003345, 0.003336],
[0.004533, 0.003988, 0.003962, 0.004642, 0.004131, 0.004391, 0.004181, 0.004103, 0.004433, 0.004131, 0.004319, 0.005307, 0.004147, 0.004432, 0.004265],
[0.004839, 0.005348, 0.004912, 0.004931, 0.004835, 0.004684, 0.004947, 0.004762, 0.004879, 0.004893, 0.004985, 0.005083, 0.004538, 0.005159, 0.004478],
[0.005475, 0.005057, 0.00523, 0.005473, 0.005253, 0.005332, 0.005032, 0.006308, 0.005018, 0.005774, 0.005019, 0.00589, 0.005205, 0.005811, 0.005238],
[0.007683, 0.009317, 0.008971, 0.009354, 0.009132, 0.00897, 0.008916, 0.009468, 0.008944, 0.009189, 0.009059, 0.009115, 0.008926, 0.010292, 0.010592],
[0.010636, 0.009361, 0.009905, 0.010493, 0.010213, 0.009849, 0.009409, 0.009433, 0.009664, 0.009863, 0.009794, 0.009714, 0.010418, 0.009696, 0.009412],
[0.023325, 0.029619, 0.029059, 0.029207, 0.029118, 0.030054, 0.030009, 0.029399, 0.029678, 0.029561, 0.029127, 0.028895, 0.029569, 0.028691, 0.029588],
[0.035991, 0.035412, 0.037721, 0.036046, 0.035118, 0.035558, 0.037355, 0.035668, 0.035902, 0.0364, 0.035524, 0.035201, 0.037202, 0.035884, 0.036195],
[0.07104, 0.095807, 0.099121, 0.098971, 0.096951, 0.099783, 0.095546, 0.096809, 0.096426, 0.094464, 0.096613, 0.094982, 0.097212, 0.095387, 0.097024],
[0.108348, 0.106537, 0.105552, 0.103853, 0.106177, 0.105467, 0.107043, 0.105886, 0.111434, 0.10851, 0.110561, 0.105202, 0.102339, 0.101052, 0.105843]
]

dataMerge = [
[8e-06, 7e-06, 6e-06, 4e-06, 4e-06, 7e-06, 5e-06, 4e-06, 4e-06, 4e-06, 4e-06, 4e-06, 4e-06, 4e-06, 4e-06, ],
[9.6e-05, 0.000104, 7.8e-05, 6.9e-05, 6.5e-05, 7.2e-05, 0.0001, 8.1e-05, 8.2e-05, 7.7e-05, 9e-05, 7.8e-05, 7.9e-05, 7.6e-05, 7.4e-05, ],
[0.000152, 0.000152, 0.000144, 0.000144, 0.000145, 0.000148, 0.000146, 0.000144, 0.000168, 0.000204, 0.000186, 0.00017, 0.00016, 0.000155, 0.000151],
[0.00025, 0.000245, 0.000239, 0.000237, 0.000237, 0.000266, 0.000276, 0.000261, 0.000245, 0.000259, 0.000237, 0.000237, 0.00024, 0.000231, 0.000233],
[0.000345, 0.000356, 0.000345, 0.000345, 0.000329, 0.000319, 0.000329, 0.000325, 0.00045, 0.000349, 0.00036, 0.000412, 0.000359, 0.000358, 0.000343],
[0.000466, 0.000507, 0.000743, 0.000459, 0.000508, 0.000448, 0.000439, 0.000518, 0.000458, 0.000556, 0.000466, 0.000455, 0.000453, 0.000461, 0.000475],
[0.000557, 0.000558, 0.000662, 0.000563, 0.000544, 0.00056, 0.000552, 0.000664, 0.000608, 0.000563, 0.000643, 0.000549, 0.000534, 0.000538, 0.000577],
[0.000668, 0.000652, 0.000668, 0.000655, 0.000678, 0.000783, 0.0008, 0.000648, 0.000667, 0.000653, 0.000659, 0.000669, 0.000648, 0.000653, 0.000648],
[0.000847, 0.000785, 0.000775, 0.000739, 0.000752, 0.00076, 0.001079, 0.000746, 0.000926, 0.000779, 0.00079, 0.00079, 0.000801, 0.000717, 0.000905],
[0.000882, 0.000881, 0.000863, 0.000876, 0.000985, 0.000869, 0.000882, 0.000872, 0.00101, 0.000866, 0.000886, 0.000852, 0.000858, 0.000873, 0.000877],
[0.000967, 0.000995, 0.000995, 0.000969, 0.000957, 0.001157, 0.001251, 0.001052, 0.000979, 0.000948, 0.000994, 0.000967, 0.000976, 0.00098, 0.001025],
[0.002058, 0.002225, 0.00208, 0.00231, 0.002073, 0.002072, 0.002067, 0.002077, 0.002069, 0.001971, 0.002481, 0.002003, 0.002092, 0.002088, 0.002449],
[0.003259, 0.003197, 0.003548, 0.003156, 0.003153, 0.003378, 0.00343, 0.003164, 0.003243, 0.003065, 0.003199, 0.003262, 0.003348, 0.003075, 0.004268],
[0.004411, 0.005018, 0.004503, 0.004628, 0.004598, 0.004636, 0.004397, 0.004399, 0.004383, 0.004395, 0.004508, 0.004538, 0.004923, 0.004499, 0.004446],
[0.005695, 0.005461, 0.005296, 0.005347, 0.005675, 0.005782, 0.005878, 0.005758, 0.005638, 0.005596, 0.005548, 0.005648, 0.0057, 0.006236, 0.00572]
]


def prom(array): #Funcion de promedio
    row = len(array)
    promTimes = []
    for i in range(row):
        promT = sum(array[i])/15
        promTimes.append(promT)
    return promTimes

bubble = prom(dataBubble)
plt.plot(size, bubble)
plt.show()