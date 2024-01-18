var vdni = false, vfirstname = false, vlastname = false, vaddress = false, vphone = false, vemail = false, vpassword = false, vreppass = false;

$(document).ready(function () {
    $("#id_register_button").attr('disabled', true)
});

$("#id_dni").on("keyup", function() {
    var run = $(this).val().replace(/\./g, '').replace('-', '').trim();  // Elimina espacios al principio y al final

    if (/^\d{7,8}[-]?\w$/.test(run)) {
        var rut = run.slice(0, -1);
        var dv = run.slice(-1).toUpperCase();

        if (rut.length === 7) {
            rut = '0' + rut; // Agrega un cero al principio si solo hay 7 dígitos
        }

        var suma = 0;
        var multiplo = 2;

        for (var i = rut.length - 1; i >= 0; i--) {
            suma += rut.charAt(i) * multiplo;
            if (multiplo < 7) multiplo++;
            else multiplo = 2;
        }

        var resto = suma % 11;
        var resultado = 11 - resto;

        if (resultado === 11) resultado = 0;
        else if (resultado === 10) resultado = 'K';

        if (resultado == dv) {
            $("#id_dni_alert").text('RUN válido');
            $("#id_dni_alert").css('color', 'green');
            vdni = true;
        } else {
            $("#id_dni_alert").text('RUN inválido');
            $("#id_dni_alert").css('color', 'red');
            vdni = false;
        }
    } else {
        $("#id_dni_alert").text('Este campo no puede quedar vacío');
        $("#id_dni_alert").css('color', 'red');
        vdni = false;
        return 0;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_first_name").keyup(function (){
    var characters = $("#id_first_name").val();
    var namePattern = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var nameLength = $("#id_first_name").val().length;

    if (nameLength < 3 || nameLength > 30) {
        $("#id_fn_alert").text("Nombre inválido (mín. 3 caracteres, máx. 30 caracteres)");
        $("#id_fn_alert").css('color', 'red');
        vfirstname = false;
    } else if (!namePattern.test(characters)) {
        $("#id_fn_alert").text("Sólo puede ingresar letras");
        $("#id_fn_alert").css('color', 'red');
        vfirstname = false;
    } else {
        $("#id_fn_alert").text("Ingreso correcto");
        $("#id_fn_alert").css('color', 'green');
        vfirstname = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_last_name").keyup(function (){
    var characters = $("#id_last_name").val();
    var lastnamePattern = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    var lastnameLenght = $("#id_last_name").val().length;

    if (lastnameLenght < 3 || lastnameLenght > 30) {
        $("#id_ln_alert").text("Apellido inválido (mín. 3 caracteres, máx. 30 caracteres)");
        $("#id_ln_alert").css('color', 'red');
        vlastname = false;
    } else if (!lastnamePattern.test(characters)) {
        $("#id_ln_alert").text("Sólo puede ingresar letras");
        $("#id_ln_alert").css('color', 'red');
        vlastname = false;
    } else {
        $("#id_ln_alert").text("Ingreso correcto");
        $("#id_ln_alert").css('color', 'green');
        vlastname = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_address").keyup(function (){
    var characters = $("#id_address").val();
    var addressLenght = $("#id_address").val().length;

    if (addressLenght < 3 || addressLenght > 255) {
        $("#id_address_alert").text("Dirección inválida (mín. 3 caracteres, máx. 255 caracteres)");
        $("#id_address_alert").css('color', 'red');
        vaddress = false;
    } else {
        $("#id_address_alert").text("Ingreso correcto");
        $("#id_address_alert").css('color', 'green');
        vaddress = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_phone_number").keyup(function (){
    var phonenumber = $("#id_phone_number").val();
    var patternNumber = /^[0-9]+$/;

    if (!patternNumber.test(phonenumber)) {
        $("#id_phone_alert").text("Ingresa solo números");
        $("#id_phone_alert").css('color', 'red');
        vphone = false;
    } else {
        if (phonenumber < 900000000 || phonenumber > 999999999) {
            $("#id_phone_alert").text("Número inválido");
            $("#id_phone_alert").css('color', 'red');
            vphone = false;
        } else {
            $("#id_phone_alert").text("Ingreso correcto");
            $("#id_phone_alert").css('color', 'green');
            vphone = true;
        }
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_email").keyup(function (){
    var patternEmail = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
    var email = $.trim($("#id_email").val());

    if (email === "") {
        $("#id_email_alert").text("Este campo no puede quedar vacío");
        $("#id_email_alert").css('color', 'red');
        vemail = false;
    } else if (!patternEmail.test(email)) {
        $("#id_email_alert").text("Formato de correo electrónico incorrecto");
        $("#id_email_alert").css('color', 'red');
        vemail = false;
    } else {
        $("#id_email_alert").text("Ingreso Correcto");
        $("#id_email_alert").css('color', 'green');
        vemail = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_password").keyup(function (){
    var password = $("#id_password").val();
    var patternPassword = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d)(?=.*[!@#$%^&*()_+,.\-])[A-Za-z\d!@#$%^&*()_+,.\-]+$/;
    var passwordLength = $("#id_password").val().length;

    if(passwordLength < 8 || passwordLength > 20){
        $("#id_password_alert").text("Contraseña inválida. Debe tener: min. 8 caracteres, máx. 20 caracteres, una letra mayúscula, dos números y un carácter especial.")
        $("#id_password_alert").css("color", "red");
        vpassword = false;
    } else if (!patternPassword.test(password)) {
        $("#id_password_alert").text("Contraseña inválida. Debe tener: min. 8 caracteres, máx. 20 caracteres, una letra mayúscula, dos números y un carácter especial.")
        $("#id_password_alert").css("color", "red");
        vpassword = false;
    } else {
        $("#id_password_alert").text("Ingreso correcto")
        $("#id_password_alert").css("color", "green");
        vpassword = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_repeat_password").keyup(function (){
    var password = $("#id_password").val();
    var repeatPassword = $("#id_repeat_password").val();

    if(password === repeatPassword){
        $("#id_repeat_password_alert").text("Ambas contraseñas coinciden");
        $("#id_repeat_password_alert").css("color", "green");
        vreppass = true;
    } else {
        $("#id_repeat_password_alert").text("Las contraseñas no coinciden");
        $("#id_repeat_password_alert").css("color", "red");
        vreppass = false;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});