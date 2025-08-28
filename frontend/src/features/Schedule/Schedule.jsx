import ScheduleCell from "./ScheduleCell";

export function Schedule({ blocks, intervals, grid, className = "" }) {
  return (
    <div className={`card scene ${className}`}>
      <div
        className="schedule-grid grid"
        style={{
          gridTemplateColumns: `repeat(${intervals}, 1fr)`,
          gap: "2px",
        }}
      >
        {Array.from({ length: blocks }).map((_, blockIdx) =>
          Array.from({ length: intervals }).map((_, intervalIdx) => {
            const cell = grid[blockIdx]?.[intervalIdx] ?? { tasks: [], resources: [] };
            return (
              <ScheduleCell
                key={`${blockIdx}-${intervalIdx}`}
                id={`B${blockIdx + 1}-I${intervalIdx + 1}`}
                tasks={cell.tasks}
                resources={cell.resources}
              />
            );
          })
        )}
      </div>
    </div>
  );
}

export default Schedule;
