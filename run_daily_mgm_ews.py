from datetime import datetime
import os

OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

ts = datetime.now().strftime("%Y%m%d")
OUT_CSV  = f"{OUT_DIR}/mgm_daily_risk_all_provinces_{ts}.csv"
OUT_HTML = f"{OUT_DIR}/mgm_daily_ews_map_{ts}.html"
OUT_ALARM_CSV = f"{OUT_DIR}/mgm_daily_alarm_only_{ts}.csv"
df.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")
df[df["alarm"]==1].to_csv(OUT_ALARM_CSV, index=False, encoding="utf-8-sig")
m.save(OUT_HTML)
print("Saved:", OUT_CSV, OUT_ALARM_CSV, OUT_HTML)

