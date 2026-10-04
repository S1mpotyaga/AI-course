from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def check(a,qs):
    out=str(solve_skewness_queries(len(a),a,len(qs),qs)).strip().splitlines()
    exp=[_skew_ref(a[l-1:r]) for l,r in qs]
    _assert(len(out)==len(exp), "Неверное количество строк.")
    for i,(s,e) in enumerate(zip(out,exp),1):
        if e is None:
            _assert(s=="UNDEFINED", f"Запрос {i}: ожидалось UNDEFINED.")
        else:
            try: x=float(s)
            except: raise AssertionError(f"Запрос {i}: ожидалось число.")
            _assert(_close(x,e,1e-6), f"Запрос {i}: ожидалось {e}, получено {x}")

check([1,2,3,4], [[1,4],[2,2],[1,3]])
check([1,1,1,2,10], [[1,3],[1,5],[4,5]])

random.seed(505)
a=[random.randint(-15,15) for _ in range(140)]
qs=[]
for _ in range(80):
    l=random.randint(1,140); r=random.randint(l,140); qs.append([l,r])
check(a,qs)
print("OK: задача E")
