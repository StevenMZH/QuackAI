export async function parseCsvFileToJson(file) {
	return new Promise((resolve, reject) => {
		const reader = new FileReader();
		reader.onload = (event) => {
			let text = event.target.result;
			if (text.charCodeAt(0) === 0xFEFF) {
				text = text.slice(1);
			}
			const lines = text.split(/\r?\n/).filter(Boolean);
			if (lines.length === 0) return resolve([]);
			const headers = lines[0].split(',');
			const data = lines.slice(1).map(line => {
				const values = line.split(',');
				const obj = {};
				headers.forEach((header, idx) => {
					obj[header.trim()] = values[idx]?.trim() ?? '';
				});
				return obj;
			});
			resolve(data);
		};
		reader.onerror = reject;
		reader.readAsText(file, 'UTF-8');
	});
}
