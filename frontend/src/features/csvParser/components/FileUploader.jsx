import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { parseCsvFileToJson } from "../helpers/parser";

const FileUploader = () => {
  const [file, setFile] = useState(null);

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
    const jsonData = await parseCsvFileToJson(file);
    
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
        <div className="mt-4">
          <p className="home-txt-small">Selected file: {file.name}</p>
          <div>
            
          </div>
          <button
            onClick={handleUpload}
            className="mt-2 px-4 py-2 upload-button hover:bg-blue-700"
          >
            Upload File
          </button>
        </div>
      )}
    </div>
  );
};

export default FileUploader;
  