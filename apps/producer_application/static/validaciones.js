/*validar primer nombre*/

var vproType = false, vnombre = false, vapellido = false, vtelefono = false, vmail = false, vrut = false, vdireccion = false, vrazonsocial = false, vfechanac = false;

producerTypes = [];
function updateHiddenSelectedProducerTypes() {
  $("#id_selectedproducertypes").val(producerTypes.join(", "));
  console.log($("#id_selectedproducertypes").val())
}

$("#id_nombre").keyup(function () {
  var caracteres = $("#id_nombre").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#id_nombre").val().length;

  if (largo < 3 || largo > 30) {
    $("#id_fn_alert").text("Nombre inválido (mín. 3 caracteres, máx. 30 caracteres)");
    $("#id_fn_alert").css("color", "red");
    vnombre = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#id_fn_alert").text("Sólo puede ingresar letras");
    $("#id_fn_alert").css("color", "red");
    vnombre = false;
  } else {
    $("#id_fn_alert").text("Ingreso correcto");
    $("#id_fn_alert").css("color", "green");
    vnombre = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
      $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

/*validar apellido p*/

$("#id_apellido").keyup(function () {
  var caracteres = $("#id_apellido").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#id_apellido").val().length;

  if (largo < 3 || largo > 30) {
    $("#id_ln_alert").text("Apellido inválido (mín. 3 caracteres, máx. 30 caracteres)");
    $("#id_ln_alert").css("color", "red");
    vapellido = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#id_ln_alert").text("Sólo puede ingresar letras");
    $("#id_ln_alert").css("color", "red");
    vapellido = false;
  } else {
    $("#id_ln_alert").text("Ingreso correcto");
    $("#id_ln_alert").css("color", "green");
    vapellido = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

/*validar telefono*/

$("#id_telefono").keyup(function () {
  var telefono = $("#id_telefono").val();
  var regexNumeros = /^[0-9]+$/;

  if (!regexNumeros.test(telefono)) {
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

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});
/*validar correo*/
$("#id_correo").keyup(function () {
  var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
  var correo = $.trim($("#id_correo").val());
  if (correo === "") {
    $("#id_email_alert").text("Este campo no puede quedar vacío");
    $("#id_email_alert").css("color", "red");
    vmail = false;
  } else if (!patronCorreo.test(correo)) {
    $("#id_email_alert").text("Formato de correo electrónico incorrecto");
    $("#id_email_alert").css("color", "red");
    vmail = false;
  } else {
    $("#id_email_alert").text("Ingreso Correcto");
    $("#id_email_alert").css("color", "green");
    vmail = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$("#id_direccion").keyup(function (){
  var address = $("#id_direccion").val();
  var addressPattern = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s.,-]*$/;
  var addressLenght = $("#id_direccion").val().length;

  if (addressLenght < 3 || addressLenght > 100) {
      $("#id_address_alert").text("Dirección inválida (mín. 3 caracteres, máx. 100 caracteres)");
      $("#id_address_alert").css('color', 'red');
      vdireccion = false;
  } else if (!addressPattern.test(address)) {
      $("#id_address_alert").text("No puede ingresar caracteres especiales");
      $("#id_address_alert").css('color', 'red');
      vdireccion = false;
  } else {
      $("#id_address_alert").text("Ingreso correcto");
      $("#id_address_alert").css('color', 'green');
      vdireccion = true;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});
/*validar edad
$(document).ready(function () {
  $("#id_edad").on('input', function () {
    validarEdad();
  });
  function validarEdad() {
    var edadInput = $("#id_edad").val();
    var edadError = $("#id_edad_alert");
    var btnRegistrar = $("#id_register_button");

    if (edadInput !== "" && !isNaN(edadInput)) {
      if (parseInt(edadInput) > 17) {
        edadError.text("").removeClass("error-message").addClass("success-message");
        btnRegistrar.prop('disabled', false);
      } else {
        edadError.text("La edad debe ser mayor a 18 años.").removeClass("success-message").addClass("error-message");
        $("#id_edad_alert").css("color", "red");
        btnRegistrar.prop('disabled', true);
      }
    } else {
      edadError.text("Ingrese una edad válida.").removeClass("success-message").addClass("error-message");
      $("#edadId").css("color", "red");
      btnRegistrar.prop('disabled', true);
    }
  }
});
*/



/*validar rut*/
$("#id_rut").keyup(function () {
  var rut = $("#id_rut").val().replace(/[.-]/g, '').toUpperCase();

  if (validarRutChileno(rut)) {
    $("#id_dni_alert").text("RUT válido");
    $("#id_dni_alert").css("color", "green");
    vrut = true;
  } else {
    $("#id_dni_alert").text("RUT inválido");
    $("#id_dni_alert").css("color", "red");
    vrut = false;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

function validarRutChileno(rut) {
  var rutNumerico = rut.slice(0, -1);
  var dvIngresado = rut.slice(-1).toUpperCase();

  var suma = 0;
  var multiplo = 2;

  for (var i = rutNumerico.length - 1; i >= 0; i--) {
    suma += parseInt(rutNumerico.charAt(i)) * multiplo;

    if (multiplo < 7) {
      multiplo += 1;
    } else {
      multiplo = 2;
    }
  }

  var dvEsperado = 11 - (suma % 11);
  dvEsperado = (dvEsperado === 11) ? 0 : dvEsperado;
  dvEsperado = (dvEsperado === 10) ? "K" : dvEsperado.toString();

  return dvIngresado === dvEsperado;
}

/*validar razon social*/

$("#id_razon_social").keyup(function () {
  var caracteres = $("#id_razon_social").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#id_razon_social").val().length;

  if (largo < 3 || largo > 15) {
    $("#id_razon_alert").text("La razon social no puede ser menor a 3 caractéres o mayor a 15.");
    $("#id_razon_alert").css("color", "red");
    vrazonsocial = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#id_razon_alert").text("Sólo puede ingresar letras");
    $("#id_razon_alert").css("color", "red");
    vrazonsocial = false;
  } else {
    $("#id_razon_alert").text("Ingreso correcto");
    $("#id_razon_alert").css("color", "green");
    vrazonsocial = true;
  }

});

$("#id_fecha_nac").change(function (){
  var birthdate = new Date($("#id_fecha_nac").val());
  var today = new Date();
  var age = today.getFullYear() - birthdate.getFullYear()

  if (birthdate.getFullYear() < 1900 || birthdate.getFullYear() > today.getFullYear() ) {
      $("#id_fecha_alert").text("Seleccione un año válido");
      $("#id_fecha_alert").css("color", "red");
      vfechanac = false;
  }

  if (
      age > 18 ||
      (age === 18 && today.getMonth() > birthdate.getMonth()) ||
      (age === 18 && today.getMonth() === birthdate.getMonth() && today.getDate() >= birthdate.getDate())
  ) {
      $("#id_fecha_alert").text("Ingreso correcto")
      $("#id_fecha_alert").css("color", "green");
      vfechanac = true;
  } else {
      $("#id_fecha_alert").text("Debe ser mayor a 18 años")
      $("#id_fecha_alert").css("color", "red");
      vfechanac = false;
  }

  if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
    $("#id_register_button").attr('disabled', false);
  } else {
      $("#id_register_button").attr('disabled', true);
  }  
});

$(document).ready(function () {

  $("#id_register_button").attr('disabled', true);

  $("#id_add_producertype").click(function (){
      var selectedOption = $("#id_producertypes :selected");
      var selectedValue = $(selectedOption).val()
      
      if(selectedValue == ""){
          vproType = false
      } else {
          var selectedValueText = $(selectedOption).text()
          $("#id_selected_types").append('<option value="' + selectedValue + '">' + selectedValueText + '</option>');
          producerTypes.push(selectedValue)
          updateHiddenSelectedProducerTypes()
          $(selectedOption).remove()
          vproType = true
      }

      if(producerTypes.length == 0){
          vproType = false
      } else {
          vproType = true
      }

      if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }  
  });

  $("#id_delete_producertype").click(function (){
      var selectedOption = $("#id_list_of_selected_materials :selected");
      var selectedValue = $(selectedOption).val()
      var selectedValueText = $(selectedOption).text()
      if (producerTypes.length == 0){
          console.log("No ha seleccionado nada para que pueda ser borrado")   
      } else {
          $("#id_producertypes").append('<option value="' + selectedValue + '">' + selectedValueText + '</option>');
          var index = producerTypes.indexOf(selectedValue);
          if (index > -1) {
              producerTypes.splice(index, 1);
          }
          updateHiddenSelectedProducerTypes()
          $(selectedOption).remove();
          if(producerTypes.length == 0){
              vproType = false
          } else {
              vproType = true
          }
      }
      if(vrut && vnombre && vapellido && vdireccion && vtelefono && vmail && vproType && vrazonsocial && vfechanac){
        $("#id_register_button").attr('disabled', false);
      } else {
          $("#id_register_button").attr('disabled', true);
      }  
  });

});