from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def check(a,qs):
    out=str(solve_alarm_queries(len(a),a,len(qs),qs)).strip().splitlines()
    exp=[]
    for l,r,t in qs:
        exp.append("YES" if math.sqrt(max(0.0,_var_ref(a[l-1:r])))>t else "NO")
    _assert(out==exp, f"Ожидалось {exp}, получено {out}")

check([1,1,1,5], [[1,3,0],[1,4,1],[4,4,0]])
check([0,2], [[1,2,1],[1,2,0.999],[1,2,1.001]])

random.seed(404)
a=[random.randint(-30,30) for _ in range(120)]
qs=[]
for _ in range(70):
    l=random.randint(1,120); r=random.randint(l,120)
    t=random.choice([0,0.5,1,2,5,10,20])
    qs.append([l,r,t])
check(a,qs)
print("OK: задача D")
