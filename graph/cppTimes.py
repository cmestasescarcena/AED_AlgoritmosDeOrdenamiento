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

"""
dataTree = [
[7.6e-05, 5.3e-05, 8.3e-05, 8.3e-05, 8.5e-05, 8.7e-05, 6.8e-05, 9.1e-05, 9.4e-05, 9.6e-05, 9.8e-05, 0.0001, 0.000107, 0.000114, 0.00013],
[0.000513, 0.000494, 0.000508, 0.00048, 0.000495, 0.000475, 0.000494, 0.000472, 0.000474, 0.000484, 0.000589, 0.000537, 0.00048, 0.000481, 0.000487],
[0.001137, 0.001086, 0.001115, 0.001066, 0.001089, 0.001046, 0.0012, 0.001137, 0.001073, 0.001063, 0.001229, 0.001043, 0.001132, 0.001079, 0.001063],
[0.001808, 0.00174, 0.001768, 0.002019, 0.001726, 0.001737, 0.001925, 0.001772, 0.001774, 0.001917, 0.00185, 0.001759, 0.0019, 0.001935, 0.001815],
[0.002578, 0.002338, 0.002458, 0.00234, 0.002315, 0.002498, 0.002607, 0.002456, 0.002305, 0.002331, 0.002626, 0.002455, 0.002305, 0.002351, 0.002319],
[0.003731, 0.003564, 0.003521, 0.004203, 0.003614, 0.003542, 0.004355, 0.00362, 0.0036, 0.003798, 0.004657, 0.003526, 0.003935, 0.004369, 0.003539],
[0.004261, 0.004255, 0.004106, 0.004482, 0.004154, 0.004109, 0.004252, 0.004159, 0.004414, 0.004544, 0.005173, 0.004195, 0.004209, 0.004125, 0.004078],
[0.005078, 0.004792, 0.004956, 0.0051, 0.0047, 0.005011, 0.004688, 0.005036, 0.005126, 0.00462, 0.006068, 0.004681, 0.005293, 0.005037, 0.004655],
[0.005724, 0.005286, 0.00641, 0.006355, 0.00691, 0.005295, 0.005866, 0.005248, 0.006114, 0.005248, 0.006397, 0.005257, 0.00547, 0.005435, 0.005534],
[0.008139, 0.009719, 0.009116, 0.009245, 0.009569, 0.009141, 0.009672, 0.009342, 0.009199, 0.009304, 0.009628, 0.009483, 0.009149, 0.009237, 0.010551],
[0.009855, 0.009851, 0.01132, 0.010034, 0.0102, 0.009535, 0.00982, 0.009633, 0.010815, 0.009716, 0.009738, 0.011402, 0.010293, 0.009467, 0.009548],
[0.023574, 0.030117, 0.02987, 0.029729, 0.029765, 0.030069, 0.029263, 0.028948, 0.029195, 0.032729, 0.02929, 0.030276, 0.030404, 0.029765, 0.030833],
[0.036524, 0.036525, 0.036622, 0.036299, 0.03605, 0.03669, 0.036274, 0.035798, 0.036806, 0.036613, 0.036107, 0.036566, 0.037865, 0.035902, 0.036241],
[0.071958, 0.097863, 0.095869, 0.09698, 0.098833, 0.095861, 0.094859, 0.096429, 0.095271, 0.09676, 0.097354, 0.096058, 0.096411, 0.094919, 0.095248],
[0.103145, 0.104593, 0.113683, 0.104231, 0.102692, 0.103691, 0.102907, 0.103193, 0.101088, 0.103811, 0.107897, 0.103443, 0.1037, 0.104169, 0.106177]
]
"""

