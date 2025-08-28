import { useNavigate } from "react-router-dom";

export function ScheduleCell({ id, tasks, resources, children, className = '' }) {
  const navigate = useNavigate();

  return (
    <button className={`schedule-cell ${className}`} onClick={() => navigate(`/schedule/block/${id}`)} >
      <div className="cell-id hl1">{id}</div>
      
      <div className="cell-data">  
        <div className="cell-tasks">
          {tasks && <div>T: {tasks.join(", ")}</div>}
        </div>
        
        <div className="cell-resources">
          {resources && <div>R: {resources.join(", ")}</div>}
        </div>
        
        {children}
      </div>
    </button>
  );
}

export default ScheduleCell;
