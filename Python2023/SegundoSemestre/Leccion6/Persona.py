class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ezequiel', 'Flores', 35)  # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
persona2 = Persona('Jessica', 'Pagano', 30)
print(f'El objeto2 de la clase persona es: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Gianella'
persona1.apellido = 'Achetoni'
persona1.edad = 18
print(
    f'El objeto1 modificado de la clase persona es: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()