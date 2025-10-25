import csv
from datetime import datetime, timedelta
import os

# Hàm hỗ trợ
def read_time_csv():
    with open("time.csv", encoding="utf-8-sig") as file:
        return list(csv.reader(file))

def write_time_csv(rows):
    with open("time.csv", "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Bắt đầu
now_utc = datetime.utcnow()
now_vn = now_utc + timedelta(hours=7)
print("time now", now_vn.strftime("%Y-%m-%d %H:%M"))

rows = read_time_csv()
remaining_rows = []
executed_count = 0

for row in rows:
    if not row: continue
    try:
        # Chuyển string → datetime (giờ VN)
        scheduled_vn = datetime.strptime(row[0], "%m/%d/%Y %H:%M")

        scheduled_utc = scheduled_vn - timedelta(hours=7)

        if scheduled_utc <= now_utc:
            print("its time to start:", scheduled_vn)
            os.system("python khaosatcheogithub.py")
            executed_count += 1
        else:
            remaining_rows.append(row)
    except Exception as e:
        print("srror", row, "|", e)
        remaining_rows.append(row)

# Ghi lại file time.csv đã cập nhật
write_time_csv(remaining_rows)

if executed_count == 0:
    print("no time to fill")
else:
    print(f"filled {executed_count} form.")
