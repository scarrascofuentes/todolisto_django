# Taller: Todo Listo en Django

Respecto a los requerimientos:

  * Es necesario tener instalado:
    * Framework Django en su version 2.0
    * XAMPP en su version 3.2.2
    * Anaconda

  * Sistema Operativo:
    * Windows 10

Respecto a la instalacion:
  * COMPLETAR

Respecto a la ejecucion:
  * Durante la ejecucion, en XAMPP, debe tener activados los modulos 'Apache' y 'MySQL' 

Respecto a los controladores:

  * COMPLETAR

Respecto a los modelos:

  * COMPLETAR

Respecto a las vistas:

  * COMPLETAR

Respecto a los datos iniciales en la base de datos:

  * DETERMINAR SI MANDAMOS LA BASE EN SQL O INDICAMOS COMO CREARLA

Respecto de las funciones del sistema:

1. Para registrarse en el sistema debe acceder a la URL `/todolisto/register`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Sign In".

2. Para ingresar al sistema debe acceder a la URL `/todolisto/login`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Login".

3. Para crear una tarea o ver el listado de tareas del usuario se debe acceder a la URL `/todolisto/tareas`
Dentro de esta vista, en caso de querer crear una tarea, debe completar los campos solicitados y luego. presionar el boton "Crear". Ademas, esta vista ofrece tres opciones para cada tarea: Detalle, Editar y Eliminar l

4. Para ver el detalle una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/detalleTarea/"id"`.
Dentro de esta vista se puede modificar la tarea seleccionada tras presionar el boton "Editar".

5. Para modificar una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/editarTarea/"id"`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Guardar".

5. Para eliminar una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/eliminarTarea/"id"`
Dentro de esta vista debe presionar el boton "Aceptar" para completar la accion.

6. Para ver el calendario que contiene todas las tareas del usuario se debe acceder a la URL `/todolisto/calendario`.

7. Para ver las tareas de todos los usuarios del sistema es necesario loguearse como administrador. 
 