Trabajo Archivos

![image](https://github.com/user-attachments/assets/6166c3a2-4fee-4d6d-8438-65cdd4b778dd)

Código:

![image](https://github.com/user-attachments/assets/2bec561b-a8fe-416c-b794-6e6a972b5562)

Explicación:

1. ![image](https://github.com/user-attachments/assets/fa1461b5-390b-4dbe-aae3-b52148c59bfb)

1. Importo la biblioteca csv, que permite leer y escribir archivos en formato csv

2. ![image](https://github.com/user-attachments/assets/9c860ca4-50a1-4792-9969-0daa8bb78b97)

2. Defino la variable archivo_csv con el archivo donde están guardados los datos a investigar. 

3. ![image](https://github.com/user-attachments/assets/30833ec5-dd70-436d-b486-23b8a7212b33)

3. Inicio la variable contador con 0, que me permitirá contar cuántas compras se realizaron 
en el país buscado

4. ![image](https://github.com/user-attachments/assets/dfa0a1a4-34d1-4035-b2fd-81f08af0323c)

4. Abro el archivo en modo lectura con codificación utf-8 para evitar problemas con caracteres
especiales

5. ![image](https://github.com/user-attachments/assets/733dc05f-f5e0-4dd9-9e8e-d2499cd8e9db)

5. La función csv.reader(archivo) crea un objeto que permite leer el contenido línea por línea
como una lista

6. ![image](https://github.com/user-attachments/assets/3f39304a-1924-4277-ae10-1c84c869150d)

6. La función next(lector) lee la primera línea del archivo, en la cual están los nombres de las columnas,
estos datos se almacenan en la variable Encabezados
encabezados.index("Country") busca el índice de la columna "Country" para saber en qué posición 
se encuentra la información del país buscado 

7. ![image](https://github.com/user-attachments/assets/24e5ec1b-77fc-4d34-b668-770a538f163a)

7. Con el ciclo for recorro cada fila del archivo exceptuando los encabezados 
fila[indice_pais] obtiene el nombre del país en la fila nombrada. Si el país coincide 
con la busqueda, se suma 1 al contador

8. ![image](https://github.com/user-attachments/assets/041504ea-05f7-4e9f-8995-6aec91a89f5c)

8. Se muestra la cantidad de compras realizadas en el país que el usuario haya buscado

Ejemplos de salida en terminal:

![image](https://github.com/user-attachments/assets/8dd9c283-2750-4318-9556-cb2dccb89bc9)
![image](https://github.com/user-attachments/assets/54bd703e-9c74-43ae-931b-825ea70f239f)
![image](https://github.com/user-attachments/assets/08f5d48b-e977-47d1-9c47-d1c1a0d7c9c4)
![image](https://github.com/user-attachments/assets/7c665e8c-54c5-4171-be43-c40c32ac9569)
![image](https://github.com/user-attachments/assets/c3ff971b-2e61-4f2b-b8e3-3ab2906f3415)




























