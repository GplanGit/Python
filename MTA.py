# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/55249/PythonEditorWrapper_c839b61c-ca11-46ca-8fd9-7dd39cdad030')
dataset = pandas.read_csv('input_df_f4eac278-bd00-41b6-89e7-66685c7ab3a1.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Forecast, Milestone, Sample Date)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
# Original Script. Please update your script content here and once completed copy below section back to the original editing window 
import matplotlib.pyplot as plt, datetime
dataset['Sample Date']=pandas.to_datetime(dataset['Sample Date'],dayfirst=True)
dataset['Forecast']=pandas.to_datetime(dataset['Forecast'],dayfirst=True)

pivot=pandas.pivot_table(dataset, aggfunc='first', index='Sample Date', values='Forecast', columns='Milestone')

for column in pivot:
    clean=pivot[[]]
    clean=clean[clean[column].notnull()]
    plt.plot_date(clean['45 Line'],clean[column],xdate=True,ydate=True,ls='-', lw=1)    
plt.xticks(rotation=90)
plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/55249/PythonEditorWrapper_c839b61c-ca11-46ca-8fd9-7dd39cdad030')
