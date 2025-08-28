import { useNavigate } from "react-router-dom";

export function SidePanel({children}) {
    const navigate = useNavigate();

    return (
        <div className="sidebar-container mobile full-view flex">
            <button className="full-view" onClick={() => navigate("/schedule")}>
            </button>            
            <div className="card">
                {children}
            </div>
        </div>
    );
}
export default SidePanel;
