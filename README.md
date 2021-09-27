# ML0921
Trabajo ML The Bridge 2021 " Análisis de datos de pozos petrolíferos: detección automática de litologías partir de registros de pozos".

Este proyecto usa el set de datos del concurso Force 2020 para predecir litologías a partir de registros de pozos usando algoritmos de Machine Learning. 
98 pozos fueron usados para el entrenamiento y testeo mientras que 10 pozos fueron usados para la validación.
Se probaron 3 algoritmos distintos (Random Forest, Gradientboosting, XGBoost) para resolver el problema. Se obtuvo usando el XGBoost, con el set de datos de validación una exactitud de 0.771, un score F1: de 0.799, y un error ponderado: -0.567.

https://xeek.ai/challenges/force-well-logs/overview) The well log data used in this repo is licensed as Norwegian License for Open Government Data (NLOD) 2.0. “Lithofacies data was provided by the FORCE Machine Learning competition with well logs and seismic 2020”.
