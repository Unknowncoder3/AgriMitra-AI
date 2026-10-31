import {ArrowUpRight} from 'lucide-react';
import {Link} from 'react-router-dom';
export default function QuickAction({title,description,icon:Icon,tone,to}){return <Link to={to} className="quick-action"><div className={`quick-action-icon ${tone}`}><Icon size={21}/></div><div><strong>{title}</strong><small>{description}</small></div><ArrowUpRight size={16} className="action-arrow"/></Link>}
