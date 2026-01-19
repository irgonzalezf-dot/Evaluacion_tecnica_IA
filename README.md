Evaluacion_tecnica_IA
# Clasificación de titulares de noticias 
Descripción: El objetivo de la actividad es predecir la categoría de una noticia de acuerdo al headline. Es decir, realizar un modelo de clasificación que tome como entrada un campo de texto
correspondiente al headline de la noticia y que dé como resultado la categoría a la que
pertenece.

Archivo data.json que contiene:
- Headline: texto del titular.
- Category: categoría de la noticia.

## 1. Análisis exploratorio de datos (EDA)
En esta primera etapa se analizó el conjunto de datos que contiene titulares de noticias y su categoría asociada.

Actividades realizadas:
- Normalización de datos desde formato JSON.
- Limpieza de valores nulos.
- Análisis del balance de clases.
- Visualización de las categorías más frecuentes y menos frecuentes. 

Hallazgos relevantes:
- Los datos originales se encontraban en formato JSON no normalizado, por lo que fue necesario reconstruir el DataFrame para obtener una estructura tabular adecuada.
- No se detectaron valores nulos en los campos headline y category, por lo que no fue necesario un proceso de imputación.
- Se observó un desbalance de clases, donde algunas categorías concentran una mayor cantidad de noticias que otras. Este desbalance influye directamente en la evaluación de los modelos y justifica el uso de métricas macro explicadas en la evaluación de los modelos utilizados. 

## 2. Preparación y entrenamiento de modelos 
En esta segunda etapa, transformé los títulares usando TF-IDF (Term Frequency – Inverse Document Frequency) para convertir el texto en características numéricas y entrené dos modelos de clasificación diferentes para comparar enfoques lineales y probabilísticos para la predicción de categorías de noticias. 

- Uso de TF-IDF para convertir todo en minúscula, eliminar palabras sin significado y quitar palabras que aparecen en casi todos los titulares.
- Se dividieron los datos en 80% entrenamiento para que el modelo aprenda, y 20% prueba para evaluar si el modelo aprendió bien. Debido a que el dataset esta desbalanceado, usé "Stratify=y" porque mantiene la proporción de las categorias.

Modelos entrenados
1. Modelo Regresión logística (clasificación lineal)
Este modelo se comportó de forma estable. Las categorías ENTERTAINMENT, FOOD & DRINK, DIVORCE y CRIME tienen un buen recall y un buen f1-score.
Ejemplo con la categoría Entertaiment:
Precision: de las veces que el modelo dijo que esta era la categoría el 0.57 fueron correctas.
Recall: de todas las noticias que si eran esta categoría, el modelo solo detecto 0.77.
f1-score: obtuvó un buen balance entre precision y recall del 0.65.
Support: hay 3473 noticias reales de esta categoría.

2. Modelo Naive Bayes
En este modelo pasó algo muy importante, se imprimió un WARNING "UndefinedMetricWarning", esto significa que el modelo nunca predijo algunas categorías. 
Ejemplo: ARTS & CULTURE, presenta un precision y recall de 0.00.
Esto porque Naive Bayes se basa en probabilidades, favorece las categorías dominantes y es sensible al desbalance que presenta el dataset.

## 3. Evaluación
En la etapa de evaluación, para ambos moodelos de clasificación se agregó la métrica average="magro" para poder tratar todas las categorías por igual y que el análisis no se deje dominar por las clases grandes. 

Para el modelo de Regresión Logística, se hizo la matriz de confusión la cual debido a su gran número de categorías, se volvió densa y dificil de interpretar visualmente. Para esto sería más util si se enfocara únicamente en las clases más frecuentes. 

En base a los resultados obtenidos elegí como modelo final el de Regresión Logística debido a su rendimiento más equilibrado en todas las categorías. A diferencia de Naive Bayes, fue capaz de generar predicciones para las clases con menor número de noticias. Además de que su Acurracy dio como resultado 0.58, es decir que el 58% de los titulares fueron clasificados correctamente y así presentando un todas las métricas de evaluación mejores resultados. 

## 4. API de inferencia
Instrucciones para probar API:
1. Es necesario descargar y guardar la carpeta "news-headline-api" en tu PC. Dentro de la carpeta estan los archivos (app.py, news_modelo.pkl, requirements.txt y tfidf_vectorizer.pkl).
4. En tu PC abre Windows Power Shell presionando Windows + X.
5. Ve a la carpeta "news-headline-api" guardada en tu PC y copia su ruta.
6. Regresa al Winddows Power Shell y escribe "cd + la ruta", + Enter.
(Ejemplo: cd C:\Users\rubyf\Documents\news-headline-api)
7. Una vez rediccionado a la carpeta. Escribe "pip install -r requirements.txt", + Enter para instalar las dependencias. 
4. Una vez instaladas, ahí mismo en PowerShell ejecuta "uvicorn app:app --reload" + Enter.
5. Cuando veas "Application startup complete" sin cerrar la pestaña de PowerShell:
6. Abre tu navegador y entra a "http://127.0.0.1:8000/docs"
6.1. Veras una pantalla interactiva.
6.2. Abre POST/predict
6.3. Click en "Try it out"
6.4. Escribe un ejemplo de título:
   "headline": "Federal Reserve raises interest rates again"
   "headline": "New Exhibition Brings Together Key Works of Contemporary Art"
6.5. Click en Execute
6.6. Mira abajo en la sección que dice "Response body", y veras algo como:
   {
  "headline": "Federal Reserve raises interest rates again",
  "predicted_category": "BUSINESS"
}
Aquí es donde se muestra la categoría que se predice de acuerdo al headline.
8. Para detener la API, entra al PowerShell, y en el comando ejecuta "CTRL + C". 
   
El archivo "news_modelo.pkl", es el modelo entrenado de Regresión Logística que elegí como modelo final para esta evaluación y "tfidf_vectorizer.pkl" es el vectorizador TF-IDF. 
