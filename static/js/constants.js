export const regexName = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
export const regexNumber = /^[0-9]+$/;
export const regexEmail = /^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$/;
export const regexPassword = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d.*\d)(?=.*[!@#$%^&*()_+,.\-])[A-Za-z\d!@#$%^&*()_+,.\-]+$/;
export const regexBussinessName = /^[a-zA-Z0-9'!@#$%^&*()-_+=?<> ]+$/;
export const regexDni = /^\d{7,8}[-]?\w$/;