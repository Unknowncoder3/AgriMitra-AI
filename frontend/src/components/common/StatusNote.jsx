import { Info } from 'lucide-react';
export default function StatusNote({ children, tone='info' }) { return <div className={`status-note ${tone}`}><Info size={17}/><span>{children}</span></div>; }
