"use client";

import { useState } from "react";

export default function Home() {
  const [tasks, setTasks] = useState<any[]>([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  function addTask() {
    const newTask = {
      id: Date.now(),
      title,
      description,
    };

    setTasks([...tasks, newTask]);

    setTitle("");
    setDescription("");
  }

  function deleteTask(id: number) {
    setTasks(tasks.filter((task) => task.id !== id));
  }

  return (
    <div className="container">
      <h1>Task Flow Next.js</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          placeholder="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          placeholder="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <button onClick={addTask}>Add</button>
      </div>

      <h3>Task List</h3>

      {tasks.map((task) => (
        <div
          key={task.id}
          style={{
            display: "flex",
            justifyContent: "space-between",
            background: "#f3f3f3",
            padding: "10px",
            marginTop: "8px",
          }}
        >
          <div>
            <b>{task.title}</b>
            <br />
            {task.description}
          </div>

          <button onClick={() => deleteTask(task.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
