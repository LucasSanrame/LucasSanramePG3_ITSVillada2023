En este trabajo se utilizo la API de "Rick & Morty" (https://rickandmortyapi.com/), el trabajo consistia en crear una tabla ordenando los datos que la API proporcionaba.

En este codigo se utilizaron (sobre todo) los archivos "views", "urls" y "home"; Donde en "views" obtenemos la respuesta de la API; El archivo "home" es donde se proyectara la tabla con toda la informacion obtenida de la API; El archivo "urls" contiene las URLSs de las funciones de los otros componentes. Para resumirlo, la funcion "home" utiliza un GET en la API de "Rick & Morty" para obtener una respuesta por parte de dicha API, luego al momento de llamar la funcion home (a travez de la url) se mostrara la plantilla "home.html" proyectando los datos de todos los personajes de "Rick & Morty" (o al menos los que nos proporciona la API) en una tabla organizada, mostrandonos los datos de cada personaje en la tabla ordenadamente.