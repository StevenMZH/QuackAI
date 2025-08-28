import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";

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

    const formData = new FormData();
    formData.append("file", file);
  };

  return (
    <div className="rounded-lg text-center">
      <div
        {...getRootProps()}
        className={"p-6 cursor-pointer"}
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p className="home-txt">Drop the file...</p>
        ) : (
          <p className="home-txt">
            Drop a file here or click to select it
          </p>
        )}
      </div>

      {file && (
        <div className="mt-4">
          <p className="home-txt-small">Selected file: {file.name}</p>
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
  