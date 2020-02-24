---
title: "Data management and exploration in pandas
date: 2020-01-01T23:05:55+02:00
draft: false
---


# Data management and exploration in pandas



This section provides a brief introduction to pandas. The pandas library is a key component for doing data science in Python for a couple of reasons. Most importantly, it provides two data types, series and data frame, that allow you to store and manipulate data in a way that is useful for analysis. Second, it is incredibly useful for importing and exporting data in a wide variety of formats. Finally, it makes descriptive analysis, including both summary statistics and visualizations. This section provides an introduction to the main capabilities of pandas relevant to data analysis.

Most of the things that you will want to do in Python require importing libraries. By convention, pandas is imported as `pd`. Additionally, we enable the ability for pandas graphics to be displayed within the notebook with `%matplotlib inline`.


```python
import pandas as pd

%matplotlib inline
```

## Reading data

In the summer of 2017, the Washington Post produced a [report](https://www.washingtonpost.com/graphics/2018/investigations/unsolved-homicide-database/) on murder clearance rates in U.S. cities. They also released the [data](https://github.com/washingtonpost/data-homicides) they collected on Github as a csv file. We can create a new dataframe, called `df`, using the [pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) `read_csv` method.  


```python
df = pd.read_csv('data/homicide.csv')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uid</th>
      <th>reported_date</th>
      <th>victim_last</th>
      <th>victim_first</th>
      <th>victim_race</th>
      <th>victim_age</th>
      <th>victim_sex</th>
      <th>city</th>
      <th>state</th>
      <th>lat</th>
      <th>lon</th>
      <th>disposition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alb-000001</td>
      <td>20100504</td>
      <td>GARCIA</td>
      <td>JUAN</td>
      <td>Hispanic</td>
      <td>78.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.095788</td>
      <td>-106.538555</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alb-000002</td>
      <td>20100216</td>
      <td>MONTOYA</td>
      <td>CAMERON</td>
      <td>Hispanic</td>
      <td>17.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.056810</td>
      <td>-106.715321</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alb-000003</td>
      <td>20100601</td>
      <td>SATTERFIELD</td>
      <td>VIVIANA</td>
      <td>White</td>
      <td>15.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.086092</td>
      <td>-106.695568</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alb-000004</td>
      <td>20100101</td>
      <td>MENDIOLA</td>
      <td>CARLOS</td>
      <td>Hispanic</td>
      <td>32.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.078493</td>
      <td>-106.556094</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alb-000005</td>
      <td>20100102</td>
      <td>MULA</td>
      <td>VIVIAN</td>
      <td>White</td>
      <td>72.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.130357</td>
      <td>-106.580986</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Alb-000006</td>
      <td>20100126</td>
      <td>BOOK</td>
      <td>GERALDINE</td>
      <td>White</td>
      <td>91.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.151110</td>
      <td>-106.537797</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alb-000007</td>
      <td>20100127</td>
      <td>MALDONADO</td>
      <td>DAVID</td>
      <td>Hispanic</td>
      <td>52.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.111785</td>
      <td>-106.712614</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alb-000008</td>
      <td>20100127</td>
      <td>MALDONADO</td>
      <td>CONNIE</td>
      <td>Hispanic</td>
      <td>52.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.111785</td>
      <td>-106.712614</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Alb-000009</td>
      <td>20100130</td>
      <td>MARTIN-LEYVA</td>
      <td>GUSTAVO</td>
      <td>White</td>
      <td>56.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.075380</td>
      <td>-106.553458</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Alb-000010</td>
      <td>20100210</td>
      <td>HERRERA</td>
      <td>ISRAEL</td>
      <td>Hispanic</td>
      <td>43.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.065930</td>
      <td>-106.572288</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Alb-000011</td>
      <td>20100212</td>
      <td>BARRIUS-CAMPANIONI</td>
      <td>HECTOR</td>
      <td>Hispanic</td>
      <td>20.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.077375</td>
      <td>-106.560569</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Alb-000012</td>
      <td>20100218</td>
      <td>LUJAN</td>
      <td>KEVIN</td>
      <td>White</td>
      <td>NaN</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.077011</td>
      <td>-106.564910</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Alb-000013</td>
      <td>20100222</td>
      <td>COLLAMORE</td>
      <td>JOHN</td>
      <td>Hispanic</td>
      <td>46.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.064076</td>
      <td>-106.608281</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Alb-000014</td>
      <td>20100306</td>
      <td>CHIQUITO</td>
      <td>CORIN</td>
      <td>Other</td>
      <td>16.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.041491</td>
      <td>-106.742147</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Alb-000015</td>
      <td>20100308</td>
      <td>TORRES</td>
      <td>HECTOR</td>
      <td>Hispanic</td>
      <td>54.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.070656</td>
      <td>-106.615845</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Alb-000016</td>
      <td>20100308</td>
      <td>GRAY</td>
      <td>STEFANIA</td>
      <td>White</td>
      <td>43.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.070656</td>
      <td>-106.615845</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Alb-000017</td>
      <td>20100322</td>
      <td>LEYVA</td>
      <td>JOEL</td>
      <td>Hispanic</td>
      <td>52.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.079082</td>
      <td>-106.495949</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Alb-000018</td>
      <td>20100323</td>
      <td>DAVID</td>
      <td>LARRY</td>
      <td>White</td>
      <td>52.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Alb-000019</td>
      <td>20100402</td>
      <td>BRITO</td>
      <td>ELIZABETH</td>
      <td>White</td>
      <td>22.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.110404</td>
      <td>-106.523668</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Alb-000020</td>
      <td>20100420</td>
      <td>CHAVEZ</td>
      <td>GREG SR.</td>
      <td>Hispanic</td>
      <td>49.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.089573</td>
      <td>-106.570078</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Alb-000021</td>
      <td>20100423</td>
      <td>KING</td>
      <td>TEVION</td>
      <td>Black</td>
      <td>15.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.095887</td>
      <td>-106.638081</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Alb-000022</td>
      <td>20100423</td>
      <td>BOYKIN</td>
      <td>CEDRIC</td>
      <td>Black</td>
      <td>25.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.095887</td>
      <td>-106.638081</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Alb-000023</td>
      <td>20100518</td>
      <td>BARRAGAN</td>
      <td>MIGUEL</td>
      <td>White</td>
      <td>20.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.083401</td>
      <td>-106.632941</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Alb-000024</td>
      <td>20100602</td>
      <td>FORD</td>
      <td>LUTHER</td>
      <td>Other</td>
      <td>47.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.102423</td>
      <td>-106.567674</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Alb-000025</td>
      <td>20100602</td>
      <td>WRONSKI</td>
      <td>VIOLA</td>
      <td>White</td>
      <td>88.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.095956</td>
      <td>-106.561135</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Alb-000026</td>
      <td>20100603</td>
      <td>ASHFORD</td>
      <td>GUADALUPE</td>
      <td>Hispanic</td>
      <td>27.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.078462</td>
      <td>-106.551755</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Alb-000027</td>
      <td>20100712</td>
      <td>TURNER</td>
      <td>MICHELLE</td>
      <td>White</td>
      <td>36.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.053748</td>
      <td>-106.531800</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Alb-000028</td>
      <td>20100712</td>
      <td>CUNNINGHAM</td>
      <td>SHARON</td>
      <td>White</td>
      <td>47.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.053748</td>
      <td>-106.531800</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Alb-000029</td>
      <td>20100726</td>
      <td>NGUYEN</td>
      <td>SELENAVI</td>
      <td>Asian</td>
      <td>1.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.064456</td>
      <td>-106.524458</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Alb-000030</td>
      <td>20100728</td>
      <td>VALDEZ</td>
      <td>BILL</td>
      <td>Hispanic</td>
      <td>58.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.061827</td>
      <td>-106.749104</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>52149</th>
      <td>Was-001353</td>
      <td>20160324</td>
      <td>TURNER</td>
      <td>GABRIEL</td>
      <td>Black</td>
      <td>46.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.857628</td>
      <td>-76.996482</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52150</th>
      <td>Was-001355</td>
      <td>20160518</td>
      <td>MERIEDY</td>
      <td>THOMAS</td>
      <td>Black</td>
      <td>24.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.862517</td>
      <td>-76.990880</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52151</th>
      <td>Was-001356</td>
      <td>20160906</td>
      <td>COOK</td>
      <td>JOE</td>
      <td>Black</td>
      <td>35.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.854721</td>
      <td>-76.990795</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52152</th>
      <td>Was-001357</td>
      <td>20160917</td>
      <td>PHILLIPS</td>
      <td>SCORPIO</td>
      <td>Black</td>
      <td>31.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.877003</td>
      <td>-76.995627</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52153</th>
      <td>Was-001358</td>
      <td>20160917</td>
      <td>HARRIS</td>
      <td>ZORUAN</td>
      <td>Black</td>
      <td>18.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.877003</td>
      <td>-76.995627</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52154</th>
      <td>Was-001359</td>
      <td>20161108</td>
      <td>PRATT</td>
      <td>ANTINA</td>
      <td>Black</td>
      <td>40.0</td>
      <td>Female</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.855699</td>
      <td>-76.993248</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52155</th>
      <td>Was-001360</td>
      <td>20161127</td>
      <td>SILVER</td>
      <td>ORLANDO</td>
      <td>Black</td>
      <td>37.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.860054</td>
      <td>-76.991825</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52156</th>
      <td>Was-001361</td>
      <td>20160304</td>
      <td>REZENE</td>
      <td>NOEL</td>
      <td>Black</td>
      <td>26.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.849150</td>
      <td>-76.971272</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52157</th>
      <td>Was-001362</td>
      <td>20160511</td>
      <td>DRAYTON</td>
      <td>JAVION</td>
      <td>Black</td>
      <td>3.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.853961</td>
      <td>-76.984712</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>52158</th>
      <td>Was-001363</td>
      <td>20160702</td>
      <td>MCCULLOUGH</td>
      <td>ANTOINE</td>
      <td>Black</td>
      <td>30.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.843740</td>
      <td>-76.977839</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52159</th>
      <td>Was-001365</td>
      <td>20161111</td>
      <td>BUIE</td>
      <td>SAMUELLE</td>
      <td>Black</td>
      <td>25.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.851284</td>
      <td>-76.981029</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52160</th>
      <td>Was-001366</td>
      <td>20161111</td>
      <td>JENNINGS</td>
      <td>RASSAAN</td>
      <td>Black</td>
      <td>19.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.851284</td>
      <td>-76.981029</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52161</th>
      <td>Was-001367</td>
      <td>20161122</td>
      <td>TYLER</td>
      <td>MARQUETT</td>
      <td>Black</td>
      <td>26.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.849967</td>
      <td>-76.974421</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52162</th>
      <td>Was-001368</td>
      <td>20160302</td>
      <td>GARRIS</td>
      <td>RUDOLPH</td>
      <td>Black</td>
      <td>25.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.827191</td>
      <td>-76.998183</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52163</th>
      <td>Was-001369</td>
      <td>20160317</td>
      <td>DANSBURY</td>
      <td>AUBREY</td>
      <td>Black</td>
      <td>27.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.829442</td>
      <td>-76.993175</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52164</th>
      <td>Was-001370</td>
      <td>20160510</td>
      <td>HANEY</td>
      <td>JAQUAN</td>
      <td>Black</td>
      <td>22.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.833943</td>
      <td>-76.990742</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52165</th>
      <td>Was-001371</td>
      <td>20160519</td>
      <td>HAMILTON</td>
      <td>DANA</td>
      <td>Black</td>
      <td>44.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.828365</td>
      <td>-76.994431</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52166</th>
      <td>Was-001372</td>
      <td>20160609</td>
      <td>WRIGHT</td>
      <td>RASHAWN</td>
      <td>Black</td>
      <td>25.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.835947</td>
      <td>-76.990438</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52167</th>
      <td>Was-001373</td>
      <td>20160626</td>
      <td>BLACKWELL</td>
      <td>WESTLEY</td>
      <td>Black</td>
      <td>38.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.834756</td>
      <td>-76.992662</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52168</th>
      <td>Was-001374</td>
      <td>20161227</td>
      <td>DOWTIN</td>
      <td>HERBERT</td>
      <td>Black</td>
      <td>22.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.833190</td>
      <td>-76.994345</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52169</th>
      <td>Was-001375</td>
      <td>20160224</td>
      <td>MEDLAY</td>
      <td>DEMETRIUS</td>
      <td>Black</td>
      <td>22.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.843399</td>
      <td>-77.000104</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52170</th>
      <td>Was-001376</td>
      <td>20160731</td>
      <td>STEPHENS</td>
      <td>JUDONNE</td>
      <td>Black</td>
      <td>25.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.863322</td>
      <td>-76.995309</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52171</th>
      <td>Was-001377</td>
      <td>20160916</td>
      <td>PEOPLES</td>
      <td>DARNELL</td>
      <td>Black</td>
      <td>35.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.845871</td>
      <td>-76.998169</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52172</th>
      <td>Was-001378</td>
      <td>20160415</td>
      <td>IVEY</td>
      <td>PAUL</td>
      <td>Black</td>
      <td>37.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.826458</td>
      <td>-77.003590</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52173</th>
      <td>Was-001379</td>
      <td>20160715</td>
      <td>HARRIS</td>
      <td>SHAROD</td>
      <td>Black</td>
      <td>20.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.827266</td>
      <td>-77.001572</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52174</th>
      <td>Was-001380</td>
      <td>20160908</td>
      <td>WILLIAMS</td>
      <td>EVAN</td>
      <td>Black</td>
      <td>29.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.828704</td>
      <td>-77.002075</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>52175</th>
      <td>Was-001381</td>
      <td>20160913</td>
      <td>SMITH</td>
      <td>DEON</td>
      <td>Black</td>
      <td>19.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.822852</td>
      <td>-77.001725</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52176</th>
      <td>Was-001382</td>
      <td>20161114</td>
      <td>WASHINGTON</td>
      <td>WILLIE</td>
      <td>Black</td>
      <td>23.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.828025</td>
      <td>-77.002511</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52177</th>
      <td>Was-001383</td>
      <td>20161130</td>
      <td>BARNES</td>
      <td>MARCUS</td>
      <td>Black</td>
      <td>24.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.820476</td>
      <td>-77.008640</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52178</th>
      <td>Was-001384</td>
      <td>20160901</td>
      <td>JACKSON</td>
      <td>KEVIN</td>
      <td>Black</td>
      <td>17.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.866689</td>
      <td>-76.982409</td>
      <td>Closed by arrest</td>
    </tr>
  </tbody>
</table>
<p>52179 rows × 12 columns</p>
</div>



If you have the URL of a csv file, you can load it directly:


```python
csv_url = 'https://raw.githubusercontent.com/nealcaren/data/master/sets/homicide.csv'

df = pd.read_csv(csv_url)
```

#### Learning about your dataframe

After loading a dataframe, best practice is to get a sense of the data with the `head`, `info` and `describe` methods. `head` shows the first five rows of the dataframe.


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uid</th>
      <th>reported_date</th>
      <th>victim_last</th>
      <th>victim_first</th>
      <th>victim_race</th>
      <th>victim_age</th>
      <th>victim_sex</th>
      <th>city</th>
      <th>state</th>
      <th>lat</th>
      <th>lon</th>
      <th>disposition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alb-000001</td>
      <td>20100504</td>
      <td>GARCIA</td>
      <td>JUAN</td>
      <td>Hispanic</td>
      <td>78.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.095788</td>
      <td>-106.538555</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alb-000002</td>
      <td>20100216</td>
      <td>MONTOYA</td>
      <td>CAMERON</td>
      <td>Hispanic</td>
      <td>17.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.056810</td>
      <td>-106.715321</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alb-000003</td>
      <td>20100601</td>
      <td>SATTERFIELD</td>
      <td>VIVIANA</td>
      <td>White</td>
      <td>15.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.086092</td>
      <td>-106.695568</td>
      <td>Closed without arrest</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alb-000004</td>
      <td>20100101</td>
      <td>MENDIOLA</td>
      <td>CARLOS</td>
      <td>Hispanic</td>
      <td>32.0</td>
      <td>Male</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.078493</td>
      <td>-106.556094</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alb-000005</td>
      <td>20100102</td>
      <td>MULA</td>
      <td>VIVIAN</td>
      <td>White</td>
      <td>72.0</td>
      <td>Female</td>
      <td>Albuquerque</td>
      <td>NM</td>
      <td>35.130357</td>
      <td>-106.580986</td>
      <td>Closed without arrest</td>
    </tr>
  </tbody>
</table>
</div>



In addition to the data in the csv file, an index has been created to identifiy each row. By default, this is an interger starting with 0.

If the dataset is wide, middle columns will not be displayed. Also, if text fields are long, only the first few characters will be shown. These can both be adjusted using pandas [display settings](https://pandas.pydata.org/pandas-docs/stable/options.html).

`info` can be used to explore the data types and the number of non-missing cases for each variable.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 52179 entries, 0 to 52178
    Data columns (total 12 columns):
    uid              52179 non-null object
    reported_date    52179 non-null int64
    victim_last      52179 non-null object
    victim_first     52179 non-null object
    victim_race      52179 non-null object
    victim_age       49180 non-null float64
    victim_sex       52179 non-null object
    city             52179 non-null object
    state            52179 non-null object
    lat              52119 non-null float64
    lon              52119 non-null float64
    disposition      52179 non-null object
    dtypes: float64(3), int64(1), object(8)
    memory usage: 4.8+ MB


`describe` provides summary statistics for all the numeric variables.


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reported_date</th>
      <th>victim_age</th>
      <th>lat</th>
      <th>lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.217900e+04</td>
      <td>49180.000000</td>
      <td>52119.000000</td>
      <td>52119.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.013090e+07</td>
      <td>31.801220</td>
      <td>37.026786</td>
      <td>-91.471094</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.123420e+06</td>
      <td>14.418692</td>
      <td>4.348647</td>
      <td>13.746378</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.007010e+07</td>
      <td>0.000000</td>
      <td>25.725214</td>
      <td>-122.507779</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2.010032e+07</td>
      <td>22.000000</td>
      <td>33.765203</td>
      <td>-95.997198</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.012122e+07</td>
      <td>28.000000</td>
      <td>38.524973</td>
      <td>-87.710286</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.015091e+07</td>
      <td>40.000000</td>
      <td>40.027627</td>
      <td>-81.755909</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.015111e+08</td>
      <td>102.000000</td>
      <td>45.051190</td>
      <td>-71.011519</td>
    </tr>
  </tbody>
</table>
</div>



The column headers can be extracted using `keys`.


```python
df.keys()
```




    Index(['uid', 'reported_date', 'victim_last', 'victim_first', 'victim_race',
           'victim_age', 'victim_sex', 'city', 'state', 'lat', 'lon',
           'disposition'],
          dtype='object')



If you wanted to look at the bottom of the dataframe, you can use `tail`. Both `head` and `tail` allow you to change the number of rows displayed from the default five.


```python
df.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uid</th>
      <th>reported_date</th>
      <th>victim_last</th>
      <th>victim_first</th>
      <th>victim_race</th>
      <th>victim_age</th>
      <th>victim_sex</th>
      <th>city</th>
      <th>state</th>
      <th>lat</th>
      <th>lon</th>
      <th>disposition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52176</th>
      <td>Was-001382</td>
      <td>20161114</td>
      <td>WASHINGTON</td>
      <td>WILLIE</td>
      <td>Black</td>
      <td>23.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.828025</td>
      <td>-77.002511</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52177</th>
      <td>Was-001383</td>
      <td>20161130</td>
      <td>BARNES</td>
      <td>MARCUS</td>
      <td>Black</td>
      <td>24.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.820476</td>
      <td>-77.008640</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>52178</th>
      <td>Was-001384</td>
      <td>20160901</td>
      <td>JACKSON</td>
      <td>KEVIN</td>
      <td>Black</td>
      <td>17.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.866689</td>
      <td>-76.982409</td>
      <td>Closed by arrest</td>
    </tr>
  </tbody>
</table>
</div>



`sample` displays random rows from the dataframe.


```python
df.sample(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uid</th>
      <th>reported_date</th>
      <th>victim_last</th>
      <th>victim_first</th>
      <th>victim_race</th>
      <th>victim_age</th>
      <th>victim_sex</th>
      <th>city</th>
      <th>state</th>
      <th>lat</th>
      <th>lon</th>
      <th>disposition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>28043</th>
      <td>Las-001175</td>
      <td>20170121</td>
      <td>SANCHEZ</td>
      <td>ALBERTO</td>
      <td>Hispanic</td>
      <td>24.0</td>
      <td>Male</td>
      <td>Las Vegas</td>
      <td>NV</td>
      <td>36.189362</td>
      <td>-115.061763</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>13424</th>
      <td>Cin-700043</td>
      <td>20170728</td>
      <td>ROBERTSON</td>
      <td>RICKEY</td>
      <td>Black</td>
      <td>58.0</td>
      <td>Male</td>
      <td>Cincinnati</td>
      <td>OH</td>
      <td>39.140126</td>
      <td>-84.476951</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>13253</th>
      <td>Cin-000947</td>
      <td>20140531</td>
      <td>GASSETT</td>
      <td>JOSHUA</td>
      <td>Black</td>
      <td>24.0</td>
      <td>Male</td>
      <td>Cincinnati</td>
      <td>OH</td>
      <td>39.162160</td>
      <td>-84.382659</td>
      <td>Closed by arrest</td>
    </tr>
    <tr>
      <th>51164</th>
      <td>Was-000343</td>
      <td>20130907</td>
      <td>SWEET</td>
      <td>KENNETH</td>
      <td>Black</td>
      <td>30.0</td>
      <td>Male</td>
      <td>Washington</td>
      <td>DC</td>
      <td>38.877011</td>
      <td>-77.002498</td>
      <td>Open/No arrest</td>
    </tr>
    <tr>
      <th>16190</th>
      <td>Den-000087</td>
      <td>20120318</td>
      <td>NEWSON</td>
      <td>BILLY</td>
      <td>Black</td>
      <td>29.0</td>
      <td>Male</td>
      <td>Denver</td>
      <td>CO</td>
      <td>39.740021</td>
      <td>-104.979913</td>
      <td>Closed by arrest</td>
    </tr>
  </tbody>
</table>
</div>



<div class="alert alert-info">
<h3> Your turn</h3>
<p> Display the first four rows of the dataframe <code>df</code>.  
</div>


```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
df.head(4)
</code>
</details>

### Working with variables



```python
df.head(2)
```


```python
df['victim_age'].describe()
```


```python
df['victim_age'].value_counts()
```

As this has many values, pandas only displays the top and bottom 30 cases. The `values` method can be used to produce an array containing all the values in order.

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Explore the <code>disposition</code> and <code>victim race</code>   columns in the dataframe.  
</div>


```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
df['disposition'].value_counts()
df['victim_race'].value_counts()
df[['disposition','victim_race']].describe()
</code>
</details>

All of the values of a specific variables can be extracted.


```python
ages = df['victim_age'].values
len(ages)
```


```python
first_age = ages[0]
print(first_age)
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Display seven value from the middle of our age variable.

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
ages[1201:1208]
</code>
</details>

<div class="alert alert-info">
<h3> Your turn</h3>
<p> A well-known data set is the list of titanic passengers. A version can be found in the data folder called, "titanic.csv". Open the file as a new dataframe <code>titanic_df</code>. How many cases? How many columns? What can you find out about the data?

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
titanic_df = pd.read_csv('data/titanic.csv')
titanic_df.describe()
titanic_df.info()
titanic_df.sample(5)
</code>
</details>

#### Plots (optional)

pandas also has plotting capabilies, such as histograms (`hist`) and a correlation matrix (`scatter_matrix`).  


```python
%matplotlib inline
```


```python
df['victim_age'].hist()
```

Plot of individual variables, or series in pandas terminology, are attributes of the data type. That is, you start wit the thing you want plotted, in this case `df['victim_age']`, and append what you want to do, such as `.hist()`.

A second type of plots, such as scatter plots, are methods of the dataframe.


```python
df.plot.scatter(x='lon', y='lat')
```

You could look at the other dataframe plotting methods on the helpful [pandas visualizations page](https://pandas.pydata.org/pandas-docs/stable/visualization.html). Alternatively, typing tab after `df.plot.` also reveals your options.

<img src="images/auto.png"  width="150px" align="left" /><p>






Want to know about `hexbin`? Again, the help page on the web is useful, but appending a question mark to the end of the command will bring up the documentation.


```df.plot.hexbin?```

<img src="images/docstring.png" width = "80%" align="left"/>

A third group of plots are part of the pandas plotting library. In these cases, the thing you want plotted is the first, or only, parameter passed, as is the case with the correlation matrix.


```python
pd.plotting.scatter_matrix(df)
```

Finally, you can also create subplots using the `by` option. Note that `by` accepts a series, or dataframe column, rather than a column name.


```python
df['victim_age'].hist(by = df['victim_sex'],
                      bins = 20)
```

By default, `by` produces separate x and y scales for each subgraph. This is why it appears to be a relatively large number of deaths of very young females. The numbers between men and women at this age are comparable, but the very large number of male deaths in their 20s results in very different xscales for the graphs. This option can be changed with the `sharex` or `sharey` option.


```python
df['victim_age'].hist(by = df['victim_sex'],
                      bins   = 20,
                      sharex = True,
                      sharey = True)
```

#### Other descriptives

Pandas also has a method for producing crosstabs.


```python
pd.crosstab(df['victim_race'], df['disposition'])
```

Note that since this is a pandas method, and not one of a specific dataframe, you need to be explicit about which datatframe each variable is coming from. That is why the first parameter is not `'victim_race'` but `df['victim_race']`.

`normalize` can be used to display percentages instead of frequencies. A value of `index` normalized by row, `columns` by column, and `all` by all values.


```python
pd.crosstab(df['victim_race'],
            df['disposition'],
            normalize='index')
```

Since this returns a dataframe, it can be saved or plotted.


```python
cross_tab = pd.crosstab(df['victim_race'],
                        df['disposition'],
                        normalize='index')

cross_tab
```


```python
cross_tab.to_csv('data/crosstab.csv')
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> In your titanic dataframe, run a crosstab between sex and survived. Anything interesting?

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
pd.crosstab(titanic_df['Survived'],
            titanic_df['Sex'], normalize='index')
</code>
</details>

In order to highlight a meaningful characteristics of the data, you can sort before plotting.


```python
cross_tab.sort_values(by='Closed by arrest')
```


```python
cross_tab.sort_values(by='Closed by arrest').plot(kind   = 'barh',
                                                  title  = 'Disposition by race')
```

#### Subsets

Similar to a list, a dataframe or series can be sliced to subset the data being shown. For example, `df[:2]` will return the first two rows of the dataframe. (This is identical to `df.head(2)`.)


```python
df[:2]
```


```python
df.head(2)
```

This also works for specific columns.


```python
df['reported_date'][:3]
```

#### Dates (optional)

A new variable can be created from `reported_date` that pandas understands is a date variable using the `to_datetime` method. The format is `%Y%m%d` because the original date is in the "YYYMMDD" format, and `coerce` places missing values where the data can be translated, rather than stopping the variable creation completely.


```python
df['reported_date'].head()
```


```python
df['date'] = pd.to_datetime(df['reported_date'],
                            format='%Y%m%d',
                            errors='coerce')
```


```python
df['date'][:3]
```

From the new series, we can extract specific elements, such as the year.


```python
df['year'] = df['date'].dt.year
```

As before, `value_counts` and plots can give some sense of the distribution of the values.


```python
df['year'].value_counts()
```

Value counts returns a pandas series with an index equal to the original values, in the case the year, and the series values based on the frequency. Since years have an order, it makes sense to sort by the index before plotting them.


```python
df['year'].value_counts().sort_index(ascending = False).plot(kind='barh')
```

`crosstab` can also group based on more than one variable for the x or y axis. In that case, you pass a list rather than a single variable or series. To make this clearer, you can create the lists before creating the crosstab.


```python
y_vars = [df['state'], df['city']]
x_vars = df['year']

pd.crosstab(y_vars, x_vars)
```

Crosstab returns a dataframe with the column and index names from the values in the original dataset. Since a list was passed, the datatframe has a `MultiIndex`. The can be useful for cases where you have nested data, like cities with states or annual data on multiple countries.


```python
pd.crosstab(y_vars, x_vars).index.names
```

### Index


```python
df.head()
```

By default, the index is a series that starts with 0. If your data has unique identifiers, however, it is helpful to use that as the index, especially if you intend on merging your data with other data sources. In this dataframe, each row has a unique value for `uid`.


```python
df.set_index('uid', inplace=True)
```


```python
df[:5]
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> In your Titanic dataframe, set the index to the <code>PassengerId</code> column. Confirm that it did want you wanted it to do.

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
titanic_df.set_index('PassengerId', inplace=True)
titanic_df.sample(3)
</code>
</details>

#### Subseting

You can view a subset of a dataframe based on the value of a column.

Let's say that you wanted to look at the cases where the victim's first name was "Juan". You could create a new series which is either `True` or `False` for each case.


```python
df['victim_first'] == 'JUAN'
```

You could store this new true/false series. If you placed this in brackets after the name of the dataframe, pandas would display only the rows with a True value.


```python
is_juan = df['victim_first'] == 'JUAN'
df[is_juan]
```

More commonly, the two statements are combined.


```python
df[df['victim_first'] == 'JUAN']
```

With this method of subsetting, pandas doesn't return a new dataframe, but rather is just hiding some of the rows. So if you want to create a new dataframe based on this subset, you need to append `copy()` to the end.


```python
new_df = df[df['victim_first'] == 'JUAN'].copy()
```


```python
new_df.head()
```

As this selection method returns a dataframe, it can be stored. The following creates two dataframes, one with just the 2016 and one with just the 2017 cases.


```python
df_2017 = df[df['year'] == 2017].copy()
df_2016 = df[df['year'] == 2016].copy()


df_2017['year'].value_counts()
```


```python
df_2016['year'].value_counts()
```

`value_counts` confirms that the correct cases were grabbed.

Alternatively you may want to limit your dataset by column. In this case, you create a list of the columns you want. This list is also placed in brackets after the dataframe name.

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Create a new dataframe with just the female passengers. Check your work.

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
mask = titanic_df['Sex'] == 'female'
titanic_df_f = titanic_df[mask]
titanic_df_f['Sex'].value_counts()
</code>
</details>

#### More subsets


```python
columns_to_keep = ['victim_last', 'victim_first', 'victim_race', 'victim_age', 'victim_sex']
```


```python
df[columns_to_keep]
```

As before, you can you use `copy` to create a new dataset.


```python
victim_df = df[columns_to_keep].copy()
```


```python
victim_df.head()
```

As with the row selection, you don't need to store the column names in a list first. By convention, these two steps are combined. However, combining the steps does create an awkward pair of double brackets.


```python
place_df = df[['city', 'state', 'lat', 'lon']].copy()
```


```python
place_df.head()
```

#### Merging

There are several different ways to combine datasets. The most straightforward is to merge two different datasets who share a key in common. To merge `place_df` with  `victim_df`, for example, you can use the datframe `merge` method.


```python
merged_df = place_df.merge(victim_df, left_index=True, right_index=True)

merged_df.head()
```

### Stacking dataframes

If you have multiple dataframes which each row represents the same kind of object, such as passengers on a ship or murder victims, you can stact them using `pd.concat`. Stacking is most effective when column names overlap between the datasets. Below, I create a new dataframe by stacking together victims from 2016 and 2017.


```python
df_2016 = df[df['year'] == 2016]
len(df_2016)
```


```python
recent_df = pd.concat([df_2017, df_2016])
```


```python
len(recent_df)
```

### New features

New columns in a dataframe can be created in the same manner that new objects are created in Python.


```python
df['birth_year'] = df['year'] - df['victim_age']
```


```python
df['birth_year'].describe()
```


```python
df['minor'] = df['victim_age'] <= 18
```


```python
df['minor'][:10]
```


```python
df['minor'].mean()
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Create a new variable in your Titanic dataframe which marks the people who paid a fare in the top 25% of all fares paid.

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
titanic_df['Fare'].describe()
threshold = 7.9104

titanic_df['Top_25_Fare'] = titanic_df['Fare'] > threshold
titanic_df['Top_25_Fare'].value_counts()</code>
</details>



### Back to some pandas string manipulation fun.

As discussed in the first notebook, Python programming involves creating functions, such as one to do a simple string manipulation.


```python
def title_case(text):
    return text.title()
```


```python
title_case('JUAN')
```

### The apply magic

You can `apply` a function to a dataframe column in order to transfrom each value. The results can also be stored as a new feature.


```python
df['victim_first'].apply(title_case)
```


```python
df['victim_first2'] = df['victim_first'].apply(title_case)
```


```python
df['victim_first2'].sample(4)
```


```python
df[['victim_first', 'victim_first2']].sample(5)
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Write a function that extracts the last name from the name field on your Titanic dataframe.
Create a new variable called <code>Family_Name</code> to store the results. What is the most common family name?

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
def make_name(name):
    family_name = name.split(', ')[0]
    return family_name

titanic_df['Family_Name'] = titanic_df['Name'].apply(make_name)
titanic_df['Family_Name'].sample(3)
</code>
</details>



### Working on more than one column (optional)

If you want a function to work with more than one column, you apply the function to the dataframe. The function will evaluate each row, so you have to specify in the function which columns you want to use.


```python
def victim_name(row):
    first_name = row['victim_first']
    last_name  = row['victim_last']
    name       = last_name + ', ' + first_name
    name       = title_case(name)
    return name
```


```python
df.apply(victim_name, axis=1)
```

Note that we include `axis=1` because we want the function to be applied to each row. The default is to apply the function to each column.


```python
df['victim_name'] = df.apply(victim_name, axis=1)
```


```python
cols_2_show = ['victim_first', 'victim_last', 'victim_name']

df[cols_2_show].sample(5)
```

<div class="alert alert-info">
<h3> Your turn</h3>
<p> Write a function that tags all titanic passgers who are under 18 and who are traveling without parents (<code>parch == 0</code>)? Use the function to create a new variable.

</div>



```python

```

<details>
<summary>Sample answer code</summary>
<code style="background-color: white">
def unac_minor(row):
    minor      = row['Age'] < 18
    no_parents = row['Parch'] == 0
    if minor == True and no_parents == True:
        return True
    return False
titanic_df['Unaccomp_Minor'] = titanic_df.apply(unac_minor, axis=1)
titanic_df['Unaccomp_Minor'].value_counts()
</code>
</details>



Congratulations! You've now been introduced to the basics of data management in pandas for social scientists.
