import pandas as pd
import pandas as py
import matplotlib.pyplot as plt

# import data
data=pd.read_csv('ProcessedData.csv')

# percentages per each brand posted
per_brand=data['Brand'].value_counts(normalize=True)*100

# if less than 1.5% = others
smallpercent=1.5
minority=per_brand[per_brand < smallpercent]
per_brand['Others']=minority.sum()
per_brand=per_brand[per_brand>= smallpercent]

# pie chart plot
plt.figure(figsize=(10,10))
wedges, texts , autotexts=plt.pie(
    per_brand,
    labels=per_brand.index,
    # percentage x.x%
    autopct='%1.1f%%',
    startangle=90,
    # gap between each wedge
    wedgeprops=dict(width=0.3,edgecolor='w'),
    # colour of text and font size of the text
    textprops=dict(color='black', fontsize=7),
)

plt.title('Distribution of Brands Posted on Sgcarmart')
plt.show()