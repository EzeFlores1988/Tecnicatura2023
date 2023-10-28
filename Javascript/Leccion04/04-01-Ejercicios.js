//Ampliando el uso de var let y const
/*
Con var puedes reasignar en cualquier momento
esta forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = "Ezequiel";
nombre = 'Juan';
console.log(nombre);

function saludar(){
    var nombre3 = 'Pedro';
    console.log(nombre3);
}
//console.log(nombre3); //Aqui no lee el dato en la funcion


if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo

/*
Let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = 'Ezequiel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad = 33;
    console.log(edad);
}

/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 1988;
console.log(fechaNacimiento);
//fechaNacimiento = 1990;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior