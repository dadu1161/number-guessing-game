<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Number Guessing Game Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 400px;
      margin: 50px auto;
      padding: 20px;
      background-color: #f3f3f3;
      border-radius: 8px;
    }
    h1 {
      text-align: center;
      color: #2c3e50;
    }
    label {
      display: block;
      margin: 15px 0 5px;
      font-weight: bold;
    }
    input[type="number"],
    select {
      width: 100%;
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }
    button {
      margin-top: 20px;
      width: 100%;
      padding: 10px;
      background-color: #3498db;
      border: none;
      border-radius: 4px;
      color: white;
      font-weight: bold;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #2980b9;
    }
  </style>
</head>
<body>
  <h1>Number Guessing Game</h1>
  <form id="guessingForm">
    <label for="startNumber">Start Number:</label>
    <input type="number" id="startNumber" name="startNumber" required />

    <label for="endNumber">End Number:</label>
    <input type="number" id="endNumber" name="endNumber" required />

    <label for="difficulty">Choose Difficulty:</label>
    <select id="difficulty" name="difficulty" required>
      <option value="easy">Easy (5 tries)</option>
      <option value="medium" selected>Medium (3 tries)</option>
      <option value="hard">Hard (2 tries)</option>
    </select>

    <button type="submit">Start Game</button>
  </form>

  <script>
    document.getElementById('guessingForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const start = parseInt(document.getElementById('startNumber').value);
      const end = parseInt(document.getElementById('endNumber').value);
      const difficulty = document.getElementById('difficulty').value;

      if (start >= end) {
        alert("Start number must be less than end number.");
        return;
      }

      alert(`Game will start with range ${start} to ${end} on ${difficulty} difficulty.`);
      // Here you can add logic to start the game or send data to a backend
    });
  </script>
</body>
</html>
