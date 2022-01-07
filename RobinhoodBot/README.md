# StockHood Bot
Trading Bot/Scanner for Robinhood Users


The bot is written in Python and relies on two core libraries for the majority of its functionality: robin-stocks and ta. robin-stocks is a library that interacts with the Robinhood API
and allows one to execute buy and sell orders, get real time ticker information, and more. ta is a technical analysis library that also incorporates the Python Pandas library to generate 
indicators from stock data.

To Install:

```bash
git clone 
cd StockHoodBot/
pip install -r requirements.txt
cp config.py.sample config.py # add auth info after copying
```

To Run:

```python
cd StockHoodBot/stockhoodbot (If outside of root directory)
python3 main.py
```



#x = [0,1,2,3,4]
#y = [0,2,4,6,8]

# Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
#plt.figure(figsize=(8,5), dpi=100)

# Line 1

# Keyword Argument Notation
#plt.plot(x,y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')

# Shorthand notation
# fmt = '[color][marker][line]'
#plt.plot(x,y, 'b^--', label='2x')

## Line 2

# select interval we want to plot points at
#x2 = np.arange(0,4.5,0.5)

# Plot part of the graph as line
#plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

# Plot remainder of graph as a dot
#plt.plot(x2[5:], x2[5:]**2, 'r--')

# Add a title (specify font parameters with fontdict)
#plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

# X and Y labels
#plt.xlabel('X Axis')
#plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
#plt.xticks([0,1,2,3,4,])
#plt.yticks([0,2,4,6,8,10])

# Add a legend
#plt.legend()

# Save figure (dpi 300 is good when saving so graph has high resolution)
#plt.savefig('mygraph.png', dpi=300)

# Show plot
#plt.show()

#df1 = pd.read_csv("pokemon_data.csv")
#print('  --  --  ')
#print(df1.columns)
#print('  --  --  ')
#print(df1[["Name", "Type 1", "HP"]])
#print('  --  --  ')
#print(df1.iloc[1])
#print('  --  --  ')
#for index, row in df1.iterrows():
#    print(index, row["Name"])
#print('  --  --  ')
#df1.loc[df1['Type 1'] == "Grass"]
#print(df1.loc[df1['Type 1'] == "Grass"])
#df1.sort_values(['Type 1', 'HP'])
#print(df1)
#df1['Total'] = df1['HP'] + df1['Attack'] + df1['Defense'] + df1['Sp. Atk'] + df1['Sp. Def'] + df1['Speed']
#print(df1.head(5))
#df1 = df1.drop(columns=['Total'])
#print(df1.head(5))

#df1['Total'] = df1.iloc[:, 4:10].sum(axis=1)
#print(df1.head(10))

#df1.to_csv('modified.csv', index=False)



