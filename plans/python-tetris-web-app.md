# Feature Implementation Plan: python-tetris-web-app

## 📋 Todo Checklist
- [x] Set up project structure
- [x] Implement core Tetris game logic in Python
- [x] Create the Flask web server
- [x] Develop the HTML/CSS for the game interface
- [x] Write the JavaScript for frontend logic and communication
- [x] Final Review and Testing

## 🔍 Analysis & Investigation

### Codebase Structure
Since this is a new project, I will propose a standard structure for a Flask application:
*   `app.py`: The main Flask application file containing the web server and game logic.
*   `static/`: A directory to store static files like CSS and JavaScript.
    *   `css/style.css`: For styling the web page.
    *   `js/tetris.js`: For frontend game logic and communication with the backend.
*   `templates/`: A directory to store HTML templates.
    *   `index.html`: The main page for the game.

### Current Architecture
There is no existing architecture. The proposed architecture is a simple client-server model:
*   **Backend (Flask):** A Python web server using the Flask framework will handle the core game logic and expose API endpoints for the frontend to interact with. It will run on port 8080.
*   **Frontend (HTML/CSS/JavaScript):** A single web page will render the game board using HTML and CSS. JavaScript will handle user input (keyboard events) and communicate with the Flask backend to update the game state.

### Dependencies & Integration Points
*   **Flask:** A lightweight Python web framework to build the web server.
*   No external services or APIs are required.

### Considerations & Challenges
*   **Real-time Gameplay:** To create a smooth experience, the frontend will need to update regularly. A simple approach is to have the JavaScript frontend poll the backend at a fixed interval (e.g., every 500ms) to get the latest game state.
*   **Game State Management:** The backend will maintain the game state (board, current piece, score) in memory. For a simple, single-player game, this is sufficient.
*   **Tetris Logic:** The core logic for piece movement, rotation, collision detection, and line clearing needs to be carefully implemented in Python to ensure the game works correctly.

## 📝 Implementation Plan

### Prerequisites
*   Install Python 3 on your system.
*   Install the Flask library: `pip install Flask`

### Step-by-Step Implementation
1.  **Step 1: Set up the Project Structure**
    *   Files to create:
        *   `app.py`
        *   `templates/index.html`
        *   `static/css/style.css`
        *   `static/js/tetris.js`
    *   Changes needed: Create the files and directories as described in the "Codebase Structure" section.

2.  **Step 2: Implement Core Tetris Logic (in `app.py`)**
    *   Files to modify: `app.py`
    *   Changes needed:
        *   Define the game board as a 2D list (e.g., 20 rows by 10 columns).
        *   Define the shapes of the Tetris pieces (tetrominoes) as lists of coordinates.
        *   Implement functions to:
            *   Create a new random piece at the top of the board.
            *   Handle piece movement (left, right, down).
            *   Handle piece rotation.
            *   Check for collisions with the board boundaries and other pieces.
            *   Lock a piece in place when it lands.
            *   Check for and clear completed lines, updating the score.
            *   Detect when the game is over.

3.  **Step 3: Create the Flask Web Server (in `app.py`)**
    *   Files to modify: `app.py`
    *   Changes needed:
        *   Import `Flask` and `jsonify`.
        *   Initialize the Flask application.
        *   Create a main route `/` that renders the `index.html` template.
        *   Create API endpoints:
            *   `POST /start`: Resets the game state and starts a new game.
            *   `GET /gamestate`: Returns the current game state (board, score, game over status) as a JSON object.
            *   `POST /move`: Takes a move (e.g., 'left', 'right', 'rotate') from the frontend, updates the game state, and returns the new state.
        *   Add the code to run the app on port 8080.

4.  **Step 4: Build the Frontend (HTML and CSS)**
    *   Files to modify: `templates/index.html`, `static/css/style.css`
    *   Changes needed:
        *   In `index.html`, create the basic page structure with a title, a `<div>` or `<canvas>` for the game board, and elements to display the score.
        *   Link the `style.css` and `tetris.js` files.
        *   In `style.css`, add basic styling to center the game board and make it look like a Tetris grid.

5.  **Step 5: Implement Frontend Logic (JavaScript)**
    *   Files to modify: `static/js/tetris.js`
    *   Changes needed:
        *   Write a function to draw the game board and pieces based on the data received from the `/gamestate` endpoint.
        *   Add an event listener for keyboard presses (`keydown`) to capture user input (arrow keys).
        *   When a key is pressed, send a `POST` request to the `/move` endpoint with the corresponding action.
        *   Use `setInterval` to create a game loop that calls a function to fetch the game state from `/gamestate` and redraw the board periodically.
        *   Add a "Start Game" button that sends a `POST` request to the `/start` endpoint.

### Testing Strategy
*   **Backend:** Manually test the API endpoints using a tool like `curl` or by writing simple Python scripts to ensure they respond correctly.
*   **Frontend:** Open the `index.html` page in a web browser.
    *   Verify that the game board renders correctly.
    *   Click the "Start Game" button and check if a new game begins.
    *   Use the arrow keys to move and rotate the pieces and confirm the display updates.
    *   Play the game to ensure line clearing, scoring, and the "game over" condition work as expected.

## 🎯 Success Criteria
*   The Python application starts without errors and listens for requests on port 8080.
*   Navigating to `http://localhost:8080` in a web browser displays the Tetris game.
*   The game is fully playable in the browser, with user controls, scoring, and a game over state.
