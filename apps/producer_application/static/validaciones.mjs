import {
  regexName, 
  regexNumber,
  regexEmail,
  regexBussinessName
  } from '../../../../static/js/constants.js';

/*validar primer nombre*/

let vrut = false;
let vnombre = false;
let vapellido = false;
let vdireccion = false;
let vtelefono = false;
let vmail = false;
let vrazonsocial = false ;
let vfechanac = false;
let vregion = false;
let vcommune = false;


$("#id_first_name").keyup(function () {
  const caracteres = $("#id_first_name").val();
  const largo = $("#id_first_name").val().length;

  if (largo < 3 || largo > 30) {
    $("#id_fn_alert").text("Nombre inválido (mín. 3 caracteres, máx. 30 caracteres)");
    $("#id_fn_alert").css("color", "red");
    vnombre = false;
  } else if (!regexName.test(caracteres)) {
    $("#id_fn_alert").text("Sólo puede ingresar letras");
    $("#id_fn_alert").css("color", "red");
    vnombre = false;
  } else {
    $("#id_fn_alert").text("Ingreso correcto");
    $("#id_fn_alert").css("color", "green");
    vnombre = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

/*validar apellido p*/

$("#id_last_name").keyup(function () {
  const caracteres = $("#id_last_name").val();
  const largo = $("#id_last_name").val().length;

  if (largo < 3 || largo > 30) {
    $("#id_ln_alert").text("Apellido inválido (mín. 3 caracteres, máx. 30 caracteres)");
    $("#id_ln_alert").css("color", "red");
    vapellido = false;
  } else if (!regexName.test(caracteres)) {
    $("#id_ln_alert").text("Sólo puede ingresar letras");
    $("#id_ln_alert").css("color", "red");
    vapellido = false;
  } else {
    $("#id_ln_alert").text("Ingreso correcto");
    $("#id_ln_alert").css("color", "green");
    vapellido = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
    $("#id_register_button").attr('disabled', false);
} else {
    $("#id_register_button").attr('disabled', true);
}  
});

/*validar telefono*/

$("#id_phone_number").keyup(function () {
  const telefono = $("#id_phone_number").val();

  if (!regexNumber.test(telefono)) {
    $("#id_phone_alert").text("Ingresa solo números");
    $("#id_phone_alert").css("color", "red");
    vtelefono = false;
  } else {
    if (telefono < 900000000 || telefono > 999999999) {
      $("#id_phone_alert").text("Número inválido");
      $("#id_phone_alert").css("color", "red");
      vtelefono = false;
    } else {
      $("#id_phone_alert").text("Ingreso correcto");
      $("#id_phone_alert").css("color", "green");
      vtelefono = true;
    }
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});
/*validar correo*/
$("#id_email").keyup(function () {
  const correo = $.trim($("#id_email").val());

  if (correo === "") {
    $("#id_email_alert").text("Este campo no puede quedar vacío");
    $("#id_email_alert").css("color", "red");
    vmail = false;
  } else if (!regexEmail.test(correo)) {
    $("#id_email_alert").text("Formato de correo electrónico incorrecto");
    $("#id_email_alert").css("color", "red");
    vmail = false;
  } else {
    $("#id_email_alert").text("Ingreso Correcto");
    $("#id_email_alert").css("color", "green");
    vmail = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$("#id_address").keyup(function (){
  const addressLenght = $("#id_address").val().length;

  if (addressLenght < 3 || addressLenght > 255) {
      $("#id_address_alert").text("Dirección inválida (mín. 3 caracteres, máx. 255 caracteres)");
      $("#id_address_alert").css('color', 'red');
      vdireccion = false;
  } else {
      $("#id_address_alert").text("Ingreso correcto");
      $("#id_address_alert").css('color', 'green');
      vdireccion = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});


/*validar rut*/
$("#id_dni").keyup(function () {
  const rut = $("#id_dni").val().replace(/[.-]/g, '').toUpperCase();

  if (validarRutChileno(rut)) {
    $("#id_dni_alert").text("RUT válido");
    $("#id_dni_alert").css("color", "green");
    vrut = true;
  } else {
    $("#id_dni_alert").text("RUT inválido");
    $("#id_dni_alert").css("color", "red");
    vrut = false;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

function validarRutChileno(rut) {
  const rutNumerico = rut.slice(0, -1);
  const dvIngresado = rut.slice(-1).toUpperCase();

  let suma = 0;
  let multiplo = 2;

  for (let i = rutNumerico.length - 1; i >= 0; i--) {
    suma += parseInt(rutNumerico.charAt(i)) * multiplo;

    if (multiplo < 7) {
      multiplo += 1;
    } else {
      multiplo = 2;
    }
  }

  let dvEsperado = 11 - (suma % 11);
  dvEsperado = (dvEsperado === 11) ? 0 : dvEsperado;
  dvEsperado = (dvEsperado === 10) ? "K" : dvEsperado.toString();

  return dvIngresado === dvEsperado;
}

/*validar razon social*/

$("#id_bussiness_name").keyup(function () {
  const caracteres = $("#id_bussiness_name").val();
  const largo = $("#id_bussiness_name").val().length;

  if (largo < 3 || largo > 25) {
    $("#id_razon_alert").text("La razon social no puede ser menor a 3 caractéres o mayor a 25.");
    $("#id_razon_alert").css("color", "red");
    vrazonsocial = false;
  } else if (!regexBussinessName.test(caracteres)) {
    $("#id_razon_alert").text("Sólo puede ingresar letras y números");
    $("#id_razon_alert").css("color", "red");
    vrazonsocial = false;
  } else {
    $("#id_razon_alert").text("Ingreso correcto");
    $("#id_razon_alert").css("color", "green");
    vrazonsocial = true;
  }

});

/*validar fecha cumpleaños*/


$("#id_birth_date").change(function (){
    const birthdate = new Date($("#id_birth_date").val());
    const today = new Date();
    const age = today.getFullYear() - birthdate.getFullYear()

    if (birthdate.getFullYear() < 1900 || birthdate.getFullYear() > today.getFullYear() ) {
        $("#id_fecha_alert").text("Seleccione un año válido");
        $("#id_fecha_alert").css("color", "red");
        vfechanac = false
    } else if (
        age > 18 ||
        (age === 18 && today.getMonth() > birthdate.getMonth()) ||
        (age === 18 && today.getMonth() === birthdate.getMonth() && today.getDate() >= birthdate.getDate())
    ) {
        $("#id_fecha_alert").text("Ingreso correcto")
        $("#id_fecha_alert").css("color", "green");
        vfechanac = true
    } else {
        $("#id_fecha_alert").text("Debe ser mayor a 18 años")
        $("#id_fecha_alert").css("color", "red");
        vfechanac = false
    }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$("#id_regions").change(function(){
  const region = $("#id_regions").val()

  if(region === ""){
    vregion = false;
  } else {
    vregion = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$("#id_communes").change(function(){
  const commune = $("#id_communes").val()
  
  if(commune === ""){
    vcommune = false;
  } else {
    vcommune = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$(document).ready(function() {
  // ... (tu código de validación existente)

  $("#id_register_button").attr('disabled', true)

  $("#id_register_button").click(function() {
      // Realizar validación antes de mostrar el mensaje
      if (validarCampos()) {
          const mensaje = "¡Postulación enviada correctamentes!";
          mostrarMensaje(mensaje);
      } else {
          // Cambiar el mensaje de error de console.log a alert
          const mensajeError = "Error en la validación de campos. Por favor, complete todos los campos correctamente.";
          alert(mensajeError);
      }
  });
});

function validarCampos() {
  // Utilizando las variables de validación existentes
  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vrazonsocial && vfechanac && vregion && vcommune) {
      return true;  // Todos los campos son válidos
  } else {
      // Muestra un mensaje de error o realiza otra acción si algún campo no es válido
      alert("Por favor, complete todos los campos correctamente.");
      return false;
  }
}

function mostrarMensaje(mensaje) {
  // Mostrar el mensaje utilizando alert
  alert(mensaje);
}