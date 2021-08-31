# Example program from https://github.com/squillero/python_the-hard-way
# Copyright © 2021 Giovanni Squillero <squillero@polito.it>
# Free for personal or classroom use; see 'LICENCE.md' for details.

data = [
    0.662719993, 0.826647583, 0.451436291, 0.81010697, 0.432401842, 0.822987053, 0.971883051,
    0.0975812, 0.47752862, 0.038958378, 0.045555378, 0.232078072, 0.656400287, 0.608264548,
    0.208160965, 0.397799489, 0.074405305, 0.734716437, 0.977429035, 0.757137655, 0.648304602,
    0.859392349, 0.112152984, 0.539415419, 0.515208838, 0.757765639, 0.514360053, 0.494890294,
    0.701493815, 0.61646899, 0.627466966, 0.585502991, 0.971912103, 0.341590568, 0.458292183,
    0.323257387, 0.313809337, 0.334541803, 0.381433861, 0.00893834, 0.270426415, 0.14553096,
    0.414964813, 0.311518168, 0.179442168, 0.877722687, 0.95969137, 0.36413393, 0.091828664,
    0.86249845, 0.558761504, 0.976228609, 0.763802015, 0.61081586, 0.173120931, 0.301780374,
    0.511756805, 0.583303757, 0.9514366, 0.273952653, 0.496007598, 0.300272116, 0.518574322,
    0.228873899, 0.595885359, 0.802330028, 0.112322197, 0.719847345, 0.171305684, 0.324399966,
    0.708137402, 0.466745683, 0.688032092, 0.137200667, 0.614304145, 0.04535652, 0.013754618,
    0.161071501, 0.055906238, 0.170270914, 0.485795467, 0.051235578, 0.265172381, 0.564101935,
    0.229187492, 0.09986199, 0.840593284, 0.614599532, 0.996836985, 0.087339066, 0.006839642,
    0.320501804, 0.665077015, 0.06195954, 0.59990903, 0.354909216, 0.654428302, 0.773783355,
    0.376246394, 0.342750318, 0.678582736, 0.478747557, 0.675050605, 0.163926179, 0.665223308,
    0.728402082, 0.900514188, 0.837798004, 0.890128268, 0.684201714, 0.276589209, 0.698558621,
    0.486168155, 0.865429834, 0.528751903, 0.019626751, 0.426059279, 0.941922478, 0.886702402,
    0.382168214, 0.102167195, 0.013669803, 0.395162881, 0.566442909, 0.692271144, 0.744960403,
    0.884414011, 0.105603067, 0.882841899, 0.749502651, 0.94612585, 0.285933531, 0.068208001,
    0.153346615, 0.958876717, 0.221348091, 0.308708538, 0.783364302, 0.552123595, 0.18806416,
    0.427089183, 0.463078252, 0.850480402, 0.273791452, 0.854852169, 0.968406893, 0.922495167,
    0.474979253, 0.587575225, 0.553730825, 0.1952588, 0.064510949, 0.707490458, 0.103025158,
    0.328248926, 0.286550992, 0.499053848, 0.243396937, 0.37731547, 0.831141412, 0.197318738,
    0.291344503, 0.866245002, 0.668796566, 0.955322769, 0.735519198, 0.125333827, 0.243463688,
    0.677210271, 0.799295207, 0.428676476, 0.651718037, 0.809781678, 0.253772141, 0.061888856,
    0.200084114, 0.684358326, 0.926677988, 0.349976621, 0.610861423, 0.585340409, 0.444792504,
    0.459654161, 0.055934907, 0.960949388, 0.90156799, 0.417518802, 0.517616065, 0.283899756,
    0.565714416, 0.31315271, 0.658245485, 0.187177981, 0.102439017, 0.372499623, 0.131848907,
    0.364103899, 0.738372948, 0.501593005, 0.592937953, 0.431085735, 0.650851475, 0.00123301,
    0.822191781, 0.028419398, 0.501464979, 0.858011926, 0.406940946, 0.012585516, 0.735591054,
    0.7657351, 0.462257069, 0.292604739, 0.528208495, 0.08264668, 0.640809299, 0.730778326,
    0.486980854, 0.047231972, 0.645614382, 0.684755257, 0.558561832, 0.310330176, 0.870683012,
    0.047198361, 0.961442869, 0.172753386, 0.609700951, 0.783047175, 0.599043362, 0.306800602,
    0.496153235, 0.303434058, 0.21836797, 0.137454933, 0.953813142, 0.987490261, 0.355209478,
    0.775154284, 0.404146531, 0.162031751, 0.580269865, 0.102870003, 0.580415147, 0.304143506,
    0.960428242, 0.743228448, 0.482239709, 0.793618527, 0.089091289, 0.453468023, 0.265914636,
    0.580078104, 0.648164251, 0.959026051, 0.774440928, 0.04685796, 0.731418118, 0.079189879,
    0.221846373, 0.312531306, 0.894173797, 0.420414418, 0.739099539, 0.357239653, 0.457266523,
    0.233423912, 0.274437464, 0.551991301, 0.625481223, 0.922867074, 0.40221591, 0.787856141,
    0.303886253, 0.115899792, 0.147164602, 0.122826005, 0.652259943, 0.389933005, 0.44148369,
    0.67636457, 0.059435305, 0.604304834, 0.943455804, 0.727449306, 0.799408189, 0.721368079,
    0.564836903, 0.13703219, 0.600776448, 0.203225125, 0.620899267, 0.074597834, 0.639686424,
    0.572191878, 0.467158695, 0.93674039, 0.140695798, 0.192142203, 0.160295415, 0.666643293,
    0.66614338, 0.330094584, 0.543617921, 0.937520885, 0.364652896, 0.708806374, 0.230304466,
    0.577975715, 0.289863518, 0.021776314, 0.138821325, 0.904701808, 0.525984906, 0.601464978,
    0.545212235, 0.085019089, 0.555061281, 0.018238321, 0.406423191, 0.314015798, 0.461990531,
    0.282215611, 0.370131754, 0.043665804, 0.648393668, 0.403086719, 0.805570233, 0.255706771,
    0.922464552, 0.453602701, 0.455449967, 0.254041841, 0.74292866, 0.287228861, 0.74185221,
    0.012038005, 0.487137751, 0.604193242, 0.176466825, 0.672209347, 0.503913229, 0.085193115,
    0.063416106, 0.167240614, 0.583598631, 0.796906428, 0.057442679, 0.584785033, 0.985544453,
    0.679973782, 0.753671258, 0.507087914, 0.923801946, 0.459523099, 0.915071203, 0.15638085,
    0.395370864, 0.176139243, 0.631228219, 0.523760283, 0.276031467, 0.204734601, 0.796945786,
    0.873549895, 0.395385198, 0.946346486, 0.266668586, 0.105149059, 0.623145212, 0.162228145,
    0.969598669, 0.967264947, 0.382448844, 0.613766203, 0.030902356, 0.794530054, 0.317717454,
    0.634417604, 0.333125701, 0.396641939, 0.657494275, 0.009866656, 0.091579883, 0.80039865,
    0.172279377, 0.8408342, 0.14389228, 0.358332426, 0.317601849, 0.804544002, 0.892980663,
    0.714091377, 0.261273855, 0.12640514, 0.306931377, 0.770146172, 0.570633547, 0.005062268,
    0.114416087, 0.640703383, 0.980553832, 0.617747789, 0.920272127, 0.30431647, 0.117424279,
    0.160963813, 0.885767341, 0.652325723, 0.263188284, 0.305185494, 0.3118532, 0.882111883,
    0.108271558, 0.627209257, 0.351413525, 0.837347727, 0.649521762, 0.332838335, 0.710555954,
    0.314332374, 0.636528832, 0.347911108, 0.15903122, 0.873590611, 0.45429726, 0.984362956,
    0.388168206, 0.365212683, 0.150230422, 0.962200803, 0.151498325, 0.558111975, 0.729771401,
    0.254044098, 0.801100329, 0.50939356, 0.889066972, 0.549698307, 0.43425189, 0.704089303,
    0.247223198, 0.24388777, 0.575049965, 0.755766107, 0.081427108, 0.300125138, 0.399823139,
    0.106478447, 0.231777481, 0.565692991, 0.481869352, 0.948061948, 0.246407417, 0.55473953,
    0.010143148, 0.025281024, 0.230527493, 0.88701862, 0.670439222, 0.142839691, 0.476741109,
    0.530424901, 0.662825883, 0.532643117, 0.803630967, 0.073862934, 0.782462676, 0.198479028,
    0.336188478, 0.335333279, 0.527305137, 0.766230907, 0.081569527, 0.011864303, 0.861401112,
    0.646696847, 0.527919981, 0.252605014, 0.635284891, 0.026597954, 0.215676527, 0.236779062,
    0.659341652, 0.226662178, 0.016032758, 0.137113283, 0.04958194, 0.618018694, 0.559624049,
    0.590923505, 0.929521132, 0.771476495, 0.168200866, 0.063289676, 0.929551651, 0.523358696,
    0.732890002, 0.392937963, 0.145324099, 0.127233787, 0.548125143, 0.049906896, 0.939592213,
    0.939071395, 0.518699699, 0.127735589, 0.009697307, 0.909432178, 0.144108313, 0.861642457,
    0.958506845, 0.82429887, 0.537000791, 0.922342936, 0.952233541, 0.15368804, 0.529044779,
    0.302847659, 0.636843366, 0.321763045, 0.122762493, 0.454289026, 0.719126208, 0.183533776,
    0.663346926, 0.975791598, 0.421512867, 0.599763577, 0.166931034, 0.726921549, 0.045428884,
    0.799265428, 0.610999123, 0.944564134, 0.869161924, 0.038297702, 0.204417633, 0.574523741,
    0.916743984, 0.088392181, 0.411994956, 0.658166269, 0.197423068, 0.299183922, 0.646127003,
    0.537163341, 0.599452947, 0.470539039, 0.619278473, 0.968300378, 0.663781188, 0.474719503,
    0.125226423, 0.674849743, 0.571525686, 0.324299116, 0.957639807, 0.391392525, 0.845865918,
    0.088877714, 0.165942031, 0.139320156, 0.282170667, 0.718376057, 0.73338567, 0.771673524,
    0.449678048, 0.96919765, 0.134004211, 0.687917349, 0.291651857, 0.431747757, 0.428654465,
    0.591538136, 0.734802587, 0.923225214, 0.028251007, 0.473448559, 0.325771718, 0.181868869,
    0.023504221, 0.713253996, 0.127262391, 0.017576544, 0.445830983, 0.146356959, 0.969611183,
    0.052614551, 0.990976076, 0.78364248, 0.965409776, 0.805024558, 0.829384603, 0.886908468,
    0.021557289, 0.085817619, 0.685725323, 0.262152059, 0.588598575, 0.9701523, 0.881561289,
    0.355582645, 0.738501166, 0.650727806, 0.561482028, 5.99216E-05, 0.078198485, 0.649922967,
    0.383692586, 0.534931946, 0.484019042, 0.470578897, 0.94581322, 0.799190552, 0.825228093,
    0.8394599, 0.101727877, 0.551027324, 0.482726714, 0.531729842, 0.455458525, 0.446475535,
    0.37157265, 0.34565959, 0.876717358, 0.24837876, 0.402195402, 0.196586353, 0.318632155,
    0.431394184, 0.455744555, 0.770803527, 0.539433667, 0.763506154, 0.529447446, 0.796295123,
    0.40205879, 0.910383759, 0.118356233, 0.235663782, 0.16136083, 0.81949971, 0.09654847,
    0.621479229, 0.018945711, 0.145222783, 0.820734799, 0.541396069, 0.162680778, 0.769695653,
    0.536936852, 0.778379935, 0.619416124, 0.646153514, 0.551349394, 0.630187046, 0.688897393,
    0.971056114, 0.805064923, 0.764059431, 0.30916867, 0.465387856, 0.80872522, 0.65463749,
    0.035937932, 0.387276315, 0.360882739, 0.417922416, 0.836335351, 0.380570706, 0.539827186,
    0.581628935, 0.875161013, 0.622566394, 0.07429205, 0.663964616, 0.062380048, 0.367662274,
    0.839284356, 0.635188852, 0.203023469, 0.458903302, 0.32985795, 0.347030544, 0.899605028,
    0.845132313, 0.00857479, 0.537366153, 0.214940275, 0.866435508, 0.431008487, 0.881918889,
    0.477788682, 0.890827609, 0.727146881, 0.070815748, 0.941250323, 0.426763269, 0.080322646,
    0.437285832, 0.524560973, 0.512749146, 0.546026939, 0.397477852, 0.687146354, 0.604095382,
    0.613454988, 0.991921385, 0.001294468, 0.250715639, 0.661093537, 0.873445812, 0.060840538,
    0.105534525, 0.45716214, 0.54120677, 0.157103148, 0.779642607, 0.795695516, 0.734218865,
    0.579289832, 0.307051244, 0.917750524, 0.805355415, 0.025976864, 0.745472199, 0.011857573,
    0.527723082, 0.849051629, 0.754038242, 0.566079997, 0.963020089, 0.107957306, 0.57816016,
    0.350118781, 0.557755396, 0.503138567, 0.697420363, 0.268406009, 0.823573205, 0.986695043,
    0.016696594, 0.94473616, 0.486346952, 0.878737343, 0.525513796, 0.334135628, 0.65472285,
    0.033355433, 0.699634776, 0.314804816, 0.207206992, 0.876436676, 0.424059209, 0.880824124,
    0.3519222, 0.186302517, 0.765355436, 0.671122082, 0.763411648, 0.462922559, 0.539919838,
    0.076461059, 0.095916812, 0.927838082, 0.911636836, 0.858167734, 0.688655124, 0.603849922,
    0.436048051, 0.037222894, 0.087140283, 0.386261246, 0.32210661, 0.047883563, 0.767078475,
    0.961614939, 0.682261094, 0.431940349, 0.573730305, 0.355664899, 0.421854751, 0.577268857,
    0.172910625, 0.490910262, 0.379019736, 0.964740338, 0.080931104, 0.644696122, 0.69030319,
    0.630610985, 0.182096703, 0.918633171, 0.41133796, 0.75644106, 0.96303982, 0.131911514,
    0.272423924, 0.700932504, 0.459736047, 0.174181161, 0.168602789, 0.632061633, 0.285352019,
    0.149775504, 0.531349346, 0.529666608, 0.339619085, 0.816225779, 0.324901046, 0.964785598,
    0.919683121, 0.557974423, 0.73148613, 0.025871816, 0.135662141, 0.34796674, 0.195538895,
    0.941186497, 0.096231242, 0.052199601, 0.39602816, 0.528266838, 0.889632012, 0.496787047,
    0.477975114, 0.223515068, 0.99239748, 0.238520873, 0.403304902, 0.480692256, 0.857157932,
    0.826910402, 0.402883822, 0.770045039, 0.065022579, 0.965778564, 0.619016461, 0.636245059,
    0.425830078, 0.127058888, 0.78130047, 0.536282209, 0.562794123, 0.786647718, 0.95957355,
    0.525808468, 0.036443611, 0.342172638, 0.195385429, 0.505996584, 0.519339743, 0.320929963,
    0.100733839, 0.02680809, 0.359336021, 0.568524886, 0.119214954, 0.703526507, 0.091533922,
    0.89353786, 0.8558834, 0.48769401, 0.595199, 0.984931459, 0.563345644, 0.757006291, 0.985660599,
    0.332212587, 0.084466618, 0.829207688, 0.383774726, 0.187203386, 0.886550142, 0.282560673,
    0.059813279, 0.30941033, 0.455138968, 0.663298829, 0.042248569, 0.360071773, 0.971448722,
    0.782387076, 0.527674632, 0.048809425, 0.54290203, 0.746277161, 0.349230359, 0.189349564,
    0.196007651, 0.661393135, 0.410818109, 0.311247174, 0.99876876, 0.201527484, 0.475663118,
    0.35252413, 0.222106475, 0.436913154, 0.179884274, 0.122922121, 0.168768146, 0.303009157,
    0.255914242, 0.015384458, 0.860499529, 0.086097967, 0.49787774, 0.184856186, 0.311683272,
    0.487307943, 0.522162996, 0.628071913, 0.367381831, 0.748656371, 0.514588509, 0.395145031,
    0.821414034, 0.611395394, 0.21646972, 0.036386886, 0.005084592, 0.871383258, 0.537365948,
    0.587807813, 0.834481057, 0.637390581, 0.601574531, 0.368261876, 0.4382954, 0.071642525,
    0.911603557, 0.291374051, 0.158971799, 0.775047935, 0.722669948, 0.511212056, 0.71784659,
    0.96975751, 0.500702347, 0.530630151, 0.149660405, 0.203704448, 0.772253031, 0.459534382,
    0.177666452, 0.427183273, 0.402012847, 0.51671091, 0.295476154, 0.91054757, 0.11609004,
    0.380191605, 0.264467757, 0.010712098, 0.418459378, 0.693799752, 0.902391539, 0.316925725,
    0.15503791, 0.354543337, 0.667525083, 0.911835316, 0.253496348, 0.111266545, 0.604833507,
    0.787258962, 0.284156822, 0.868480313, 0.105766516, 0.006683185, 0.676714115, 0.686138679,
    0.893221029, 0.832546829, 0.220967954, 0.371925283, 0.118772237, 0.21679535, 0.4272583,
    0.720207695, 0.855139444, 0.137465494, 0.638373294, 0.912618056, 0.304809557, 0.369295885,
    0.764547524, 0.909828976, 0.777619199, 0.445715283, 0.858631245, 0.156645483, 0.824036767,
    0.252329275, 0.057218912, 0.741157368, 0.589869272, 0.019082046
]
