from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def check(a, qs):
    out=str(solve_variance_queries(len(a),a,len(qs),qs)).strip().splitlines()
    exp=[_var_ref(a[l-1:r]) for l,r in qs]
    _assert(len(out)==len(exp), "Неверное количество строк.")
    for i,(s,e) in enumerate(zip(out,exp),1):
        try: x=float(s)
        except: raise AssertionError(f"Запрос {i}: ожидалось число.")
        _assert(_close(x,e,1e-6), f"Запрос {i}: ожидалось {e}, получено {x}")

check([1,2,3,4], [[1,4],[2,3],[4,4]])
check([7,7,7], [[1,3],[2,2]])

random.seed(202)
a=[random.randint(-50,50) for _ in range(150)]
qs=[]
for _ in range(90):
    l=random.randint(1,len(a)); r=random.randint(l,len(a)); qs.append([l,r])
check(a,qs)
print("OK: задача B")
