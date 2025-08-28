import { Routes, Route, Navigate } from "react-router-dom";
import { Suspense, lazy } from "react";
import { useMediaQuery } from "react-responsive";

import MainLayout from "./layouts/MainLayout";
import MobileLayout from "./layouts/MobileLayout";
import ScheduleLayout from "./layouts/ScheduleLayout";
import ScheduleDashboard from "./pages/Schedule";
import Block from "./pages/Block";
import Task from "./pages/Task";
import Resource from "./pages/Resource";


const Home = lazy(() => import("./pages/Home"));

function App() {
  const isMobile = useMediaQuery({ maxWidth: 768 });
  const Layout = isMobile ? MobileLayout : MainLayout;

  return (
    <Routes>
      <Route element={<Layout />}> 
        <Route path="/" element={ <Suspense fallback={<div></div>}>
          <Home />
        </Suspense>}/> 
        
        <Route path="/schedule" element={ <Suspense fallback={<div></div>}>
          <ScheduleDashboard />
        </Suspense>} />
      </Route>

      {/* Sidebar */}
      <Route path="/schedule/block" element={<ScheduleLayout />}>
        <Route path=":id" element={<Block/>} />
      </Route>
      <Route path="/schedule/task" element={<ScheduleLayout />}>
        <Route path=":id" element={<Task/>} />
      </Route>
      <Route path="/schedule/resource" element={<ScheduleLayout />}>
        <Route path=":id" element={<Resource/>} />
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

export default App;
