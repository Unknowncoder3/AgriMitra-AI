import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar.jsx';
import Topbar from './Topbar.jsx';

export default function MainLayout(){
 const [sidebarOpen,setSidebarOpen]=useState(false);
 const [theme,setTheme]=useState(()=>localStorage.getItem('agrimitra.theme')||'light');
 const toggleTheme=()=>setTheme(current=>{const next=current==='light'?'dark':'light';localStorage.setItem('agrimitra.theme',next);return next;});
 return <div className="app-shell" data-theme={theme}><Sidebar open={sidebarOpen} onClose={()=>setSidebarOpen(false)}/><main className="main-content"><Topbar onMenuClick={()=>setSidebarOpen(true)} theme={theme} onToggleTheme={toggleTheme}/><div className="page-container"><Outlet/></div></main>{sidebarOpen&&<button aria-label="Close navigation" className="sidebar-backdrop" onClick={()=>setSidebarOpen(false)}/>}</div>;
}
