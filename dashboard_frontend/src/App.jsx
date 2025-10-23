import {useEffect,useState} from "react";
function App(){
  const[logs,setLogs]=useState([]);
  useEffect(()=>{
    fetch("http://localhost:8000/logs").then(r=>r.json()).then(d=>setLogs(d.logs||[]));
  },[]);
  return(
    <div style={{background:"#000",color:"#0f0",fontFamily:"monospace",padding:"20px"}}>
      <h1>🕵️ PhantomNet Monitor</h1>
      {logs.map((l,i)=><pre key={i}>{l}</pre>)}
    </div>);
}
export default App;
