#1
import matplotlib.pyplot as plt, pandas

df = pandas.read_csv('C:\Datasets\Hurricanes.csv', delimiter=',')
print(df)
plt.bar(df["Year"], df["Hurricanes"])
plt.show()

#2
import matplotlib.pyplot as plt, pandas

df = pandas.read_csv('D:\Datasets\CityTemps.csv', delimiter=',')
plt.hist(df["San Francisco"], df["Moscow"])
plt.show()


#3 m4 assign data is missing in the data files 



#Answer –5.1
#import matplotlib libary
import pandas as pd
import matplotlib.pyplot as plt
#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
#plot data
plt.plot(x, y)
#show plot
plt.show()

#Answer – 5.2

#import matplotlib libary
import matplotlib.pyplot as plt

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#show plot
plt.show()

#Answer – 5.3

#import matplotlib libary
import matplotlib.pyplot as plt

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#show plot
plt.show()


#Answer – 5.4

#import matplotlib libary
import matplotlib.pyplot as plt

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#show plot
plt.show()


#Answer – 5.5

#import matplotlib libary
import matplotlib.pyplot as plt

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#show plot
plt.show()


#Answer – 5.6
#import matplotlib libary
import matplotlib.pyplot as plt

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(4, 5), dpi=100)

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#adjust plot
plt.subplots_adjust(left=0.18)

#show plot
plt.show()


#Answer – 5.7

#import matplotlib libary
import matplotlib.pyplot as plt

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(4, 5), dpi=100)

#define font size
plt.rc("font", size=14)

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#adjust plot
plt.subplots_adjust(left=0.19)

#show plot
plt.show()

#Answer 5.8
import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


#Answer 5.9

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df.head(3))
plt.scatter(df.preTestScore, df.postTestScore, s=df.age)

#Answer 5.10

plt.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)
