# Feature Implementation Plan: Botão de Pausa

## 📋 Todo Checklist
- [x] Adicionar o botão de pausa ao `index.html`
- [x] Estilizar o botão de pausa em `style.css`
- [x] Implementar a lógica de pausa/resumo em `tetris.js`
- [x] Exibir uma mensagem de "Pausado" na tela
- [x] Testar a funcionalidade de pausa

## 🔍 Analysis & Investigation

### Codebase Structure
O projeto é uma aplicação web Flask simples com uma clara separação de responsabilidades:
- `app.py`: Backend Flask que serve a página principal.
- `templates/index.html`: Estrutura HTML da página do jogo.
- `static/js/tetris.js`: Lógica principal do jogo Tetris.
- `static/css/style.css`: Estilização da página e do jogo.

### Current Architecture
A lógica do jogo está contida em `tetris.js` e é renderizada em um elemento `<canvas>` do HTML5. O jogo provavelmente opera em um loop principal (usando `requestAnimationFrame` ou `setInterval`) que atualiza o estado do jogo e o desenha na tela. A tarefa principal será identificar e controlar este loop.

### Dependencies & Integration Points
A nova funcionalidade exigirá a modificação de três arquivos:
1.  `templates/index.html`: Para adicionar o elemento do botão.
2.  `static/css/style.css`: Para estilizar o novo botão.
3.  `static/js/tetris.js`: Para implementar a lógica de pausa.

### Considerations & Challenges
- **Estado de Pausa**: Precisaremos de uma variável booleana (por exemplo, `isPaused`) para rastrear se o jogo está pausado ou não.
- **Game Loop**: O loop principal do jogo precisa ser modificado para não executar a lógica de atualização do jogo quando `isPaused` for `true`.
- **Feedback Visual**: É uma boa prática de UX mostrar uma indicação visual de que o jogo está pausado, como uma sobreposição ou texto na tela.

## 📝 Implementation Plan

### Prerequisites
Nenhum pré-requisito é necessário. Todas as alterações serão feitas nos arquivos existentes.

### Step-by-Step Implementation
1. **Adicionar o Botão de Pausa ao HTML**:
   - **Files to modify**: `templates/index.html`
   - **Changes needed**: Adicionar um elemento `<button>` abaixo do canvas do jogo.
     ```html
     ...
     <canvas id="tetris" width="240" height="400"></canvas>
     <div>
         <button id="pause-button">Pausar</button>
     </div>
     <script src="{{ url_for('static', filename='js/tetris.js') }}"></script>
     ...
     ```

2. **Estilizar o Botão de Pausa**:
   - **Files to modify**: `static/css/style.css`
   - **Changes needed**: Adicionar algumas regras de estilo básicas para o botão para que ele se pareça bom.
     ```css
     ...
     #pause-button {
         display: block;
         margin: 1rem auto;
         padding: 0.5rem 1rem;
         font-size: 1rem;
         cursor: pointer;
     }
     ```

3. **Implementar a Lógica de Pausa/Resumo**:
   - **Files to modify**: `static/js/tetris.js`
   - **Changes needed**:
     - Introduzir uma variável de estado `isPaused`.
     - Adicionar um ouvinte de evento ao botão de pausa.
     - Modificar o loop do jogo para respeitar o estado de pausa.
     - Desenhar uma mensagem de "Pausado" na tela.

     ```javascript
     // No topo do arquivo, com outras variáveis
     let isPaused = false;
     const pauseButton = document.getElementById('pause-button');

     // Adicionar ouvinte de evento
     pauseButton.addEventListener('click', () => {
         isPaused = !isPaused;
         pauseButton.textContent = isPaused ? 'Resumir' : 'Pausar';
         if (!isPaused) {
             update(); // Reinicia o loop do jogo se estava pausado
         }
     });

     // Encontre a função de loop principal (provavelmente chamada update ou similar)
     function update(time = 0) {
         if (isPaused) {
             // Desenha a mensagem de "Pausado"
             context.fillStyle = 'rgba(0, 0, 0, 0.5)';
             context.fillRect(0, 0, canvas.width, canvas.height);
             context.fillStyle = 'white';
             context.font = '30px Arial';
             context.textAlign = 'center';
             context.fillText('Pausado', canvas.width / 2, canvas.height / 2);
             return;
         }

         // ... (lógica de atualização do jogo existente) ...

         draw();
         requestAnimationFrame(update);
     }
     ```
     *(Nota: O código exato pode precisar de ajustes para se encaixar na estrutura existente de `tetris.js`)*

### Testing Strategy
1.  Abra o jogo no navegador.
2.  Clique no botão "Pausar". O jogo deve congelar e a mensagem "Pausado" deve aparecer.
3.  Enquanto estiver pausado, as peças não devem se mover.
4.  Clique no botão "Resumir". O jogo deve continuar de onde parou.
5.  Teste pausar e resumir em diferentes momentos do jogo para garantir a estabilidade.

## 🎯 Success Criteria
O recurso será considerado completo quando o usuário puder pausar e resumir o jogo a qualquer momento usando o botão "Pausar"/"Resumir", com um feedback visual claro indicando o estado de pausa.
