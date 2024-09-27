document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("criacao");
  const titulo = document.getElementById("titulo");
  const descricao = document.getElementById("descricao");
  const curta = document.getElementsByClassName("curta")[0];
  const longa = document.getElementsByClassName("longa")[0];
  const alternativas = document.getElementsByClassName("alternativas")[0];
  const selectPerguntas = document.getElementById("add");
  const acoes = document.getElementById("acoes");
  const excluirForm = document.getElementById("form-exclusao");
  const multiplaContainer = document.querySelector(".multipla-container");

  const adicionarPerguntas = (campo) => {
    const campoSelecionado = campo.cloneNode(true);
    campoSelecionado.style.display = "block";

    const btnRemover = document.createElement("button");
    btnRemover.type = "button";
    btnRemover.textContent = "Remover pergunta";
    btnRemover.classList.add("remover-pergunta");
    btnRemover.onclick = function () {
      campoSelecionado.remove();
    };

    campoSelecionado.appendChild(btnRemover);
    formulario.insertBefore(campoSelecionado, acoes);

    if (campoSelecionado.classList.contains("alternativas")) {
      const opcoesContainer = campoSelecionado.querySelector(
        ".opcoes-alternativas"
      );
      const adicionarOpcoesBtn =
        campoSelecionado.querySelector(".adicionar-opcao");

      adicionarOpcoesBtn.addEventListener("click", () => {
        adicionarOpcao(opcoesContainer);
      });
    } else if (campoSelecionado.classList.contains("multipla-container")) {
      const adicionarOpcoesBtn =
        campoSelecionado.querySelector(".adicionar-opcao");
      const multiplaRespostasDiv = campoSelecionado.querySelector(
        ".multipla-respostas"
      );

      adicionarOpcoesBtn.addEventListener("click", () => {
        adicionarOpcaoMultipla(multiplaRespostasDiv);
      });
    }
  };

  let contadoraAlternativa = 0;
  const adicionarOpcao = (container) => {
    const opcaoContainer = document.createElement("div");
    opcaoContainer.classList.add("opcao-container");
    opcaoContainer.style.display = "flex";
    opcaoContainer.style.alignItems = "center";

    const opcaoInput = document.createElement("input");
    opcaoInput.type = "text";
    opcaoInput.placeholder = "Opção";
    opcaoInput.classList.add("opcao-alternativa");
    opcaoInput.name = `textoOpcaoAlternativa[${contadoraAlternativa}]`;
    contadoraAlternativa += 1;

    const btnRemover = document.createElement("button");
    btnRemover.type = "button";
    btnRemover.textContent = "Remover opção";
    btnRemover.classList.add("remover-opcao");
    btnRemover.onclick = function () {
      opcaoContainer.remove();
    };

    opcaoContainer.appendChild(opcaoInput);
    opcaoContainer.appendChild(btnRemover);
    container.appendChild(opcaoContainer);
  };

  let contadoraMultipla = 0;

  const adicionarOpcaoMultipla = (container) => {
    const novaResposta = document.createElement("div");
    novaResposta.classList.add("multipla-resposta");
    novaResposta.style.display = "flex";
    novaResposta.style.alignItems = "center";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.classList.add("check");
    checkbox.name = "opcoesMultipla";

    const input = document.createElement("input");
    input.type = "text";
    input.placeholder = "Opção";
    input.classList.add("opcao-alternativa-multipla");
    input.name = `textoOpcaoMultipla[${contadoraMultipla}]`;
    contadoraMultipla += 1;

    const btnRemover = document.createElement("button");
    btnRemover.type = "button";
    btnRemover.textContent = "Remover opção";
    btnRemover.classList.add("remover-opcao");
    btnRemover.onclick = function () {
      novaResposta.remove();
    };

    novaResposta.appendChild(checkbox);
    novaResposta.appendChild(input);
    novaResposta.appendChild(btnRemover);
    container.appendChild(novaResposta);
  };

  const adicionarOpcoesBtn =
    multiplaContainer.querySelector(".adicionar-opcao");
  const multiplaRespostasDiv = multiplaContainer.querySelector(
    ".multipla-respostas"
  );

  adicionarOpcoesBtn.addEventListener("click", () => {
    adicionarOpcaoMultipla(multiplaRespostasDiv);
  });

  selectPerguntas.addEventListener("change", function () {
    let opcao = selectPerguntas.value;
    if (opcao == "Curta") {
      adicionarPerguntas(curta);
    }
    if (opcao == "Longa") {
      adicionarPerguntas(longa);
    }
    if (opcao == "Alternativas") {
      adicionarPerguntas(alternativas);
    }
    if (opcao == "Multipla") {
      adicionarPerguntas(multiplaContainer);
    }
    selectPerguntas.selectedIndex = 0;
  });

  formulario.addEventListener("submit", async function (event) {
    event.preventDefault();

    const perguntaCurta = document.querySelectorAll(".pergunta-curta");
    const perguntaLonga = document.querySelectorAll(".pergunta-longa");
    const perguntaAlternativas = document.querySelectorAll(
      ".pergunta-alternativas"
    );
    const perguntaMultipla = document.querySelectorAll(".pergunta-multipla");
    const opcaoAlternativa = document.querySelectorAll(".opcao-alternativa");
    const opcaoMultipla = document.querySelectorAll(
      ".opcao-alternativa-multipla"
    );

    if (curta.style.display !== "none" && perguntaCurta) {
      perguntaCurta.required = true;
    }

    if (longa.style.display !== "none" && perguntaLonga) {
      perguntaLonga.required = true;
    }

    if (alternativas.style.display !== "none" && perguntaAlternativas) {
      perguntaAlternativas.required = true;
    }

    if (multiplaContainer.style.display !== "none" && perguntaMultipla) {
      perguntaMultipla.required = true;
    }

    if (opcaoAlternativa) {
      opcaoAlternativa.required = true;
    }

    if (opcaoMultipla) {
      opcaoMultipla.required = true;
    }

    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
      if (value) {
        data[key] = value;
      }
    });

    const url = `/api/formulario`;
    const res = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const responseText = await res.text();

    let responseData;
    try {
      responseData = JSON.parse(responseText);
    } catch (error) {
      console.error("Erro ao parsear JSON:", error);
    }

    console.log(data)

    window.location.href = "/meus";
    contadoraMultipla = 0;
    contadoraAlternativa = 0;
  });

  if (excluirForm) {
    excluirForm.forEach((form) => {
      form.onsubmit = function (event) {
        if (!confirm("Você tem certeza que deseja excluir este formulário?")) {
          event.preventDefault();
        }
      };
    });
  }
});
