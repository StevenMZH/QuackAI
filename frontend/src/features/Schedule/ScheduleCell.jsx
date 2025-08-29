import { useNavigate } from "react-router-dom";

export function ScheduleCell({ id, tasks = [], resources = [], children, className = '' }) {
  const navigate = useNavigate();

  return (
    <button
      className={`schedule-cell ${className}`}
      onClick={() => navigate(`/schedule/block/${id}`)}
    >
      <div className="cell-id hl1"><div>{id}</div></div>

      <div className="cell-data">
          <div className="cell-tasks">
            {tasks.length > 0 && <div>T: {tasks.join(", ")}</div>}
          </div>
          <div className="cell-resources">
            {resources.length > 0 && <div>R: {resources.join(", ")}</div>}
          </div>
        {children}
      </div>
      
      {tasks.length > 0 && (<div className="cell-mobile">
        <div>{tasks.length}</div>
      </div>)}

    </button>
  );
}

export default ScheduleCell;
