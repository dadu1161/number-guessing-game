<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Number Guessing Game Form</title>
</head>
<body>
  <h1>Number Guessing Game</h1>
  <form>
    <label for="startNumber">Start Number:</label><br />
    <input type="number" id="startNumber" name="startNumber" required /><br /><br />

    <label for="endNumber">End Number:</label><br />
    <input type="number" id="endNumber" name="endNumber" required /><br /><br />

    <label for="difficulty">Choose Difficulty:</label><br />
    <select id="difficulty" name="difficulty" required>
      <option value="easy">Easy (5 tries)</option>
      <option value="medium" selected>Medium (3 tries)</option>
      <option value="hard">Hard (2 tries)</option>
    </select><br /><br />

    <button type="submit">Start Game</button>
  </form>
</body>
</html>
