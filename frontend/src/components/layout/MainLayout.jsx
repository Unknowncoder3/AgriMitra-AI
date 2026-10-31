import {useState} from 'react';
import {Outlet} from 'react-router-dom';
import Sidebar from './Sidebar.jsx';
import Topbar from './Topbar.jsx';
export default function MainLayout(){const[sidebarOpen,setSidebarOpen]=useState(false);return <div className="app-shell"><Sidebar open={sidebarOpen} onClose={()=>setSidebarOpen(false)}/><main className="main-content"><Topbar onMenuClick={()=>setSidebarOpen(true)}/><div className="page-container"><Outlet/></div></main>{sidebarOpen&&<button aria-label="Close navigation" className="sidebar-backdrop" onClick={()=>setSidebarOpen(false)}/>}</div>}
