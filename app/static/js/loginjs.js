function fazer_login() {
    const email = document.getElementById("email").value.trim()
    const senha = document.getElementById("password").value.trim()
    const mensagem = document.getElementById("mensagem");

    mensagem.innerText = "";
    mensagem.style.color = "red";

    if (!email || !senha) {
        mensagem.textContent = "Por favor, preencha todos os campos.";
        aplicarEfeitoTremer(mensagem);
        return;
    }

    // Envia o formulário para o Django processar
    document.getElementById("loginForm").submit();
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