import { useState } from 'react';
import { Plus, ShoppingBasket, MapPin, Package } from 'lucide-react';
import PageHeader from '../components/common/PageHeader.jsx';
import EmptyState from '../components/common/EmptyState.jsx';
import StatusNote from '../components/common/StatusNote.jsx';
import { useAppData } from '../context/AppDataContext.jsx';
export default function MarketplacePage(){
 const {listings,addListing,farms}=useAppData();const [show,setShow]=useState(false);const [form,setForm]=useState({produce:'',quantity:'',unit:'quintal',price:'',district:'',availableDate:'',farmId:''});
 const update=e=>setForm(f=>({...f,[e.target.name]:e.target.value}));
 const submit=e=>{e.preventDefault();addListing(form);setShow(false);setForm({produce:'',quantity:'',unit:'quintal',price:'',district:'',availableDate:'',farmId:''});};
 return <div className="module-content"><PageHeader title="Farmer marketplace" description="Prepare produce listings and organize the details buyers will need. Buyer discovery and transactions are not connected yet." action={<button className="btn-primary" onClick={()=>setShow(v=>!v)}><Plus size={17}/> Create listing</button>}/>
 <StatusNote>Listings created here are saved locally as drafts only. They are not published to real buyers, and no payment or order can be made in this prototype.</StatusNote>
 {show&&<div className="form-panel"><div className="panel-header"><h3>Produce listing details</h3><button className="text-button" onClick={()=>setShow(false)}>Close</button></div><form className="form-grid" onSubmit={submit}>
 <label className="field">Produce / crop<input required name="produce" value={form.produce} onChange={update} placeholder="e.g. Potato"/></label><label className="field">Quantity<input required type="number" min="0.01" step="any" name="quantity" value={form.quantity} onChange={update}/></label>
 <label className="field">Unit<select name="unit" value={form.unit} onChange={update}><option>quintal</option><option>kg</option><option>tonne</option><option>piece</option></select></label><label className="field">Asking price (₹ / unit)<input required type="number" min="0" step="0.01" name="price" value={form.price} onChange={update}/></label>
 <label className="field">District<input required name="district" value={form.district} onChange={update}/></label><label className="field">Available from<input type="date" name="availableDate" value={form.availableDate} onChange={update}/></label>
 <label className="field full">Associated farm<select name="farmId" value={form.farmId} onChange={update}><option value="">Select farm (optional)</option>{farms.map(f=><option key={f.id} value={f.id}>{f.name}</option>)}</select></label>
 <div className="form-actions full"><span className="form-hint">A buyer-facing listing requires server-side verification in a later phase.</span><button className="btn-primary">Save draft</button></div></form></div>}
 <div className="section-heading"><div><span className="eyebrow">YOUR INVENTORY</span><h2>Produce drafts</h2></div><span className="count-pill">{listings.length} drafts</span></div>
 {listings.length===0?<EmptyState title="No produce listings yet" description="Create a draft with crop, quantity, unit, asking price and availability details." action={<button className="btn-secondary" onClick={()=>setShow(true)}>Create first listing</button>}/>:<div className="listing-grid">{listings.map(l=><article className="listing-card" key={l.id}><div className="listing-icon"><Package size={22}/></div><div className="listing-info"><strong>{l.produce}</strong><span><MapPin size={13}/> {l.district}</span><p>{l.quantity} {l.unit} · ₹{Number(l.price).toLocaleString('en-IN')} / {l.unit}</p><small>{l.status}</small></div></article>)}</div>}</div>;
}
