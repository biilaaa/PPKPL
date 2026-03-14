const express = require("express");
const cors = require("cors");

const tasksRoute = require("./routes/tasks");

const app = express();

app.use(cors());
app.use(express.json());

app.use("/tasks", tasksRoute);

app.listen(5000, () => {
  console.log("Server running on http://localhost:5000");
});
