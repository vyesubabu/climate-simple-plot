

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

# สีต่างๆ ที่น่าสนใจ
ตาม IPCC report
- ด้าน temperature จะเป็นสี น้ำเงิน-แดง
- ด้าน prcp จะเป็นสี น้ำตาล-น้ำเงิน


```python
color_res = 20
palettes = ['RdBu', 'coolwarm_r', 'RdYlBu', 'rainbow_r', 'Spectral', 'BrBG', 'RdYlGn']
```


```python
for palette in palettes:
    print(palette)
    sns.palplot(sns.color_palette(palette, color_res))
    plt.show()
```

    RdBu
    


![png](output_3_1.png)


    coolwarm_r
    


![png](output_3_3.png)


    RdYlBu
    


![png](output_3_5.png)


    rainbow_r
    


![png](output_3_7.png)


    Spectral
    


![png](output_3_9.png)


    BrBG
    


![png](output_3_11.png)


    RdYlGn
    


![png](output_3_13.png)


## สร้าง color map เอง / custom color map


```python
f_color = 'BrBG'
s_color = 'RdBu'
f = sns.color_palette(f_color, color_res).as_hex()
s = sns.color_palette(s_color, color_res).as_hex()
mid = color_res//2 
custom_prcp = f[0:mid] + s[mid:]
len(custom_prcp)
```




    20




```python
offset = 5
ex = 2
custom_rainbow = sns.color_palette('rainbow', color_res+offset).as_hex()[offset-ex:-ex]
len(custom_rainbow)
```




    20




```python
sns.palplot(custom_prcp)
sns.palplot(custom_rainbow)
```


![png](output_7_0.png)



![png](output_7_1.png)


# export ค่าสีออกมาเป็น list RGB


```python
temp_cmap = 'RdYlBu'
temp_color = sns.color_palette('RdYlBu', color_res).as_hex()
sns.palplot(temp_color)
print(temp_color)
```

    ['#bd1726', '#d42d27', '#e34933', '#f16640', '#f7844e', '#fca55d', '#fdbf71', '#fed687', '#fee99d', '#fff7b3', '#f7fcce', '#e9f6e8', '#d6eef5', '#bde2ee', '#a3d3e6', '#87bdd9', '#6ea6ce', '#588cc0', '#4471b2', '#3a54a4']
    


![png](output_9_1.png)



```python
prcp_color = custom_prcp
sns.palplot(prcp_color)
print(prcp_color)
```

    ['#6e4007', '#894f0a', '#a16518', '#b97b29', '#ca9849', '#dbb972', '#e7cf94', '#f1e1b5', '#f6ecd1', '#f5f2e8', '#edf2f5', '#dbeaf2', '#c5dfec', '#a7d0e4', '#87beda', '#5fa5cd', '#3f8ec0', '#2f79b5', '#1f63a8', '#124984']
    


![png](output_10_1.png)



```python
variance_color = custom_rainbow
sns.palplot(variance_color)
print(variance_color)
```

    ['#3176f8', '#1e91f3', '#09a9ee', '#08bee9', '#1dd1e2', '#30e1da', '#44eed2', '#58f8c9', '#6dfdbf', '#80ffb4', '#92fda9', '#a6f89d', '#bbee91', '#cee184', '#e2d176', '#f6be68', '#ffa95b', '#ff914c', '#ff763d', '#ff592d']
    


![png](output_11_1.png)


## Ref
[matplotlib colormap](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)

[seaborn color palette](https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=color)
