import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import TaskResourceCell from "../features/SidePanel/TaskResourceCell";

export function Block() {
  const { id } = useParams(); 
  const [blockData, setBlockData] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("task_schedule");
    if (!saved) return;

    const schedule = JSON.parse(saved);
    const grid = schedule.schedule ?? [];

    let found = null;
    for (let b = 0; b < grid.length; b++) {
      for (let i = 0; i < grid[b].length; i++) {
        const cell = grid[b][i];
        cell.id = cell.id || `B${b + 1}-I${i + 1}`;
        if (cell.id === id) {
          found = cell;
          break;
        }
      }
      if (found) break;
    }

    setBlockData(found);
  }, [id]);

  if (!blockData) return <div>Loading block {id}...</div>;

  return (
    <div className="block-detail">
      <h2>Time Block {blockData.id}</h2>

      {/* Celdas separadas */}
      <TaskResourceCell type="Tasks" group={blockData.tasks ?? []} />
      <TaskResourceCell type="Resources" group={blockData.resources ?? []} />
    </div>
  );
}

export default Block;
