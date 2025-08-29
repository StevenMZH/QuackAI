export async function parseCsvFileToJson(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      let text = event.target.result;
      if (text.charCodeAt(0) === 0xFEFF) {
        text = text.slice(1);
      }

      const lines = text.split(/\r?\n/).filter(Boolean);
      if (lines.length === 0) return resolve({ tasks: [], resources: [] });

      const headers = lines[0].split(",").map(h => h.trim());
      const data = lines.slice(1).map(line => {
        const values = line.split(",");
        const obj = {};
        headers.forEach((header, idx) => {
          obj[header] = values[idx]?.trim() ?? "";
        });
        return obj;
      });

      const tasks = data
        .filter(d => d.type === "task")
        .map(d => ({
          name: d.name,
          time_blocks: Number(d.time_blocks) || 0,
          compatible_tags: d.compatible_tags
            ? d.compatible_tags.split(";").map(t => t.trim())
            : [],
          max_per_cicle: Number(d.max_per_cicle) || 0,
          max_per_interval: Number(d.max_per_interval) || 0,
        }));

      const resources = data
        .filter(d => d.type === "resource")
        .map(d => ({
          name: d.name,
          tags: d.tags ? d.tags.split(";").map(t => t.trim()) : [],
          max_per_cicle: Number(d.max_per_cicle) || 0,
          max_per_interval: Number(d.max_per_interval) || 0,
        }));

      resolve({ tasks, resources });
    };

    reader.onerror = reject;
    reader.readAsText(file, "UTF-8");
  });
}
