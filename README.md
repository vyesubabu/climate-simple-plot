# Climate Simple Plot

ลองพล็อตข้อมูลสภาพอากาศอย่างง่าย

## Data

- [Climate.gov Datasets Gallery](https://www.climate.gov/maps-data/datasets) `> Past Weather by Zip Code > Data Access`

- [Daily Summaries Thailand Details](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/FIPS:TH/detail)

## รวมข้อมูลให้เป็น CSV ไฟล์เดียว

เนื่องจาก climage.gov ได้มีการจำกัดการโหลดข้อมูล (10,000 rows ประมาณ 10 ปี) และ ขนาดไฟล์ของ github repo. เลยต้องทำการแยกโหลดเป็นหลายๆไฟล์ ทำการรวมไฟล์ csv เป็นไฟล์เดียวคือไฟล์ `1951-2019.csv`
โดยการรันไฟล์ `/data/concat_csv.py`

การแยกไฟล์เป็นผลตรวจวัดของแต่ละสถานี ให้ทำการรัน `/data/concat_csv.py` เพื่อให้ได้ไฟล์ `1951-2019.csv` มาก่อน จากนั้นทำการรัน `/data/station_csv.py` แล้วข้อมูลของแต่ละสถานีจะอยู่ในโฟลเดอร์ `/station_data/`

## อธิบายว่าแต่ละไฟล์ทำอะไรบ้าง

### `anomaly.py`

ทำการคำนวณหา anomaly (เฉลี่ยรายปี) จากข้อมูลประเทศไทย นำมาพล็อตเป็นกราฟเส้น

### `anomaly_nc.py`

ทำการคำนวณหา anomaly (เฉลี่ยรายปี) จาก nc file นำมาพล็อตเป็นแผนที่

### `climatology_month_thai.py`

ทำการคำนวณหาค่าเฉลี่ยรายเดือนจากข้อมูลประเทศไทย (เฉลี่ยเดือนเดียวกันจากทุกๆปี แกน x เป็น Jan..Dec) แล้วนำมาพล็อตเปรียบเทียบเป็นปี ครึ่งแรก vs ครึ่งหลัง แสดงให้เห็นถึง seasonal

### `histogram-annual.py`

พล็อตฮิสโตแกรมของข้อมูลประเทศไทย ครึ่งแรก vs ครึ่งหลัง เพื่อแสดงให้เห็นว่า distribution เปลี่ยนแปลงอย่างไร

### `HypothesisTesting.py`

Library เขียนเองสำหรับ Hypothesis testing (จะทดสอบ significance ของ trend, การเปลี่ยนแปลง climate) ทดสอบโดยใช้หาว่าค่าเฉลี่ยอยู่นอก confidence interval 90% หรือไม่ (ในความจริงควรใช้ Mann-Kendall test/ทดสอบว่า slope significance หรือไม่)

### `MannKendallTest.py`

Library เขียนเองสำหรับ MannKendall Test (มีคนอื่นเขียนไว้แล้ว - pymannkendall)

### `plot_stations_loc.py`

ทำการพล็อตเปรียบเทียบระหว่างตำแหน่งที่ตั้งของสถานีจากข้อมูลประเทศไทย และกริดของไฟล์ nc RCM


## R packages
```R
install.packages("package_name")
```
package list
```
ggplot2
dplyr
tidyverse
qmap
```
