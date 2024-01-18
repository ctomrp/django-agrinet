$(document).ready(function () {
    var originalCommunesOptions = $("#id_communes option").clone();

    $("#id_communes option").prop("disabled", true);

    $("#id_regions").change(function () {
        var selectedRegion = $(this).val();

        $("#id_communes").html(originalCommunesOptions);

        $("#id_communes option[data-comuna!='" + selectedRegion + "']").remove();
        $("#id_communes option[data-comuna='" + selectedRegion + "']").prop("disabled", false);

        $("#id_communes").val($("#id_communes option:enabled:first").val());
    });
});

