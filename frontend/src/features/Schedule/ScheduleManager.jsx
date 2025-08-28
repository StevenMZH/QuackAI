import { useState, useEffect } from "react";
import Schedule from "./Schedule";

export function ScheduleManager() {
  const [schedule, setSchedule] = useState(() => {
    const saved = localStorage.getItem("task_schedule");
    return saved ? JSON.parse(saved) : {};
  });

  useEffect(() => {
    if (schedule && Object.keys(schedule).length > 0) {
      localStorage.setItem("task_schedule", JSON.stringify(schedule));
    }
  }, [schedule]);

  const blocks = schedule.blocks ?? 0;
  const intervals = schedule.intervals ?? 0;
  const grid = schedule.schedule ?? [];

  return (
    <div className="full-view row gap5 scene-manager">
      <Schedule
        schedule={schedule}
        setSchedule={setSchedule}
        blocks={blocks}
        intervals={intervals}
        grid={grid}
      />
    </div>
  );
}

export default ScheduleManager;
