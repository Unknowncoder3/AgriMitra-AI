import { createContext, useContext, useEffect, useMemo, useState } from 'react';
const AppDataContext=createContext(null);
const KEY='agrimitra.frontend.v1';
const initial={farms:[],soilSamples:[],diseaseCases:[],tasks:[],listings:[],expenses:[],harvests:[]};
function load(){try{return {...initial,...JSON.parse(localStorage.getItem(KEY)||'{}')}}catch{return initial}}
export function AppDataProvider({children}){
 const [data,setData]=useState(load);
 useEffect(()=>{localStorage.setItem(KEY,JSON.stringify(data))},[data]);
 const api=useMemo(()=>({
  ...data,
  addFarm:item=>setData(d=>({...d,farms:[{...item,id:crypto.randomUUID(),createdAt:new Date().toISOString()},...d.farms]})),
  addSoilSample:item=>setData(d=>({...d,soilSamples:[{...item,id:crypto.randomUUID(),createdAt:new Date().toISOString()},...d.soilSamples]})),
  addDiseaseCase:item=>{const {preview,...safeRecord}=item;setData(d=>({...d,diseaseCases:[{...safeRecord,id:crypto.randomUUID(),createdAt:new Date().toISOString(),status:'Pending backend screening'},...d.diseaseCases]}))},
  addTask:item=>setData(d=>({...d,tasks:[{...item,id:crypto.randomUUID(),done:false},...d.tasks]})),
  toggleTask:id=>setData(d=>({...d,tasks:d.tasks.map(t=>t.id===id?{...t,done:!t.done}:t)})),
  addListing:item=>setData(d=>({...d,listings:[{...item,id:crypto.randomUUID(),createdAt:new Date().toISOString(),status:'Draft — local only'},...d.listings]})),
  addExpense:item=>setData(d=>({...d,expenses:[{...item,id:crypto.randomUUID()},...d.expenses]})),
  addHarvest:item=>setData(d=>({...d,harvests:[{...item,id:crypto.randomUUID()},...d.harvests]})),
  resetDemo:()=>setData(initial)
 }),[data]);
 return <AppDataContext.Provider value={api}>{children}</AppDataContext.Provider>;
}
export function useAppData(){const value=useContext(AppDataContext);if(!value)throw new Error('useAppData must be used inside AppDataProvider');return value}
