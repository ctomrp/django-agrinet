function Nombre(Pnombre) {
    var longitudMinima = 3;
    var longitudMaxima = 30;

    if (nombre.length > longitudMaxima) {
        alert("El nombre no debe exceder los " + longitudMaxima + " caracteres.");
        return false;
    } else if (nombre.length < longitudMinima) {
        alert("El nombre debe tener al menos " + longitudMinima + " caracteres.");
        return false;
    }

    return true;
}