dataTree = [
[0.000133, 5.4e-05, 8.5e-05, 9.5e-05, 9e-05, 0.000137, 6.4e-05, 9.9e-05, 9.7e-05, 0.000105, 0.0001, 0.000101, 0.000108, 0.000139, 0.000117],
[0.000549, 0.00051, 0.000538, 0.000579, 0.000508, 0.00049, 0.000504, 0.000512, 0.000485, 0.000571, 0.000586, 0.0005, 0.000495, 0.000496, 0.000499],
[0.001094, 0.001358, 0.002189, 0.001448, 0.001684, 0.001183, 0.001313, 0.001455, 0.00161, 0.001293, 0.001443, 0.001812, 0.001179, 0.001145, 0.001134],
[0.001938, 0.002169, 0.002189, 0.002172, 0.002349, 0.002325, 0.002985, 0.002437, 0.002209, 0.001939, 0.002327, 0.002378, 0.002463, 0.002007, 0.002421],
[0.002582, 0.002938, 0.00272, 0.002653, 0.002648, 0.003178, 0.002704, 0.002748, 0.002756, 0.003583, 0.002683, 0.00256, 0.002656, 0.002985, 0.002744],
[0.003655, 0.004008, 0.00562, 0.003936, 0.004149, 0.005185, 0.004033, 0.004232, 0.004232, 0.004165, 0.004605, 0.003998, 0.004263, 0.004353, 0.004585],
[0.004984, 0.005146, 0.004597, 0.005849, 0.004963, 0.00565, 0.005607, 0.005215, 0.005595, 0.004752, 0.004972, 0.005049, 0.004676, 0.005329, 0.004789],
[0.006766, 0.00654, 0.006327, 0.006285, 0.006412, 0.005585, 0.005369, 0.005128, 0.00516, 0.005247, 0.006103, 0.006205, 0.005751, 0.006661, 0.005644],
[0.00726, 0.00725, 0.008011, 0.006358, 0.00671, 0.005902, 0.006301, 0.005854, 0.006612, 0.006376, 0.006809, 0.005817, 0.006361, 0.006176, 0.00628],
[0.010468, 0.011665, 0.010532, 0.010392, 0.010274, 0.011416, 0.010199, 0.010748, 0.011193, 0.01059, 0.011268, 0.010666, 0.010205, 0.011677, 0.010932],
[0.012203, 0.011392, 0.010991, 0.010749, 0.010597, 0.010789, 0.010865, 0.011158, 0.010864, 0.011413, 0.010999, 0.012296, 0.012726, 0.011543, 0.01138],
[0.025353, 0.037792, 0.041294, 0.030733, 0.030788, 0.031642, 0.028358, 0.036207, 0.032954, 0.032579, 0.033141, 0.031571, 0.03676, 0.032708, 0.032111],
[0.044319, 0.04161, 0.043041, 0.042809, 0.042983, 0.040763, 0.041084, 0.040058, 0.043388, 0.03989, 0.039372, 0.042545, 0.039677, 0.043639, 0.044069],
[0.076692, 0.10251, 0.104843, 0.107221, 0.101937, 0.102067, 0.102355, 0.102489, 0.10623, 0.103365, 0.103983, 0.102861, 0.102758, 0.106098, 0.101872],
[0.112299, 0.110572, 0.111499, 0.113668, 0.113727, 0.112891, 0.109804, 0.104956, 0.105715, 0.105722, 0.117211, 0.114181, 0.111374, 0.110738, 0.111616],
]

dataMerge = [
[7e-06, 4e-06, 3e-06, 3e-06, 3e-06, 3e-06, 3e-06, 3e-06, 3e-06, 3e-06, 3e-06, 7e-06, 3e-06, 3e-06, 3e-06],
[8.2e-05, 9.3e-05, 8e-05, 7.4e-05, 6.8e-05, 6.7e-05, 7e-05, 6.5e-05, 6.4e-05, 6.7e-05, 7.9e-05, 8.1e-05, 7.5e-05, 7.8e-05, 7e-05],
[0.000183, 0.000175, 0.000154, 0.000166, 0.000154, 0.000162, 0.000162, 0.00015, 0.000156, 0.000146, 0.000149, 0.000148, 0.000197, 0.000155, 0.000153],
[0.00027, 0.000255, 0.00025, 0.000246, 0.000244, 0.000279, 0.000263, 0.000252, 0.000282, 0.000242, 0.000253, 0.000248, 0.000274, 0.000247, 0.000253],
[0.00038, 0.000357, 0.000429, 0.00036, 0.000381, 0.000341, 0.000348, 0.000349, 0.000389, 0.000337, 0.000381, 0.000344, 0.000335, 0.000337, 0.000451],
[0.000498, 0.000463, 0.000447, 0.000495, 0.000452, 0.000488, 0.000461, 0.00047, 0.000456, 0.000469, 0.000501, 0.000456, 0.000451, 0.000447, 0.000445],
[0.00056, 0.000537, 0.000725, 0.000564, 0.000662, 0.000539, 0.000521, 0.000514, 0.000529, 0.000506, 0.000511, 0.00064, 0.000609, 0.000534, 0.000553],
[0.000659, 0.00066, 0.000655, 0.000673, 0.000661, 0.000668, 0.000641, 0.000636, 0.000628, 0.000637, 0.0007, 0.000655, 0.000684, 0.000668, 0.000659],
[0.000785, 0.000759, 0.000915, 0.000839, 0.000774, 0.000748, 0.00074, 0.00075, 0.000775, 0.000789, 0.000781, 0.000761, 0.000747, 0.000748, 0.000804],
[0.000888, 0.000892, 0.000853, 0.000931, 0.000868, 0.000881, 0.001145, 0.000881, 0.00125, 0.000873, 0.000852, 0.001096, 0.000873, 0.000863, 0.000857],
[0.001023, 0.000969, 0.001102, 0.000982, 0.000994, 0.001041, 0.000985, 0.001136, 0.000931, 0.000963, 0.000936, 0.001023, 0.001195, 0.000942, 0.000926],
[0.002345, 0.002138, 0.002006, 0.002289, 0.001993, 0.002055, 0.002046, 0.001968, 0.002169, 0.002142, 0.00223, 0.002091, 0.002096, 0.002104, 0.002029],
[0.003287, 0.003123, 0.003244, 0.003341, 0.003325, 0.003053, 0.003208, 0.003212, 0.003247, 0.003232, 0.003174, 0.003708, 0.003367, 0.003202, 0.003347],
[0.004294, 0.004396, 0.004462, 0.00527, 0.004587, 0.004418, 0.004383, 0.004424, 0.005454, 0.004664, 0.004407, 0.004416, 0.004431, 0.004361, 0.004475],
[0.005593, 0.00554, 0.005661, 0.00553, 0.005533, 0.005516, 0.005658, 0.005425, 0.006095, 0.005526, 0.005609, 0.006335, 0.005559, 0.005814, 0.00571]
]


