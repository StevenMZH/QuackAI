import { ThemeSwitch } from "../components/ThemeSwitch";

export function Header() {

    const handleDownload = () => {
        downloadDoc("pdf"); // el hook se encarga de obtener los objetos
    };

    return (
        <>
            <div className="full-w row-left gap5">
                <img src="duck.png" alt="Logo" className="logo"/>
                <h1>Quack AI</h1>            
            </div>
            <div className="full-w row-right gap10">
                <ThemeSwitch />
            </div>
            {/* {error && <p className="error-text">Error: {error.message}</p>} */}
        </>
    );
}

export default Header;
