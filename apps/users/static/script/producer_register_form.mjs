import {
    regexName, 
    regexNumber,
    regexEmail,
    regexPassword,
    regexBussinessName,
    regexDni
    } from '../../../../static/js/constants.js';

let vdni = false;
let vfirstname = false;
let vlastname = false;
let vaddress = false;
let vphone = false;
let vemail = false;
let vpassword = false;
let vreppass = false;
let vbussinessname = false ;
let vbirthdate = false;


$("#id_dni").on("keyup", function() {
    let run = $(this).val().replace(/\./g, '').replace('-', '').trim();  // Elimina espacios al principio y al final

    if (regexDni.test(run)) {
        const rut = run.slice(0, -1);
        const dv = run.slice(-1).toUpperCase();

        if (rut.length === 7) {
            rut = '0' + rut; // Agrega un cero al principio si solo hay 7 dígitos
        }

        let suma = 0;
        let multiplo = 2;

        for (let i = rut.length - 1; i >= 0; i--) {
            suma += rut.charAt(i) * multiplo;
            if (multiplo < 7) multiplo++;
            else multiplo = 2;
        }

        const resto = suma % 11;
        let resultado = 11 - resto;

        if (resultado === 11) resultado = 0;
        else if (resultado === 10) resultado = 'K';

        if (resultado == dv) {
            $("#id_dni_alert").text('RUT válido');
            $("#id_dni_alert").css('color', 'green');
            vdni = true;
        } else {
            $("#id_dni_alert").text('RUT inválido');
            $("#id_dni_alert").css('color', 'red');
            vdni = false;
        }
    } else {
        $("#id_dni_alert").text('Este campo no puede quedar vacío');
        $("#id_dni_alert").css('color', 'red');
        vdni = false;
        return 0;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_first_name").keyup(function (){
    const firstname = $("#id_first_name").val();
    const firstNameLength = $("#id_first_name").val().length;

    if (firstNameLength < 3 || firstNameLength > 30) {
        $("#id_fn_alert").text("Nombre inválido (mín. 3 caracteres, máx. 30 caracteres)");
        $("#id_fn_alert").css('color', 'red');
        vfirstname = false;
    } else if (!regexName.test(firstname)) {
        $("#id_fn_alert").text("Sólo puede ingresar letras");
        $("#id_fn_alert").css('color', 'red');
        vfirstname = false;
    } else {
        $("#id_fn_alert").text("Ingreso correcto");
        $("#id_fn_alert").css('color', 'green');
        vfirstname = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_last_name").keyup(function (){
    const lastname = $("#id_last_name").val();
    const lastnameLenght = $("#id_last_name").val().length;

    if (lastnameLenght < 3 || lastnameLenght > 30) {
        $("#id_ln_alert").text("Apellido inválido (mín. 3 caracteres, máx. 30 caracteres)");
        $("#id_ln_alert").css('color', 'red');
        vlastname = false;
    } else if (!regexName.test(lastname)) {
        $("#id_ln_alert").text("Sólo puede ingresar letras");
        $("#id_ln_alert").css('color', 'red');
        vlastname = false;
    } else {
        $("#id_ln_alert").text("Ingreso correcto");
        $("#id_ln_alert").css('color', 'green');
        vlastname = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
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
        vaddress = false;
    } else {
        $("#id_address_alert").text("Ingreso correcto");
        $("#id_address_alert").css('color', 'green');
        vaddress = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false)
    } else {
        $("#id_register_button").attr('disabled', true)
    }
});

$("#id_phone_number").keyup(function (){
    const phonenumber = $("#id_phone_number").val();

    if (!regexNumber.test(phonenumber)) {
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

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_email").keyup(function (){
    const email = $.trim($("#id_email").val());

    if (email === "") {
        $("#id_email_alert").text("Este campo no puede quedar vacío");
        $("#id_email_alert").css('color', 'red');
        vemail = false;
    } else if (!regexEmail.test(email)) {
        $("#id_email_alert").text("Formato de correo electrónico incorrecto");
        $("#id_email_alert").css('color', 'red');
        vemail = false;
    } else {
        $("#id_email_alert").text("Ingreso Correcto");
        $("#id_email_alert").css('color', 'green');
        vemail = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_password").keyup(function (){
    const password = $("#id_password").val();
    const passwordLength = $("#id_password").val().length;

    if(passwordLength < 8 || passwordLength > 20){
        $("#id_password_alert").text("Contraseña inválida. Debe tener: min. 8 caracteres, máx. 20 caracteres, una letra mayúscula, dos números y un carácter especial.")
        $("#id_password_alert").css("color", "red");
        vpassword = false;
    } else if (!regexPassword.test(password)) {
        $("#id_password_alert").text("Contraseña inválida. Debe tener: min. 8 caracteres, máx. 20 caracteres, una letra mayúscula, dos números y un carácter especial.")
        $("#id_password_alert").css("color", "red");
        vpassword = false;
    } else {
        $("#id_password_alert").text("Ingreso correcto")
        $("#id_password_alert").css("color", "green");
        vpassword = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_repeat_password").keyup(function (){
    const password = $("#id_password").val();
    const repeatPassword = $("#id_repeat_password").val();

    if(password === repeatPassword){
        $("#id_repeat_password_alert").text("Ambas contraseñas coinciden");
        $("#id_repeat_password_alert").css("color", "green");
        vreppass = true;
    } else {
        $("#id_repeat_password_alert").text("Las contraseñas no coinciden");
        $("#id_repeat_password_alert").css("color", "red");
        vreppass = false;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_bussiness_name").keyup(function (){
    const bussinessName = $("#id_bussiness_name").val()
    const bussinessNameLength = $("#id_bussiness_name").val().length

    if(bussinessNameLength < 3 || bussinessNameLength > 200 ){
        $("#id_bussinessname_alert").text("Razón social inválida (mín. 3 caracteres, máx. 200 caracteres)");
        $("#id_bussinessname_alert").css("color", "red");
        vbussinessname = false;
    } else if (!regexBussinessName.test(bussinessName)){
        $("#id_bussinessname_alert").text("Caracteres NO permitidos: ({, }, ´, ¨, |, °, ¬, `)");
        $("#id_bussinessname_alert").css("color", "red");
        vbussinessname = false;
    } else {
        $("#id_bussinessname_alert").text("Ingreso correcto");
        $("#id_bussinessname_alert").css("color", "green");
        vbussinessname = true;
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass &&  vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$("#id_birth_date").change(function (){
    const birthdate = new Date($("#id_birth_date").val());
    const today = new Date();
    const age = today.getFullYear() - birthdate.getFullYear();

    if (birthdate.getFullYear() < 1900 || birthdate.getFullYear() > today.getFullYear() ) {
        $("#id_birthdate_alert").text("Seleccione un año válido");
        $("#id_birthdate_alert").css("color", "red");
        vbirthdate = false
    } else if (
        age > 18 ||
        (age === 18 && today.getMonth() > birthdate.getMonth()) ||
        (age === 18 && today.getMonth() === birthdate.getMonth() && today.getDate() >= birthdate.getDate())
    ) {
        $("#id_birthdate_alert").text("Ingreso correcto")
        $("#id_birthdate_alert").css("color", "green");
        vbirthdate = true
    } else {
        $("#id_birthdate_alert").text("Debe ser mayor a 18 años")
        $("#id_birthdate_alert").css("color", "red");
        vbirthdate = false
    }

    if(vdni && vfirstname && vlastname && vaddress && vphone && vemail && vpassword && vreppass && vbussinessname && vbirthdate){
        $("#id_register_button").attr('disabled', false);
    } else {
        $("#id_register_button").attr('disabled', true);
    }
});

$(document).ready(function () {
    $("#id_register_button").attr('disabled', true)
});