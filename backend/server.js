
const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

let users = [{ username: 'admin', password: 'password' }];
let todos = [];
let currentId = 1;

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username && u.password === password);
  if (user) res.json({ success: true });
  else res.status(401).json({ success: false, message: 'Invalid credentials' });
});

app.get('/todos', (req, res) => {
  res.json(todos);
});

app.post('/todos', (req, res) => {
  const todo = { id: currentId++, text: req.body.text };
  todos.push(todo);
  res.status(201).json(todo);
});

app.put('/todos/:id', (req, res) => {
  const todo = todos.find(t => t.id === parseInt(req.params.id));
  if (todo) {
    todo.text = req.body.text;
    res.json(todo);
  } else res.status(404).json({ message: 'Not found' });
});

app.delete('/todos/:id', (req, res) => {
  todos = todos.filter(t => t.id !== parseInt(req.params.id));
  res.status(204).send();
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
