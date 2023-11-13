import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar
from scipy.interpolate import UnivariateSpline

#glft-psyNx5JvEF31vQBy16aK

#rdf = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/Cr_rdf.csv')

#rdfint = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/Cr_rdfint.csv')

#adf = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/Cr_adf.csv')

#rmsd = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/Cr_RMSDs.csv')


rdf = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/EDTA-rdf.csv')

rdfint = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/EDTA-rdf-integral.csv')

adf = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/EDTA-adf.csv')

rmsd = pd.read_csv('C:/Users/fouch/OneDrive/Documents/Cours_5A/AFICS-main/AFICS-main/EDTA-RMSDs.csv')


rmsd =rmsd.drop(1)
rmsd =rmsd.drop(0)

for i in range(rmsd.shape[1]):
    rmsd[rmsd.columns[i]]=list(map(float,rmsd[rmsd.columns[i]]))
    



x=np.linspace(0,10,9999)

#rmsd['octahedral']= list(map(float,rmsd['octahedral']))
#rmsd['trigonal-prismatic'] = list(map(float,rmsd['trigonal-prismatic']))



plt.figure(1)
plt.plot(adf['Angle'],adf['Count'])
plt.xlabel('Angle')
plt.ylabel('Count')
plt.title('Nombre de présence de chaque angle')


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(rdf['Distance (A)'], rdf['Count'], 'g-', label='RDF')
ax2.plot(rdf['Distance (A)'], rdfint['Integral'], 'b-', label='Integral')
ax2.set_ylim(0, 12)
ax1.set_ylabel('g(r)')
ax2.set_ylabel('Integration')
fig.legend(loc='center right')


plt.figure(3)
for i in range(rmsd.shape[1]):
    plt.plot(x,rmsd[rmsd.columns[i]],label=str(rmsd.columns[i]))
    
plt.ylim(0, 1.0)
plt.legend(loc='best')



rmsd['Best geometry'] = rmsd[rmsd.columns].idxmin(axis=1)
#rmsd['Best geometry'].iloc[4]='trigo'
count=rmsd['Best geometry'].value_counts()
distrib = pd.Series(index=count.index, dtype=float)



for i in range(len(count)):
    
    distrib[count.index[i]]=float(count[count.index[i]]/len(rmsd['Best geometry']))
    

print(distrib)

#count_octahedral = (rmsd['Best geometry'] == 'octahedral').sum()


#print(type(rmsd.iloc[0,0]))

#print(rmsd[rmsd.columns[0]])



   








