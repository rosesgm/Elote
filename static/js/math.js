// Evente que se dispara cuando se termina de cargar el DOM
// DOM: Document Object Model
document.addEventListener("DOMContentLoaded", function(){

    // Declaramos una variable en js que representa el boton en html
    var btnsuma= document.getElementById("btn-suma")
    var btnresta=document.getElementById("btn-resta")
    var btnmulti= document.getElementById("btn-multi")
    var btndivision=document.getElementById("btn-division")
    // Declaramos un evento click a ese boton
    btnsuma.addEventListener("click", function(){
        // agarramos el valor o contenido de la caja de texto input
        //El cual retorna un tipo string
        var value1 = document.getElementById("input-value1").value
        //Transformamos el string a un numero float
        var value1Number = parseFloat(value1) 

      
        var value2Number = parseFloat(document.getElementById("input-value2").value)
        //isNaN => is Not a Number
        //alert es un mensaje para el usuario
        //console es mensaje para el desarrollador
        if (isNaN(value1Number) || isNaN(value2Number)){
            alert("Por favor ingrese numeros validos")
            console.error("Se ingreso un valor no numerico")
            return
        }
            var result = value1Number + value2Number
            alert("El resultado es: " + result)
        
    })

    btnresta.addEventListener("click",function(){
        var value1 =parseFloat(document.getElementById("input-value1").value)
        var value2 =parseFloat(document.getElementById("input-value2").value)
        if (isNaN(value1) || isNaN(value2)){
            alert("Ingrese numeros validos")
            console.error("Se ingreso un valor no numerico")
            return
        }
            var result = value1 - value2
            alert("El resultado es: " + result)
        
    })
    btnmulti.addEventListener("click",function(){
        var value1 =parseFloat(document.getElementById("input-value1").value)
        var value2 =parseFloat(document.getElementById("input-value2").value)
        if (isNaN(value1) || isNaN(value2)){
            alert("Ingrese numeros validos")
            console.error("Se ingreso un valor no numerico")
            return
        }
            var result = value1 * value2
            alert("El resultado es: " + result)

    })
    btndivision.addEventListener("click",function(){
        var value1= parseFloat (document.getElementById("input-value1").value)
        var value2 = parseFloat(document.getElementById("input-value2").value)
        if (isNaN(value1) || isNaN(value2)){
            alert("Ingrese un número válido")
            console.error("Se ingreso un valor no numerico")
            return
        }
        if (value2===0){
            alert("NO se puede dividir entre 0")
            console.error("Se intento dividir por 0")
            return
        }
        var result=value1/value2
        alert("El resultado es:" + result)
        
           

    })
})