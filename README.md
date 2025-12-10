# CRUD de Perguntas

O sistema criado é um CRUD de perguntas, responsável por Adicionar, Listar, Atualizar e Excluir perguntas.  
É um tipo de programa muito útil para professores, estudantes e qualquer pessoa que precise organizar questões de forma prática.

Para utilizá-lo, basta digitar uma pergunta, adicionar as opções de resposta e definir qual delas é a correta. Depois disso, é só clicar em _Adicionar_, e a pergunta será salva no sistema, permitindo também editar ou excluir quando necessário.

Neste projeto foi utilizada a linguagem de programação _Python, desenvolvida na IDE \*\*VS Code_.

---

## Estrutura do Projeto

O projeto foi dividido em quatro arquivos:

- _main.py_
- _logica_crud.py_
- _interface_crud.py_
- _perguntas.json_

---

### logica_crud.py

Responsável pelas funções de lógica, como abrir o arquivo JSON, salvar os dados e manipular a lista de perguntas.

### interface_crud.py

Responsável pela interface visual do programa, cuidando da posição dos elementos, mensagens de texto, cores, botões, etc.

### main.py

Tem como objetivo integrar os outros dois arquivos mencionados acima, garantindo que o programa seja inicializado corretamente.

## Como executar o projeto

1. Certifique-se de que todos os arquivos estejam na mesma pasta:

   - main.py
   - logica_crud.py
   - interface_crud.py
   - perguntas.json (será criado automaticamente caso não exista)

2. Abra a pasta do projeto no VS Code.

3. Execute o arquivo principal:

   - Abra o arquivo _main.py_.
   - Clique em "Run" (Executar) ou pressione _F5_.

4. A interface do CRUD irá abrir automaticamente e você poderá adicionar, editar e excluir perguntas.
