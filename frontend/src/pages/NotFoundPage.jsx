import { Link } from 'react-router-dom';
export default function NotFoundPage(){return <div className="not-found"><span className="eyebrow">PAGE NOT FOUND</span><h1>We couldn't find that page.</h1><p>Return to your farm workspace.</p><Link className="btn-primary" to="/">Back to dashboard</Link></div>}
