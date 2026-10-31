import { Sprout } from 'lucide-react';
export default function EmptyState({ title, description, action }) {
  return <div className="empty-state-card"><div className="empty-state-icon"><Sprout size={24}/></div><strong>{title}</strong><p>{description}</p>{action}</div>;
}
