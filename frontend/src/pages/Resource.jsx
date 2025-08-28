import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";

export function Resource() {
  const { id } = useParams(); // nombre del recurso (ej. "R1")
  const [schedule, setSchedule] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("task_schedule");
    if (!saved) return;

    const parsed = JSON.parse(saved);
    setSchedule(parsed);
  }, []);

  if (!schedule) return <div>Loading resource {id}...</div>;

  const blocks = schedule.blocks ?? 0;
  const intervals = schedule.intervals ?? 0;
  const grid = schedule.schedule ?? [];

  return (
    <div className="task-details">
      <h2>Resource {id}</h2>

      <div className="task-schedule-grid">
        <div
          className="task-schedule-grid"
          style={{
            display: "grid",
            gridTemplateColumns: `repeat(${intervals}, 1fr)`,
          }}
        >
          {Array.from({ length: blocks }).map((_, bIndex) =>
            Array.from({ length: intervals }).map((_, iIndex) => {
              const cell = grid[bIndex]?.[iIndex] ?? { tasks: [], resources: [] };
              const cellId = `B${bIndex + 1}-I${iIndex + 1}`;
              const isAssigned = cell.resources?.includes(id);

              return (
                <div
                  key={cellId}
                  className={`grid-cell ${isAssigned ? "assigned" : ""}`}
                ></div>
              );
            })
          )}
        </div>
      </div>
    </div>
  );
}

export default Resource;
