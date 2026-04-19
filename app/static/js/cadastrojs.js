function validarCadastro() {
    const emailELemento = document.getElementById("email")
    const cpfElemento = document.getElementById("cpf")
    const senhaElemento = document.getElementById("password")

    const nome = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const cpf = document.getElementById("cpf").value.trim();
    const senha = document.getElementById("password").value.trim();
    const mensagem = document.getElementById("mensagem");

    //Limpar efeitos da tela
    mensagem.textContent = "";
    mensagem.classList.remove("shake");
    mensagem.style.color = "red";

    //Limpar os inputs
    emailELemento.classList.remove("is-invalid")
    senhaElemento.classList.remove("is-invalid")
    cpfElemento.classList.remove("is-invalid")

    //Mensagem pra quando todos inputs tiverem vazios
    if (!nome || !email || !cpf || !senha) {
      mostrarErro("Por favor, preencha todos os campos.");
      return;
    }
    
      //Validação de cada Campo do Cadastro
    if (!validarEmail(email)) {
      mostrarErro("E-mail inválido.", emailELemento);
      emailELemento.classList.add("is-invalid")
      return;
    }if (!validarSenha(senha)) {
      mostrarErro("A senha deve ter no mínimo 8 caracteres, com ao menos uma letra maiúscula e uma minúscula.",senhaElemento);
      senhaElemento.classList.add("is-invalid")
      return;
    }if (!validarCPF(cpf)) {
      mostrarErro("CPF inválido.", cpfElemento);
      cpfElemento.classList.add("is-invalid")
      return;
    }

    mensagem.style.color = "green";
    mensagem.textContent = "Cadastro realizado com sucesso!";
}

function mostrarErro(texto, elemento) {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = texto;
  aplicarEfeitoTremer(mensagem);
        
  // Agora aplica a classe APENAS ao elemento que causou o erro, le por ordem de cima pra baixo
  if (elemento) {
    elemento.classList.add("is-invalid");
  }
}

// Validação de e-mail simples com regex
function validarEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

// Validação de senha
function validarSenha(senha) {
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W_]).{8,}$/
  return regex.test(senha);
}

// Validação de CPF
function validarCPF(cpf) {
  cpf = cpf.replace(/\D/g, ""); // remove tudo que não for número

  if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;

  let soma = 0;
  for (let i = 0; i < 9; i++) soma += parseInt(cpf.charAt(i)) * (10 - i);
  let resto = 11 - (soma % 11);
  if (resto === 10 || resto === 11) resto = 0;
  if (resto !== parseInt(cpf.charAt(9))) return false;

  soma = 0;
  for (let i = 0; i < 10; i++) soma += parseInt(cpf.charAt(i)) * (11 - i);
  resto = 11 - (soma % 11);
  if (resto === 10 || resto === 11) resto = 0;
  return resto === parseInt(cpf.charAt(10));
}
function aplicarEfeitoTremer(elemento) {
  elemento.classList.add("shake");
  // Remove a classe após a animação para poder reutilizar depois
  setTimeout(() => elemento.classList.remove("shake"), 400);
}


function togglePassword() {
  const passwordField = document.getElementById('password');
  const eyeIcon = document.getElementById('eyeIcon');


    // Alterna o tipo do campo de senha
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);


    // Alterna o ícone do olhinho
    if (type === 'password') {
      eyeIcon.classList.remove('bi-eye');
      eyeIcon.classList.add('bi-eye-slash');
    } else {
      eyeIcon.classList.remove('bi-eye-slash');
      eyeIcon.classList.add('bi-eye');
    }
  }
