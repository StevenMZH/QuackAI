export function ScheduleCell({ id, tasks, resources, children, className = '', }) {
  return (
    <div className={`schedule-cell ${className}`}>
      <div className="cell-id hl1">{id}</div>
      <div className="cell-data">
        <div className="cell-tasks"> {tasks && (<div>T: {tasks.join(", ")}</div>)} </div>
        <div className="cell-resources"> {resources && (<div>R: {resources.join(", ")}</div>)} </div>
        {children}
      </div>
    </div>
  );
}
export default ScheduleCell;