export default function TaskList({ tasks, refresh }) {
  async function deleteTask(id) {
    await fetch("http://localhost:5000/tasks/" + id, {
      method: "DELETE",
    });

    refresh();
  }

  return (
    <div className="task-list">
      <h3>Task List</h3>

      {tasks.map((task) => (
        <div key={task.id} className="task-item">
          <div className="task-text">
            <span className="task-title">{task.title}</span>

            <span>{task.description}</span>
          </div>

          <button className="delete-btn" onClick={() => deleteTask(task.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}
