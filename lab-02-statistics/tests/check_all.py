from pathlib import Path
for name in [
    "check_0a_mean_filter.py",
    "check_0b_std_filter.py",
    "check_0c_skewness_direction.py",
    "check_prefixes.py",
    "check_a_mean.py",
    "check_b_variance.py",
    "check_c_stability.py",
    "check_d_alarm.py",
    "check_e_skewness.py",
]:
    print(f"--- {name} ---")
    exec((Path("./tests")/name).read_text(encoding="utf-8"), globals())
print("\nВСЕ ПРОВЕРКИ ПРОЙДЕНЫ")
