//Ejercicio para encontrar numeros pares e impares
let parInpar = 10;
if(parInpar % 2 == 0){
    console.log("Es un numero PAR");
}
else{
    console.log("Es un numero IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 18, adulto = 18;
if( edad >= adulto ){
    console.log("Usted es una persona adulta");
}
else{
    console.log("Usted es una persona menor de edad");
}

//Ejercicio: Dentro de un rango
let dentroRango = 10; //Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}