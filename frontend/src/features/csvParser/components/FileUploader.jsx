import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { parseCsvFileToJson } from "../helpers/parser";
import { useSchedule } from "../../../hooks/useSchedule";
import { useNavigate } from "react-router-dom";

const FileUploader = () => {
  const [file, setFile] = useState(null);
  const [intervals, setIntervals] = useState('');
  const [blocks, setBlocks] = useState('');
  const { scheduleData, loading, error, fetchSchedule } = useSchedule();
  const navigate = useNavigate();

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    multiple: false, 
  });

  const handleUpload = async () => {
    if (!file) return alert("Select a file first");
    if (!blocks || !intervals) return alert("Please provide both blocks and intervals");
    const jsonData = await parseCsvFileToJson(file);
    
    const payload = {
      blocks: Number(blocks),
      intervals: Number(intervals),
      tasks: jsonData.tasks,
      resources: jsonData.resources,
    };

    const data = await fetchSchedule(payload);
    if(data) {
      localStorage.setItem('task_schedule', JSON.stringify(data));
      navigate('/schedule');
    } else {
      console.error(error);
    }
    
  };

  return (
    <div className="rounded-lg text-center">
      <div
        {...getRootProps()}
        className={"p-6 cursor-pointer border-dashed border-2 rounded-lg"}
      >
        <input {...getInputProps()} />
        <p
          className={`home-txt-small${isDragActive ? ' text-white' : ''}`}
          style={{minHeight: '1.5em'}}
        >
          Drop a file here or click to select it
        </p>
      </div>

      {file && (
        <div className="mt-4 flex column">
          <p className="file-name-txt">Selected file: {file.name}</p>
          <div className="flex gap10 mt-4 custom-width">
            <div className="full-w">
              <input 
              type="number" 
              min={1}
              placeholder="Blocks per interval"
              onChange={(e) => setBlocks(e.target.value)}
              />
            </div>
            <div className="full-w">
              <input 
              type="number" 
              min={1}
              placeholder="Intervals per cycle"
              onChange={(e) => setIntervals(e.target.value)}
              />
            </div>
          </div>
          <button
            onClick={handleUpload}
            className="mt-4 px-4 py-2 upload-button hover:bg-blue-700"
          >
            Generate Schedule
          </button>
        </div>
      )}
    </div>
  );
};

export default FileUploader;
  