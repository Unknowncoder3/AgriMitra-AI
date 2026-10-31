import { useMemo, useState } from 'react';
import { Sprout, SlidersHorizontal, Leaf } from 'lucide-react';
import PageHeader from '../components/common/PageHeader.jsx';
import StatusNote from '../components/common/StatusNote.jsx';

const cropGuide=[
 {name:'Aman rice',season:'Kharif',water:'High',soil:'Alluvial / clay loam',note:'Common monsoon-season crop; local variety and sowing window matter.'},
 {name:'Mustard',season:'Rabi',water:'Low to moderate',soil:'Well-drained loam',note:'Often considered after kharif harvest where temperature and moisture suit the variety.'},
 {name:'Potato',season:'Rabi',water:'Moderate',soil:'Loose, well-drained loam',note:'Requires healthy seed tubers, disease management and reliable market planning.'},
 {name:'Lentil',season:'Rabi',water:'Low',soil:'Well-drained loam',note:'Can fit selected rotations; waterlogging and local variety suitability need checking.'},
 {name:'Jute',season:'Kharif',water:'Moderate to high',soil:'Alluvial',note:'A traditional regional crop; retting water and market access are important.'},
 {name:'Vegetables',season:'Season-dependent',water:'Moderate',soil:'Depends on crop',note:'Choose a specific vegetable and plan perishability, labor and buyer access.'}
];
export default function CropsPage(){
 const [season,setSeason]=useState('All'),[water,setWater]=useState('All'),[query,setQuery]=useState('');
 const results=useMemo(()=>cropGuide.filter(c=>(season==='All'||c.season===season)&&(water==='All'||c.water===water)&&c.name.toLowerCase().includes(query.toLowerCase())),[season,water,query]);
 return <div className="module-content"><PageHeader title="Crop recommendations" description="Explore a regional crop-planning guide. Personalized AI ranking will arrive after soil, weather and market data are connected."/>
 <StatusNote>These are general planning notes, not personalized recommendations or a profitability prediction. Confirm variety, sowing window and practices with local agricultural extension guidance.</StatusNote>
 <div className="filter-panel"><div className="filter-title"><SlidersHorizontal size={18}/><strong>Explore crop options</strong></div><div className="filter-grid"><label className="field">Season<select value={season} onChange={e=>setSeason(e.target.value)}><option>All</option><option>Kharif</option><option>Rabi</option><option>Season-dependent</option></select></label><label className="field">Water need<select value={water} onChange={e=>setWater(e.target.value)}><option>All</option><option>Low</option><option>Low to moderate</option><option>Moderate</option><option>Moderate to high</option><option>High</option></select></label><label className="field">Search crop<input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search by crop name"/></label></div></div>
 <div className="crop-guide-grid">{results.map((c,i)=><article className="crop-guide-card" key={c.name}><div className="crop-guide-top"><div className="crop-icon"><Leaf size={21}/></div><span>GENERAL GUIDE</span></div><h3>{c.name}</h3><div className="crop-tags"><span>{c.season}</span><span>{c.water} water</span></div><p>{c.note}</p><div className="crop-meta"><span>Typical soil context</span><strong>{c.soil}</strong></div></article>)}</div>
 {results.length===0&&<div className="empty-state-card"><strong>No matching crops</strong><p>Try changing your filters.</p></div>}
 <div className="next-step-banner"><Sprout size={22}/><div><strong>Want a recommendation for your own field?</strong><p>Add a farm and a soil test first. The personalized recommendation engine is part of the AI integration phase.</p></div></div></div>;
}
