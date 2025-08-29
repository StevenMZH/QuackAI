import { useState } from "react";
import { useSchedule } from "../hooks/useSchedule";

const ScheduleViewer = () => {
  const { scheduleData, loading, error, fetchSchedule } = useSchedule();
  const [blocks, setBlocks] = useState(2);
  const [intervals, setIntervals] = useState(5);

  const handleFetch = () => {
    const payload = {
      blocks,
      intervals,
      tasks: [
        { name: "T1", time_blocks: 3, compatible_tags: ["A", "C"], max_per_cicle: 5, max_per_interval: 2 },
        { name: "T2", time_blocks: 6, compatible_tags: ["B"], max_per_cicle: 7, max_per_interval: 3 },
        { name: "T3", time_blocks: 2, compatible_tags: ["D", "E", "A"], max_per_cicle: 4, max_per_interval: 1 },
        { name: "T4", time_blocks: 5, compatible_tags: ["C", "F"], max_per_cicle: 6, max_per_interval: 2 },
        { name: "T5", time_blocks: 1, compatible_tags: ["G", "B"], max_per_cicle: 3, max_per_interval: 1 },
      ],
      resources: [
        { name: "R1", tags: ["A", "C"], max_per_cicle: 6, max_per_interval: 2 },
        { name: "R2", tags: ["B"], max_per_cicle: 5, max_per_interval: 1 },
        { name: "R3", tags: ["D", "E"], max_per_cicle: 7, max_per_interval: 3 },
        { name: "R4", tags: ["F", "G", "C"], max_per_cicle: 8, max_per_interval: 2 },
      ],
    };

    fetchSchedule(payload);
  };

  if (loading) return <p>Cargando horario...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error.message}</p>;

  return (
    <div>
      <button onClick={handleFetch}>Generar Schedule</button>
      {scheduleData && (
        <pre style={{ whiteSpace: "pre-wrap" }}>
          {JSON.stringify(scheduleData, null, 2)}
        </pre>
      )}
    </div>
  );
};

export default ScheduleViewer;