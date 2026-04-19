const Email_correto = "indiano@gmail.com"
const Senha_correta = "Indiano*123"

function fazer_login() {
    const email = document.getElementById("email").value.trim()
    const senha = document.getElementById("password").value.trim()
    const mensagem = document.getElementById("mensagem")

// Limpa mensagens anteriores
mensagem.innerText = ""
mensagem.classList.remove("shake"); // Remove o efeito anterior
mensagem.style.color = "red";
aplicarEfeitoTremer(mensagem)

if (!email || !senha) {
    mensagem.textContent = "Por favor, preencha todos os campos.";
    return;
}

    if (email === Email_correto && senha === Senha_correta) {
    // Redirecionar para a página inicial
    setTimeout(() => {
        window.location.href = "../homepage/homepagehtml.html"
    },)
    } else {
    mensagem.style.color = "red"
    mensagem.innerText = "E-mail ou senha incorretos."
    aplicarEfeitoTremer(mensagem)
    }
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