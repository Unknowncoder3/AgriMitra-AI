import { Navigate, Route, Routes } from 'react-router-dom';
import MainLayout from './components/layout/MainLayout.jsx';
import Dashboard from './pages/Dashboard.jsx';
import FarmsPage from './pages/FarmsPage.jsx';
import SoilPage from './pages/SoilPage.jsx';
import DiseasePage from './pages/DiseasePage.jsx';
import CropsPage from './pages/CropsPage.jsx';
import WeatherPage from './pages/WeatherPage.jsx';
import CalendarPage from './pages/CalendarPage.jsx';
import MarketplacePage from './pages/MarketplacePage.jsx';
import FinancePage from './pages/FinancePage.jsx';
import AssistantPage from './pages/AssistantPage.jsx';
import NotFoundPage from './pages/NotFoundPage.jsx';

export default function App() {
  return <Routes><Route element={<MainLayout/>}>
    <Route index element={<Dashboard/>}/>
    <Route path="farms" element={<FarmsPage/>}/>
    <Route path="soil" element={<SoilPage/>}/>
    <Route path="disease" element={<DiseasePage/>}/>
    <Route path="crops" element={<CropsPage/>}/>
    <Route path="weather" element={<WeatherPage/>}/>
    <Route path="calendar" element={<CalendarPage/>}/>
    <Route path="marketplace" element={<MarketplacePage/>}/>
    <Route path="finance" element={<FinancePage/>}/>
    <Route path="assistant" element={<AssistantPage/>}/>
    <Route path="*" element={<NotFoundPage/>}/>
  </Route></Routes>;
}
