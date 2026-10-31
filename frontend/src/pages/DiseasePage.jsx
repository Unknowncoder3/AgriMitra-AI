import { useRef, useState } from 'react';
import { Camera, ImagePlus, ShieldAlert, UploadCloud } from 'lucide-react';
import PageHeader from '../components/common/PageHeader.jsx';
import EmptyState from '../components/common/EmptyState.jsx';
import StatusNote from '../components/common/StatusNote.jsx';
import { useAppData } from '../context/AppDataContext.jsx';
export default function DiseasePage(){
 const {farms,diseaseCases,addDiseaseCase}=useAppData();
 const [file,setFile]=useState(null),[preview,setPreview]=useState(''),[crop,setCrop]=useState(''),[farmId,setFarmId]=useState(''),[symptoms,setSymptoms]=useState('');
 const input=useRef(null);
 const choose=e=>{const f=e.target.files?.[0];if(!f)return;if(!f.type.startsWith('image/'))return alert('Please select an image file.');if(f.size>8*1024*1024)return alert('Image must be smaller than 8 MB.');setFile(f);setPreview(URL.createObjectURL(f))};
 const submit=e=>{e.preventDefault();if(!file)return;addDiseaseCase({crop,farmId,symptoms,fileName:file.name});setFile(null);setPreview('');setCrop('');setSymptoms('');if(input.current)input.current.value=''};
 return <div className="module-content"><PageHeader title="Crop disease screening" description="Prepare a crop case with a clear photograph and context for a future AI screening and expert-review workflow."/>
 <StatusNote tone="warning"><strong>No diagnosis is generated.</strong> This page records case details and the selected filename locally. The image itself is not uploaded or retained, and no prediction is produced.</StatusNote>
 <div className="split-layout"><section className="form-panel upload-panel"><div className="panel-header"><div><span className="eyebrow">NEW DISEASE CASE</span><h3>Choose crop photograph</h3></div><Camera size={21}/></div><form onSubmit={submit}>
 <button type="button" className="upload-dropzone" onClick={()=>input.current?.click()}><input ref={input} type="file" accept="image/*" hidden onChange={choose}/>{preview?<img src={preview} alt="Selected crop preview"/>:<><div className="upload-icon"><ImagePlus size={27}/></div><strong>Choose a crop image</strong><span>JPG, PNG or WEBP · Maximum 8 MB</span><small><UploadCloud size={14}/> Browse files</small></>}</button>
 <label className="field">Crop type<input value={crop} onChange={e=>setCrop(e.target.value)} placeholder="e.g. Paddy, potato, tomato" required/></label><label className="field">Farm (optional)<select value={farmId} onChange={e=>setFarmId(e.target.value)}><option value="">Choose farm</option>{farms.map(f=><option key={f.id} value={f.id}>{f.name}</option>)}</select></label><label className="field">What are you observing?<textarea rows="3" value={symptoms} onChange={e=>setSymptoms(e.target.value)} placeholder="Describe visible spots, wilting, discoloration or when symptoms began."/></label><button className="btn-primary full-button" disabled={!file}>Save case details</button></form></section>
 <aside className="guidance-card"><div className="guidance-icon"><ShieldAlert size={22}/></div><h3>Take a useful photograph</h3><ul><li>Photograph the affected leaf or plant in natural light.</li><li>Include both healthy and affected areas if possible.</li><li>Avoid heavy blur, shadows and filters.</li><li>For widespread symptoms, capture more than one plant.</li></ul><p>For rapidly spreading disease or severe crop damage, contact a local agricultural extension officer or KVK promptly.</p></aside></div>
 <div className="section-heading"><div><span className="eyebrow">CASE HISTORY</span><h2>Your submissions</h2></div><span className="count-pill">{diseaseCases.length} cases</span></div>
 {diseaseCases.length===0?<EmptyState title="No cases submitted" description="Your submitted crop case details will appear here."/>:<div className="case-grid">{diseaseCases.map(c=><article className="case-card" key={c.id}><div><strong>{c.crop}</strong><span>{new Date(c.createdAt).toLocaleString()} · {c.fileName}</span><p>{c.symptoms||'No symptom notes added.'}</p><small className="pending-label">{c.status}</small></div></article>)}</div>}</div>
}
