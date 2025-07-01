<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Number Guessing Game - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 700px;
            margin: 40px auto;
            padding: 0 20px;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: monospace;
        }
        hr {
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <h1>Number Guessing Game</h1>

    <p>A simple Python console game where the player tries to guess a randomly generated number within a certain number of tries based on difficulty.</p>

    <h2>How to Play</h2>
    <ol>
        <li>Run the Python script.</li>
        <li>Enter the start and end numbers to define the range.</li>
        <li>Choose a difficulty level:
            <ul>
                <li><strong>easy</strong> — 5 tries</li>
                <li><strong>medium</strong> — 3 tries (default)</li>
                <li><strong>hard</strong> — 2 tries</li>
            </ul>
        </li>
        <li>Try to guess the number within the allowed attempts.</li>
        <li>The game will tell you if your guess is correct or how many attempts you have left.</li>
    </ol>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
    </ul>

    <h2>How to Run</h2>
    <p>Run the script in your terminal or command prompt:</p>
    <pre><code>python guessing_game.py</code></pre>

    <h2>Features</h2>
    <ul>
        <li>Input validation for numbers.</li>
        <li>Different difficulty levels with varying number of tries.</li>
        <li>Clear prompts and feedback messages.</li>
    </ul>

    <hr />
    <p>Enjoy the game!</p>
</body>
</html>
