from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def check(a, qs):
    out = str(solve_mean_queries(len(a),a,len(qs),qs)).strip().splitlines()
    exp = [_mean_ref(a[l-1:r]) for l,r in qs]
    _assert(len(out)==len(exp), "Неверное количество строк.")
    for i,(s,e) in enumerate(zip(out,exp),1):
        try: x=float(s)
        except: raise AssertionError(f"Запрос {i}: ожидалось число.")
        _assert(_close(x,e,1e-6), f"Запрос {i}: ожидалось {e}, получено {x}")

check([2,4,6,8,10], [[1,3],[2,5],[5,5]])
check([-5,5,-5,5], [[1,4],[1,1],[2,3]])

random.seed(101)
a=[random.randint(-100,100) for _ in range(120)]
qs=[]
for _ in range(80):
    l=random.randint(1,len(a)); r=random.randint(l,len(a)); qs.append([l,r])
check(a,qs)
print("OK: задача A")
