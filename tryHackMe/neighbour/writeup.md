![alt text](img/image.png)

## Contexto
Check out our new cloud service, Authentication Anywhere -- log in from anywhere you would like! Users can enter their username and password, for a totally secure login process! You definitely wouldn't be able to find any secrets that other people have in their profile, right?

## Preguntas
- Find the flag on your neighbor's logged in page!

## Solucion
Accedemos al servicio web y visualizamos un panel de autenticacion.
![alt text](img/image-2.png)

Revisamos el codigo html con *"ctrl + u"*

![alt text](img/image-1.png)

Visualizamos credencial **"guest:guest"** que ingresamos en el login que nos redirige a *"profile.php"*.

![alt text](img/image-3.png)
![alt text](img/image-4.png)

En aqui prestamos atencion es la url.

![alt text](img/image-5.png)

Cambiamos el valor del parametro **user** de '*guest*' a '*admin*' y obtenemos la flag.

![alt text](img/image-6.png)