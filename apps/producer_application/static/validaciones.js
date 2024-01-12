/*validar primer nombre*/
var vnombre
$("#idnombre").keyup(function () {
  var caracteres = $("#idnombre").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#idnombre").val().length;

  if (largo < 3 || largo > 15) {
    $("#nombre").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
    $("#nombre").css("color", "red");
    vnombre = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#nombre").text("Sólo puede ingresar letras");
    $("#nombre").css("color", "red");
    vnombre = false;
  } else {
    $("#nombre").text("Ingreso correcto");
    $("#nombre").css("color", "green");
    vnombre = true;
  }

});

/*validar apellido p*/
var vapellido
$("#apellidoId").keyup(function () {
  var caracteres = $("#apellidoId").val();
  var patronNombre = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
  var largo = $("#apellidoId").val().length;

  if (largo < 3 || largo > 15) {
    $("#apellido").text("El nombre no puede ser menor a 3 caractéres o mayor a 15.");
    $("#apellido").css("color", "red");
    vnombre = false;
  } else if (!patronNombre.test(caracteres)) {
    $("#apellido").text("Sólo puede ingresar letras");
    $("#apellido").css("color", "red");
    vnombre = false;
  } else {
    $("#apellido").text("Ingreso correcto");
    $("#apellido").css("color", "green");
    vnombre = true;
  }

});

/*validar telefono*/
var vtelefono
$("#TelId").keyup(function () {
  var telefono = $("#TelId").val();
  var regexNumeros = /^[0-9]+$/;

  if (!regexNumeros.test(telefono)) {
    $("#teleId").text("Ingresa solo números");
    $("#teleId").css("color", "red");
    vtelefono = false;
  } else {
    if (telefono < 900000000 || telefono > 999999999) {
      $("#teleId").text("Número inválido");
      $("#teleId").css("color", "red");
      vtelefono = false;
    } else {
      $("#teleId").text("Ingreso correcto");
      $("#teleId").css("color", "green");
      vtelefono = true;
    }
  }

});
/*validar correo*/
vmail = false
$("#EmailId").keyup(function () {
  var patronCorreo = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
  var correo = $.trim($("#EmailId").val());
  if (correo === "") {
    $("#EId").text("Este campo no puede quedar vacío");
    $("#EId").css("color", "red");
    vmail = false;
  } else if (!patronCorreo.test(correo)) {
    $("#EId").text("Formato de correo electrónico incorrecto");
    $("#EId").css("color", "red");
    vmail = false;
  } else {
    $("#EId").text("Ingreso Correcto");
    $("#EId").css("color", "green");
    vmail = true;
  }
});


/*validar edad*/
$(document).ready(function () {
  $("#edad").on('input', function () {
    validarEdad();
  });
  function validarEdad() {
    var edadInput = $("#edad").val();
    var edadError = $("#edadId");
    var btnRegistrar = $("#btnRegistrarId");

    if (edadInput !== "" && !isNaN(edadInput)) {
      if (parseInt(edadInput) > 17) {
        edadError.text("").removeClass("error-message").addClass("success-message");
        btnRegistrar.prop('disabled', false);
      } else {
        edadError.text("La edad debe ser mayor a 18 años.").removeClass("success-message").addClass("error-message");
        $("#edadId").css("color", "red");
        btnRegistrar.prop('disabled', true);
      }
    } else {
      edadError.text("Ingrese una edad válida.").removeClass("success-message").addClass("error-message");
      $("#edadId").css("color", "red");
      btnRegistrar.prop('disabled', true);
    }
  }
});



/*validar rut*/
$("#Idrut").keyup(function () {
  var rut = $("#Idrut").val().replace(/[.-]/g, '').toUpperCase();

  if (validarRutChileno(rut)) {
    $("#rutid").text("RUT válido");
    $("#rutid").css("color", "green");
    vrut = true;
  } else {
    $("#rutid").text("RUT inválido");
    $("#rutid").css("color", "red");
    vrut = false;
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
$(document).keyup(function () {
  $("#razonsocialId").on('input', function () {
    var razonSocial = $(this).val();

    if (razonSocial.length > 20) {
      $("#socialId").text("La Razón Social no puede tener más de 20 caracteres.");
      $("#socialId").css("color", "red");
    } else {
      $("#socialId").text("");
    }
  });
});



$(document).ready(function () {
  $('#tipoid').change(function () {
      var producto = $("#tipoid");

      if (producto.val() === "") {
          document.getElementById("result").innerHTML = "<b>Seleccione una opción</b>";
          document.getElementById("result").style.color = "red";
      } else {
          document.getElementById("result").innerHTML = "La opción seleccionada es: <b>" + producto.val() + "</b>";
          document.getElementById("result").style.color = "green";
      }
  });
});