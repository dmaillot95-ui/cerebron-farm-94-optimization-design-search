import json,hashlib,pathlib
# Deterministic constrained design search; objective intentionally simple.
c=[]
for x in range(1,101):
 mass=1000+4*x; energy=5000/x+2*x; feasible=(x>=10 and x<=80); score=mass+10*energy
 if feasible:c.append((score,x,mass,energy))
b=min(c); res={"status":"PASS","model":"deterministic-design-search-smoke-v1","best":{"x":b[1],"mass":b[2],"energy":b[3],"objective":b[0]},"evaluations":100,"epistemic":"TOY_OPTIMIZATION_NOT_ENGINEERING_OPTIMUM"}
pathlib.Path('artifacts').mkdir(exist_ok=True); raw=json.dumps(res,sort_keys=True).encode(); res['payload_sha256']=hashlib.sha256(raw).hexdigest(); pathlib.Path('artifacts/optimization.json').write_text(json.dumps(res,indent=2)+'\n'); print(json.dumps(res,indent=2))
