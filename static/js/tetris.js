
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('game-board');
    const context = canvas.getContext('2d');
    const scoreElement = document.getElementById('score');
    const startButton = document.getElementById('start-button');

    const COLS = 10;
    const ROWS = 20;
    const BLOCK_SIZE = 20;

    let board = [];
    let score = 0;
    let gameOver = false;

    function drawBoard() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        for (let r = 0; r < ROWS; r++) {
            for (let c = 0; c < COLS; c++) {
                if (board[r][c]) {
                    context.fillStyle = board[r][c] === 1 ? 'black' : 'blue';
                    context.fillRect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
                    context.strokeRect(c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
                }
            }
        }
    }

    function updateGameState(state) {
        board = state.board;
        score = state.score;
        gameOver = state.game_over;
        scoreElement.textContent = score;
        drawBoard();
        if (gameOver) {
            alert('Game Over!');
        }
    }

    async function startGame() {
        const response = await fetch('/start', { method: 'POST' });
        const data = await response.json();
        updateGameState(data);
    }

    async function move(direction) {
        if (gameOver) return;
        const response = await fetch('/move', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ direction })
        });
        const data = await response.json();
        updateGameState(data);
    }

    document.addEventListener('keydown', (event) => {
        switch (event.key) {
            case 'ArrowLeft':
                move('left');
                break;
            case 'ArrowRight':
                move('right');
                break;
            case 'ArrowDown':
                move('down');
                break;
            case 'ArrowUp':
                move('rotate');
                break;
        }
    });

    startButton.addEventListener('click', startGame);

    // Game loop
    setInterval(async () => {
        if (!gameOver) {
            await move('down');
        }
    }, 1000);

    // Initial fetch of the game state
    async function getInitialState() {
        const response = await fetch('/gamestate');
        const data = await response.json();
        updateGameState(data);
    }

    getInitialState();
});
