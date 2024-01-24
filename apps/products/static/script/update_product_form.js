
let vprodname = false;
let vprodprice = false;
let vprodstock = false;
let vproddesc = false;
let vprodcateg = false;

$(document).ready(function (){
    $("#id_saveproduct_button").attr('disabled', true);
});

$("#id_name").ready(function (){
    const prodNameLength = $("#id_name").val().length

    if(prodNameLength < 3 || prodNameLength > 255){
        $("#id_productname_alert").text("Nombre de producto inválido (mín 3 caracteres, máx 255 caracteres)");
        $("#id_productname_alert").css('color', 'red');
        vprodname = false;
    } else {
        $("#id_productname_alert").text("Ingreso correcto");
        $("#id_productname_alert").css('color', 'green');
        vprodname = true;
    }
     
    if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
        $("#id_saveproduct_button").attr('disabled', false);
    } else {
        $("#id_saveproduct_button").attr('disabled', true);
    }

    $("#id_name").keyup(function (){
        const prodNameLength = $("#id_name").val().length
    
        if(prodNameLength < 3 || prodNameLength > 255){
            $("#id_productname_alert").text("Nombre de producto inválido (mín 3 caracteres, máx 255 caracteres)");
            $("#id_productname_alert").css('color', 'red');
            vprodname = false;
        } else {
            $("#id_productname_alert").text("Ingreso correcto");
            $("#id_productname_alert").css('color', 'green');
            vprodname = true;
        }
    
         
        if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
            $("#id_saveproduct_button").attr('disabled', false);
        } else {
            $("#id_saveproduct_button").attr('disabled', true);
        }
    });
});

$("#id_price").ready(function(){
    const productPrice = $("#id_price").val()

    if(productPrice <= 0){
        $("#id_productprice_alert").text("Error. El precio debe mayor a 0");
        $("#id_productprice_alert").css('color', 'red');
        vprodprice = false;
    } else {
        $("#id_productprice_alert").text("Ingreso correcto");
        $("#id_productprice_alert").css('color', 'green');
        vprodprice = true;
    }

    if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
        $("#id_saveproduct_button").attr('disabled', false);
    } else {
        $("#id_saveproduct_button").attr('disabled', true);
    }

    $("#id_price").keyup(function(){
        const productPrice = $("#id_price").val()
    
        if(productPrice <= 0){
            $("#id_productprice_alert").text("Error. El precio debe mayor a 0");
            $("#id_productprice_alert").css('color', 'red');
            vprodprice = false;
        } else {
            $("#id_productprice_alert").text("Ingreso correcto");
            $("#id_productprice_alert").css('color', 'green');
            vprodprice = true;
        }
    
        if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
            $("#id_saveproduct_button").attr('disabled', false);
        } else {
            $("#id_saveproduct_button").attr('disabled', true);
        }
    });
});

$("#id_stock").ready(function(){
    const productStock = $("#id_stock").val()

    if(productStock < 0){
        $("#id_productstock_alert").text("Error. El stock debe ser 0 o mayor");
        $("#id_productstock_alert").css('color', 'red');
        vprodstock = false;
    } else {
        $("#id_productstock_alert").text("Ingreso correcto");
        $("#id_productstock_alert").css('color', 'green');
        vprodstock = true;
    }

    if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
        $("#id_saveproduct_button").attr('disabled', false);
    } else {
        $("#id_saveproduct_button").attr('disabled', true);
    }

    $("#id_stock").keyup(function(){
        const productStock = $("#id_stock").val()
    
        if(productStock < 0){
            $("#id_productstock_alert").text("Error. El stock debe ser 0 o mayor");
            $("#id_productstock_alert").css('color', 'red');
            vprodstock = false;
        } else {
            $("#id_productstock_alert").text("Ingreso correcto");
            $("#id_productstock_alert").css('color', 'green');
            vprodstock = true;
        }
    
        if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
            $("#id_saveproduct_button").attr('disabled', false);
        } else {
            $("#id_saveproduct_button").attr('disabled', true);
        }
    });
});

$("#id_description").ready(function(){
    const descriptionLength = $("#id_description").val()

    if(descriptionLength < 3 || descriptionLength > 255){
        $("#id_productdescription_alert").text("Descripción de producto inválida (mín 3 caracteres, máx 255 caracteres)");
        $("#id_productdescription_alert").css('color', 'red');
        vproddesc = false;
    } else {
        $("#id_productdescription_alert").text("Ingreso correcto");
        $("#id_productdescription_alert").css('color', 'green');
        vproddesc = true;
    }

    if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
        $("#id_saveproduct_button").attr('disabled', false);
    } else {
        $("#id_saveproduct_button").attr('disabled', true);
    }

    $("#id_description").keyup(function(){
        const descriptionLength = $("#id_description").val()
    
        if(descriptionLength < 3 || descriptionLength > 255){
            $("#id_productdescription_alert").text("Descripción de producto inválida (mín 3 caracteres, máx 255 caracteres)");
            $("#id_productdescription_alert").css('color', 'red');
            vproddesc = false;
        } else {
            $("#id_productdescription_alert").text("Ingreso correcto");
            $("#id_productdescription_alert").css('color', 'green');
            vproddesc = true;
        }
    
        if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
            $("#id_saveproduct_button").attr('disabled', false);
        } else {
            $("#id_saveproduct_button").attr('disabled', true);
        }
    });
});

$("#id_category").ready(function(){
    const productCategory = $("#id_category").val()

    if(productCategory === ""){
        $("#id_productcategory_alert").text("Seleccione una categoría válida");
        $("#id_productcategory_alert").css('color', 'red');
        vprodcateg = false;
    } else {
        $("#id_productcategory_alert").text("Ingreso correcto");
        $("#id_productcategory_alert").css('color', 'green');
        vprodcateg = true;
    }

    if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
        $("#id_saveproduct_button").attr('disabled', false);
    } else {
        $("#id_saveproduct_button").attr('disabled', true);
    }

    $("#id_category").change(function(){
        const productCategory = $("#id_category").val()
    
        if(productCategory === ""){
            $("#id_productcategory_alert").text("Seleccione una categoría válida");
            $("#id_productcategory_alert").css('color', 'red');
            vprodcateg = false;
        } else {
            $("#id_productcategory_alert").text("Ingreso correcto");
            $("#id_productcategory_alert").css('color', 'green');
            vprodcateg = true;
        }
    
        if(vprodname && vprodprice && vprodstock && vproddesc && vprodcateg){
            $("#id_saveproduct_button").attr('disabled', false);
        } else {
            $("#id_saveproduct_button").attr('disabled', true);
        }
    });
});