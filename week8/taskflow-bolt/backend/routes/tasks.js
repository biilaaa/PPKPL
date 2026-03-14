const express = require("express");
const router = express.Router();
const db = require("../database/db");

router.get("/", (req, res) => {
  db.all("SELECT * FROM tasks", (err, rows) => {
    if (err) return res.status(500).send(err);
    res.json(rows);
  });
});

router.post("/", (req, res) => {
  const { title, description } = req.body;

  db.run(
    "INSERT INTO tasks (title, description) VALUES (?, ?)",
    [title, description],
    function (err) {
      if (err) return res.status(500).send(err);
      res.json({ id: this.lastID });
    },
  );
});

router.delete("/:id", (req, res) => {
  db.run("DELETE FROM tasks WHERE id=?", req.params.id, (err) => {
    if (err) return res.status(500).send(err);
    res.sendStatus(200);
  });
});

module.exports = router;
