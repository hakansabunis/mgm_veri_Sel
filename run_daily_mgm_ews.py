from datetime import datetime
import os

OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

ts = datetime.now().strftime("%Y%m%d")
OUT_CSV  = f"{OUT_DIR}/mgm_daily_risk_all_provinces_{ts}.csv"
OUT_HTML = f"{OUT_DIR}/mgm_daily_ews_map_{ts}.html"
OUT_ALARM_CSV = f"{OUT_DIR}/mgm_daily_alarm_only_{ts}.csv"
