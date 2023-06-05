const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	nombreF: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	apellidoF: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	mailF: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	phoneF: /^\d{7,14}$/, // 7 a 14 numeros.
	direccionF: /^[a-zA-Z0-9-ÿ\s]{4,50}$/, // Letras, numeros.
}

const campos = {
	nombreF: false,
	apellidoF: false,
	mailF: false,
	phoneF: false,
	direccionF: false,
	regionF: false,
	comunaF: false,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "nombre":
			validarCampo(expresiones.nombreF, e.target, 'nombre');
		break;
		case "apellido":
			validarCampo(expresiones.apellidoF, e.target, 'apellido');
		break;
		case "correo":
			validarCampo(expresiones.mailF, e.target, 'correo');
			validarCorreo2();
		break;
		case "telefono":
			validarCampo(expresiones.mailF, e.target, 'telefono');
		break;
		case "direccion":
			validarCampo(expresiones.direccionF, e.target, 'direccion');
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		campos[campo] = false;
	}
}

const validarCorreo2 = () => {
	const inputCorreo1 = document.getElementById('correo');
	const inputCorreo2 = document.getElementById('correo2');

	if(inputCorreo1.value !== inputCorreo2.value){
		document.getElementById(`grupo__correo2`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__correo2`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__correo2 i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__correo2 i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__correo2 .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos['correo'] = false;
	} else {
		document.getElementById(`grupo__correo2`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__correo2`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__correo2 i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__correo2 i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__correo2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos['correo'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	e.preventDefault();

	const terminos = document.getElementById('terminos');
	if(campos.nombreF && campos.apellidoF  && campos.mailF && campos.phoneF && campos.direccionF ){
		formulario.reset();

		document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
		setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);

		document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
			icono.classList.remove('formulario__grupo-correcto');
		});
	} else {
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
});

