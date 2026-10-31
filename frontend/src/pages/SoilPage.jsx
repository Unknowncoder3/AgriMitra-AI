import { useState } from 'react';
import { FlaskConical, Plus, FileText } from 'lucide-react';
import PageHeader from '../components/common/PageHeader.jsx';
import EmptyState from '../components/common/EmptyState.jsx';
import StatusNote from '../components/common/StatusNote.jsx';
import { useAppData } from '../context/AppDataContext.jsx';

export default function SoilPage(){
 const {farms,soilSamples,addSoilSample}=useAppData();
 const [form,setForm]=useState({farmId:'',sampleDate:new Date().toISOString().slice(0,10),ph:'',nitrogen:'',phosphorus:'',potassium:'',organicCarbon:'',source:'Manual entry'});
 const [show,setShow]=useState(false);
 const update=e=>setForm(f=>({...f,[e.target.name]:e.target.value}));
 const submit=e=>{e.preventDefault();addSoilSample(form);setShow(false);setForm(f=>({...f,ph:'',nitrogen:'',phosphorus:'',potassium:'',organicCarbon:''}));};
 return <div className="module-content"><PageHeader title="Soil intelligence" description="Record measured soil-test values and keep a history for each farm." action={<button className="btn-primary" onClick={()=>setShow(v=>!v)}><Plus size={17}/> Add soil test</button>}/>
 <StatusNote>Enter values from a soil laboratory report where possible. This prototype does not diagnose nutrient levels or calculate fertilizer doses.</StatusNote>
 {farms.length===0 && <StatusNote tone="warning">Create a farm profile first so soil samples can be linked to a location.</StatusNote>}
 {show && <div className="form-panel"><div className="panel-header"><div><span className="eyebrow">SOIL SAMPLE</span><h3>Measured parameters</h3></div><button className="text-button" onClick={()=>setShow(false)}>Close</button></div><form className="form-grid" onSubmit={submit}>
 <label className="field full">Farm<select required name="farmId" value={form.farmId} onChange={update}><option value="">Choose a farm</option>{farms.map(f=><option key={f.id} value={f.id}>{f.name} — {f.district}</option>)}</select></label>
 <label className="field">Sample date<input required type="date" name="sampleDate" value={form.sampleDate} onChange={update}/></label>
 <label className="field">Source<select name="source" value={form.source} onChange={update}><option>Manual entry</option><option>Laboratory report</option></select></label>
 {['ph','nitrogen','phosphorus','potassium','organicCarbon'].map(k=><label className="field" key={k}>{({ph:'pH',nitrogen:'Nitrogen (unit from report)',phosphorus:'Phosphorus (unit from report)',potassium:'Potassium (unit from report)',organicCarbon:'Organic carbon (unit from report)'})[k]}<input type="number" step="any" name={k} value={form[k]} onChange={update} placeholder="Optional"/></label>)}
 <div className="form-actions full"><span className="form-hint">Keep the original report and units for accurate interpretation.</span><button className="btn-primary" type="submit" disabled={!farms.length}>Save sample</button></div>
 </form></div>}
 <div className="section-heading"><div><span className="eyebrow">SOIL HISTORY</span><h2>Recorded samples</h2></div><span className="count-pill">{soilSamples.length} samples</span></div>
 {soilSamples.length===0?<EmptyState title="No soil samples recorded" description="Add results from a soil test report. Leave unknown parameters blank rather than guessing." action={<button className="btn-secondary" onClick={()=>setShow(true)} disabled={!farms.length}>Record soil test</button>}/>:<div className="data-card-list">{soilSamples.map(s=><article className="data-card" key={s.id}><div className="data-card-icon"><FlaskConical size={20}/></div><div className="data-card-main"><strong>{farms.find(f=>f.id===s.farmId)?.name || 'Farm record'}</strong><span>{s.sampleDate} · {s.source}</span><div className="parameter-chips">{[['pH',s.ph],['N',s.nitrogen],['P',s.phosphorus],['K',s.potassium],['Organic C',s.organicCarbon]].filter(x=>x[1]!==''&&x[1]!=null).map(([k,v])=><span key={k}>{k}: {v}</span>)}</div></div><FileText size={18} className="muted-icon"/></article>)}</div>}
 <p className="footnote">Values are stored as entered. Units and lab methods should be captured explicitly before production agronomic interpretation.</p></div>;
}
