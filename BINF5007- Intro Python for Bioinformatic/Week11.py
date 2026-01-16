#Metlab Seaborn
import seaborn as ses
import matplotlib.pyplot as plt

'''
ses.set() 
#loading dataset 'penguins' included in seaborn library
penguins = ses.load_dataset("penguins")

#making scatterplot with seaborn
ses.scatterplot(data=penguins, x="bill_length_mm", y="flipper_length_mm",
                size = "body_mass_g", hue="species", alpha = 0.7) #scatterplot method
plt.show()  #method needed to show plot in seperate window
plt.close() #method needed to ensure plt is cleared before new plt is made

'''
import numpy as np
import pandas as pd
'''
#using panda library and seaborn
data = np.random.multivariate_normal([0,0],[[5,2],[2,2]], size=200)
data = pd.DataFrame(data, columns = ['x','y'])

#making continuous 'kde' plot and histograms
for col in 'xy':
    #ses.kdeplot(data[col], fill=True)
    ses.histplot(data[col], kde=True)
    #plt.hist(data[col],alpha=0.5)

plt.legend("XY", ncol=2, loc='upper left')#modigying figure legend
plt.savefig("example_plot.png") #saves plot figure (default is working directory)#save plots as a png
plt.show()
plt.close()
'''
'''
#using csv/tsv with seaborn
my_types = {
        'Species' : 'string',
        'Kingdom' : 'string',
        'Class'   : 'string',
        'Assembly status' : 'string',
        'Number of genes' : 'Int64',
        'Number of proteins' : 'Int64'
    }
euk = pd.read_csv("eukaryotes.tsv", sep="\t", dtype = my_types, na_values=['-'])
filtered_euk = euk[euk["Size (Mb)"]<4000].dropna()

ses.kdeplot(filtered_euk["GC%"], fill=True)
plt.show()
plt.close()
'''
'''
penguins = ses.load_dataset("penguins")
# Set kind="reg" to add a linear regression fit (using regplot())
# and univariate KDE curves:
ses.jointplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species"
)
plt.legend(["Adele","Chinstrap","Gentoo"], ncol=1, loc='lower right')
plt.savefig("test6.png")
plt.show()
plt.close()
'''
'''
#subplots
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes   = [x**3 for x in x_values]
fig, ax = plt.subplots(1, 2)
ses.scatterplot(x=x_values, y=squares, ax=ax[0])
ax[0].set_title('Squares')
ses.scatterplot(x=x_values, y=cubes, ax=ax[1], color='red')
ax[1].set_title('Cubes')
fig.tight_layout()   # automatically adjusts spacing between subplots
plt.show()
plt.close()
'''
#subplots cont.
x_values = list(range(11))
squares = [x**2  for x in x_values]
cubes   = [x**3  for x in x_values]
fourths = [x**4  for x in x_values]
fifths  = [x**5  for x in x_values]

# number row x columns, and update the size of the figure
# here ax is a two-dimensional list of Axes
fig, ax = plt.subplots(2, 2, figsize=(10, 7))
ses.scatterplot(x=x_values, y=squares, ax=ax[0, 0])
ax[0, 0].set_title('Squares')
 
ses.scatterplot(x=x_values, y=cubes,   ax=ax[0, 1], color='red')
ax[0, 1].set_title('Cubes')
 
ses.scatterplot(x=x_values, y=fourths, ax=ax[1, 0])
ax[1, 0].set_title('Fourths')
 
ses.scatterplot(x=x_values, y=fifths,  ax=ax[1, 1], color='red')
ax[1, 1].set_title('Fifths')
fig.tight_layout()   # automatically adjusts subplot params so they fit
plt.show()
plt.close()