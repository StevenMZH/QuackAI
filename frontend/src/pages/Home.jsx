import FileUploader from "../features/csvParser/components/FileUploader"

export function Home() {
  return (
    <div className="home-container full-view flex card">
      <FileUploader></FileUploader>
    </div>
  );
}


export default Home;


