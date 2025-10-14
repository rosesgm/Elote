// Evente que se dispara cuando se termina de cargar el DOM
// DOM: Document Object Model
document.addEventListener("DOMContentLoaded", function(){

    // Declaramos una variable en js que representa el boton en html
    var btnOK= document.getElementById("btn-ok")
    
    // Declaramos un evento click a ese boton
    btnOK.addEventListener("click", function(){
        // Declaramos una variable del input  de HTML
        var name = document.getElementById("input-name")

        // Mostramos un alerta del navegador con el contenido del intup
        alert("hola " + name.value + " zorrete")
        console.log("Se imprimio el hola zorrete")
        console.error("Esto es un error simulado")
    })

})