import { ThemeSwitch } from "../components/ThemeSwitch";

export function Header() {

    const handleDownload = () => {
        downloadDoc("pdf"); // el hook se encarga de obtener los objetos
    };

    return (
        <>
            <a className="home-button row-left gap5" href="/">
                <img src="/duck.png" alt="Logo" className="logo"/>
                <h1>Quack AI</h1>            
            </a>
            <div className="full-w row-right gap10">
                <ThemeSwitch />
            </div>
        </>
    );
}

export default Header;
