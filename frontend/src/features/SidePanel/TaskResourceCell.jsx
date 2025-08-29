import { useNavigate } from "react-router-dom";

export function TaskResourceCell({ type, group = [], className = '' }) {
  const navigate = useNavigate();

  return (
    <div className="card task-resource-cell">
      <div className="group-title">{type}</div>
      <div className="resource-cell-container">
        {group.length > 0 ? (
          group.map((item, idx) => (
            <button
              key={idx}
              className={`resource-cell ${className}`}
              onClick={() =>
                navigate(
                  type === "Tasks"
                    ? `/schedule/task/${item}`
                    : `/schedule/resource/${item}`
                )
              }
            >
              {item}
            </button>
          ))
        ) : (
          <div>No {type}</div>
        )}
      </div>
    </div>
  );
}

export default TaskResourceCell;
