import { useNavigate } from "react-router-dom";

export function TaskResourceCell({ task, resources = [], className = '' }) {
  const navigate = useNavigate();

  return (
    <div className="card task-resource-cell">
      <button
        className={`task-cell ${className}`}
        onClick={() => navigate(`/schedule/task/${task}`)}
      >
        {task}
      </button>

      <div className="resource-cell-container">
        {resources.length > 0 ? (
          resources.map((resource, idx) => (
            <button key={idx} className={`resource-cell ${className}`} onClick={() => navigate(`/schedule/resource/${resource}`)}>
              {resource}
            </button>
          ))
        ) : (
          <div>No resources</div>
        )}
      </div>
    </div>
  );
}

export default TaskResourceCell;
