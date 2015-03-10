__author__ = 'bruno'
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy import linspace

SCALE_CONST = 4000
HOW_MANY_STD = 3
_n_bins = 15

filename = r"local_subject101.dat"
print(filename)


def toint(what):
    if isinstance(what,list): return list(map(int,what))
    if isinstance(what,int):  return what
    if isinstance(what,str):  return int(what)


activitydict = {1:[],4:[],5:[]}

with open(filename) as handle:
    c=0

    for one_line in handle.readlines():
        one_line_array = one_line.split(" ")
        type_of_activity = int(one_line_array[1])

        if (type_of_activity in [1,4,5]) and one_line_array[2] != 'NaN':
                activitydict[type_of_activity].append(int(one_line_array[2]))


print(activitydict[1][1:100]);
print(activitydict[4][1:100]);
print(activitydict[5][1:100]);

print(len(activitydict[1]),len(activitydict[4]),len(activitydict[5]))




plt.hist (activitydict[1],label='(1)',bins=_n_bins)
plt.hist (activitydict[4],label='(4)',bins=_n_bins)
plt.hist (activitydict[5],label='(5)',bins=_n_bins)

#fits

fit_1_params,fit_4_params,fit_5_params = norm.fit(activitydict[1]),norm.fit(activitydict[4]),norm.fit(activitydict[5],)
print(fit_1_params,fit_4_params,fit_5_params)




linspace_for_1 = linspace(int(fit_1_params[0]-HOW_MANY_STD*fit_1_params[1]),int(fit_1_params[0]+HOW_MANY_STD*fit_1_params[1]),100)
for_plot_1 = SCALE_CONST*norm.pdf (linspace_for_1,fit_1_params[0],fit_1_params[1])
plt.plot(linspace_for_1,for_plot_1,'r-')

linspace_for_4 = linspace(int(fit_4_params[0]-HOW_MANY_STD*fit_4_params[1]),int(fit_4_params[0]+HOW_MANY_STD*fit_4_params[1]),100)
for_plot_4 = SCALE_CONST*norm.pdf (linspace_for_4,fit_4_params[0],fit_4_params[1])
plt.plot(linspace_for_4,for_plot_4,'r-')

linspace_for_5 = linspace(int(fit_5_params[0]-HOW_MANY_STD*fit_5_params[1]),int(fit_5_params[0]+HOW_MANY_STD*fit_5_params[1]),100)
for_plot_5 = SCALE_CONST*norm.pdf (linspace_for_5,fit_5_params[0],fit_5_params[1])
plt.plot(linspace_for_5,for_plot_5,'r-')



plt.show()



