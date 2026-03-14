import { useEffect, useState } from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

export default function App() {
  const [tasks, setTasks] = useState([]);

  async function loadTasks() {
    const res = await fetch("http://localhost:5000/tasks");
    const data = await res.json();
    setTasks(data);
  }

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div className="container">
      <h1>Task Flow Node.js</h1>

      <TaskForm refresh={loadTasks} />
      <TaskList tasks={tasks} refresh={loadTasks} />
    </div>
  );
}
