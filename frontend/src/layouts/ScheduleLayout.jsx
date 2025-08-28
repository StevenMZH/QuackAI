import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'
import ScheduleDashboard from '../pages/Schedule'
import SidePanel from '../features/SidePanel/SidePanel'

export default function ScheduleLayout({sidebar}) {
  
    return (
    <>
      <header>
        <Header/>
      </header>
      
      <main className='full-view flex column'>
        <ScheduleDashboard/>

      </main>

      <SidePanel>
        <Outlet/>
      </SidePanel>

      <footer>
        <Footer/>
      </footer>
    </>
  )
}