def prom(array): #Funcion de promedio
    row = len(array)
    promTimes = []
    for i in range(row):
        promT = sum(array[i])/15
        promTimes.append(promT)
    return promTimes

def devStand(array):
    row = len(array)
    devStd = []
    for i in range(row):
        devStd.append(np.std(array[i]))
    return(devStd)

print("**PROMEDIO Y DESVIACION ESTANDAR DE BUBBLE SORT**")
bubbleprom = prom(dataBubble)
bubbleStd = devStand(dataBubble)
print("Promedio")
print(bubbleprom)
print("Desviacion estandar")
print(bubbleStd, "\n")

print("**PROMEDIO Y DESVIACION ESTANDAR DE TREE SORT**")
treeprom = prom(dataTree)
treeStd = devStand(dataTree)
print("Promedio")
print(treeprom)
print("Desviacion estandar")
print(treeStd, "\n")

print("**PROMEDIO Y DESVIACION ESTANDAR DE MERGE SORT**")
mergeprom = prom(dataMerge)
mergeStd = devStand(dataMerge)
print("Promedio")
print(mergeprom)
print("Desviacion estandar")
print(mergeStd, "\n")

dataNqueens = [
[ 3e-06, 1e-06, 1e-06, 1e-06, 0, 1e-06, 1e-06, 1e-06, 0, 1e-06, 1e-06, 0, 0, 0, 0, ],
[ 8e-06, 6e-06, 3e-06, 2e-06, 2e-06, 2e-06, 2e-06, 3e-06, 2e-06, 2e-06, 4e-06, 3e-06, 2e-06, 2e-06, 2e-06, ],
[ 2.7e-05, 2.1e-05, 1.2e-05, 1e-05, 1.1e-05, 1.1e-05, 1e-05, 1e-05, 1.1e-05, 1.1e-05, 9e-06, 9e-06, 1.7e-05, 1e-05, 1e-05, ],
[ 0.000107, 9.7e-05, 9.1e-05, 8e-05, 6.9e-05, 5.3e-05, 6.8e-05, 6.1e-05, 5.3e-05, 5.3e-05, 6.1e-05, 4.8e-05, 5e-05, 7.2e-05, 6.6e-05, ],
[ 0.000497, 0.000397, 0.00036, 0.000349, 0.000399, 0.000406, 0.000416, 0.000432, 0.000415, 0.000392, 0.0004, 0.000402, 0.000397, 0.000403, 0.000408, ],
[ 0.001638, 0.001765, 0.001647, 0.001622, 0.001794, 0.001605, 0.001641, 0.001581, 0.001706, 0.00198, 0.001793, 0.0016, 0.001595, 0.001691, 0.00195, ],
[ 0.008044, 0.008124, 0.008315, 0.007708, 0.007709, 0.007943, 0.007904, 0.007741, 0.007927, 0.007502, 0.008007, 0.007353, 0.007331, 0.007508, 0.007398, ],
[ 0.041766, 0.040652, 0.040196, 0.042721, 0.040391, 0.041513, 0.040428, 0.041138, 0.040373, 0.038873, 0.041048, 0.0399, 0.039033, 0.039365, 0.039208, ],
[ 0.222067, 0.229251, 0.221703, 0.223473, 0.219968, 0.223572, 0.218294, 0.219244, 0.221557, 0.219316, 0.220271, 0.219266, 0.223518, 0.220303, 0.219958, ],
[ 1.32502, 1.3206, 1.33363, 1.32299, 1.32192, 1.31475, 1.32105, 1.31614, 1.31488, 1.32567, 1.31436, 1.31098, 1.31702, 1.31733, 1.31529, ],
[ 8.4046, 8.37392, 8.4081, 8.40937, 8.41353, 8.37865, 8.38131, 8.40052, 8.37713, 8.41797, 8.38757, 8.3775, 8.38919, 8.38202, 8.39007, ]
]

print("**PROMEDIO Y DESVIACION ESTANDAR DE N QUEENS**")
Nqueenprom = prom(dataNqueens)
NqueenStd = devStand(dataNqueens)
print("Promedio")
print(Nqueenprom)
print("Desviacion estandar")
print(NqueenStd, "\n")

