# Examen_1
 Un sistema de gestión de biblioteca en Python que permite administrar inventario de libros, préstamos y devoluciones, con visualización de estadísticas.

Características Principales
Gestión de Libros:

Añadir nuevos libros con título, autor y cantidad

Registrar copias disponibles y prestadas

Operaciones de Usuario:

Prestar libros (reduce copias disponibles)

Devolver libros (aumenta copias disponibles)

Consultas:

Verificar disponibilidad de libros

Mostrar inventario completo

Obtener recomendaciones personalizadas según historial de lectura

Visualización de Datos:

Gráficos de disponibilidad de libros

Listado de libros más prestados

Estructura del Código
Clase LibraryManager
Métodos Principales:
Operaciones Básicas:

add_book(título, autor, cantidad): Añade o actualiza libros

borrow_book(título, usuario): Registra préstamo

return_book(título, usuario): Registra devolución

check_availability(título): Verifica disponibilidad

Sistema de Recomendaciones:

suggest_book(usuario): Sugiere libros basados en historial

Visualización:

plot_availability(): Muestra gráfico de disponibilidad

plot_most_borrowed(top_n=5): Muestra libros más populares

Reportes:

show_inventory(): Imprime inventario completo
