# Creating graphics
1. Install packages
```python
pip install pandas
pip install seaborn
pip install matplotlib
```
2. Import libs
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```
3. Load dataset
```python
df = pd.read_csv('dataset.csv')

df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 400 entries, 0 to 399
Data columns (total 7 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   valor_venda_unitario  400 non-null    float64
 1   valor_venda_total     400 non-null    int64  
 2   custo_entrega         400 non-null    int64  
 3   status_entrega        400 non-null    object 
 4   idade_vendedor        400 non-null    int64  
 5   area_urbana           400 non-null    object 
 6   cliente_local         400 non-null    object 
dtypes: float64(1), int64(3), object(3)
memory usage: 22.0+ KB
```

4. Defining style
```python
sns.set(style="darkgrid")
```

5. Plot a histogram graphic
```python
fig, axes = plt.subplots(1, 1, figsize = (10, 4))
fig.suptitle('Distribution of Unit Sales Value')
sns.histplot(df['valor_venda_unitario'], kde = True);
```
<img src="/image/image15.png">

6. Plot a bar graphic
```python
fig, axes = plt.subplots(1, 1, figsize = (10, 4))
fig.suptitle('Distribuition of Urban Area')
sns.countplot(data = df, x = 'area_urbana');
```
<img src="/image/image16.png">

7. Plot a pie graphic
```python
fig, axes = plt.subplots(1, 1, figsize = (10, 4))
fig.suptitle('Distribuition of local client')
df['cliente_local'].value_counts().plot(kind = 'pie', autopct = '%1.1f%%');
```
<img src="/image/image17.png">
