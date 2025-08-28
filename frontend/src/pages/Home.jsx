import FileUploader from "../features/csvParser/components/FileUploader"

export function Home() {
  return (
    <div className="home-container full-view flex card">
      <img src="home/schedule_img.svg" alt="home image" className="home-img"/>
      <FileUploader></FileUploader>
    </div>
  );
}


export default Home;


