![portada](https://github.com/angelanavarrog/Restaurantes-con-Estrella/blob/master/images/image1.jpg)

## Context

We often hear that Michelin-starred restaurants are not affordable for everyone.


## Objective

Demonstrate a serie of Hypotheses thar relate Michelin restaurant with economic and demographic variables. The analyzed hypotheses are:

- **Hypothesis 1:** "Awarded restaurants are equally distributed per Spanish regions."
- **Hypothesis 2:** "The larger population, the more award-winning restaurants."
- **Hypothesis 3:** "The more award-winning regions have lower unemployment rates."
- **Hypothesis 4:** "Average menu prices are higher in regions with lower unemployment rates regions."
- **Hypothesis 5:** " Highest menu prices are associated to restaurants that counts with a higher number of stars."
- **Hypothesis 6:** "Most Michelin-starred restaurants in Spain have been awarded only one star."
- **Hypothesis 7:** "Most of the restaurant are located in coast provinces." 
- **Hypothesis 8:** "Spanish tourism is concentrated in regions with the most Michelin Star restaurants."


## Procedure

To demonstrate the veracity or not of the hypothesis mentioned, **the procedure followed is**:

1. Create a restaurants database.
2. Extract database from official website.
3. Clean of mentioned database
4. Locate restaurants in Spain
5. Analyze hypothesis.
6. Conclude the veracity of the hypotheses.

## Repositories structure

1. **[Data:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/data)** folder that contains the original databases
2. **[Cleaning:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/Cleaning)** directory containing .ipynb files where each database was cleaned.
3. **[Output:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/output)** folder on which cleaned databases are stored.
4. **[Analysys:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/Analysis)** directory where location and hypotheses analysis are saved.
5. **[Images:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/images)** folder in which the images used as well as the maps and figures generated in our notebooks are stored.
6. **[Src:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/tree/master/src)** directory where files in format .py are stored. Functions define on these files has been used in other notebooks.
7. **[main.py:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/blob/master/main.py)** file used to generate a streamlit app where some previously analyzed information is shown in an interactive way. 
8. **[Hypotheses.pdf:](https://github.com/angelanavarrog/Restaurantes-con-Estrella/blob/master/Hypotheses.pdf)** document defining the assumptions and the conclusion reached in each case.
9. **[README.md](https://github.com/angelanavarrog/Restaurantes-con-Estrella/blob/master/README.md)**
10. **[.gitignore](https://github.com/angelanavarrog/Restaurantes-con-Estrella/blob/master/.gitignore**

## Libraries

- numpy
- pandas
- geopandas
- json
- matplotlib
- seaborn
- bokeh
- folium
- Cartoframes
- shapely


## Data sources

- [Spain Michelin Guide](https://guide.michelin.com/es/es/restaurantes/1-estrella-michelin/2-estrellas-michelin/3-estrellas-michelin)

- [Instituto Nacional de Estadística](https://www.ine.es/): used to obtain demographic and economic information.