from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def answer(a,q):
    l1,r1,l2,r2=q
    v1=_var_ref(a[l1-1:r1]); v2=_var_ref(a[l2-1:r2])
    if math.isclose(v1,v2,rel_tol=1e-9,abs_tol=1e-9): return "EQUAL"
    return "FIRST" if v1<v2 else "SECOND"

def check(a,qs):
    out=str(solve_stability_queries(len(a),a,len(qs),qs)).strip().splitlines()
    exp=[answer(a,q) for q in qs]
    _assert(out==exp, f"Ожидалось {exp}, получено {out}")

check([5,5,5,1,3,5], [[1,3,4,6],[4,6,1,3]])
check([1,2,3,1,2,3], [[1,3,4,6]])

random.seed(303)
a=[random.randint(-20,20) for _ in range(100)]
qs=[]
for _ in range(60):
    l1=random.randint(1,100); r1=random.randint(l1,100)
    l2=random.randint(1,100); r2=random.randint(l2,100)
    qs.append([l1,r1,l2,r2])
check(a,qs)
print("OK: задача C")
