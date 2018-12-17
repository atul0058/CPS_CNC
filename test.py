import xlrd
import pymysql



file_location="D:/CPS of CNC/sheet1.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
# print(sheet.cell_value(0,0))
# print(sheet.nrows)
# print("====================")
# print(sheet.ncols)

Time=[]
Power=[]
Energy=[]
OperatingState=[]
BasicModule=[]
Lights=[]
CoolantPump=[]
SpindleMotor=[]
XAxisMotor=[]
YAxisMotor=[]
ZAxisMotor=[]
ToolSelectMotor=[]
ToolChangeMotor=[]
CuttingOperation=[]

for i in range(1,sheet.nrows):
	Time.append(sheet.cell_value(i,0))

for i in range(1,sheet.nrows):
	Power.append(sheet.cell_value(i,1))

for i in range(1,sheet.nrows):
	Energy.append(sheet.cell_value(i,2))

for i in range(1,sheet.nrows):
	OperatingState.append(sheet.cell_value(i,3))

for i in range(1,sheet.nrows):
	BasicModule.append(sheet.cell_value(i,4))

for i in range(1,sheet.nrows):
	Lights.append(sheet.cell_value(i,5))

for i in range(1,sheet.nrows):
	CoolantPump.append(sheet.cell_value(i,6))

for i in range(1,sheet.nrows):
	SpindleMotor.append(sheet.cell_value(i,7))

for i in range(1,sheet.nrows):
	XAxisMotor.append(sheet.cell_value(i,8))

for i in range(1,sheet.nrows):
	YAxisMotor.append(sheet.cell_value(i,9))

for i in range(1,sheet.nrows):
	ZAxisMotor.append(sheet.cell_value(i,10))

for i in range(1,sheet.nrows):
	ToolSelectMotor.append(sheet.cell_value(i,11))

for i in range(1,sheet.nrows):
	ToolChangeMotor.append(sheet.cell_value(i,12))

for i in range(1,sheet.nrows):
	CuttingOperation.append(sheet.cell_value(i,13))

conn = pymysql.connect(host="localhost", user="root", passwd="raspberry", db="CNC")
cur = conn.cursor()


for i in range(len(Time)):
    query=("""insert into test2(Time_sec,Power_W,Operating_State,Basic_Module,Lights,
    Coolant_Pump,Spindle_Motor,X_Axis_Motor,Y_Axis_Motor,Z_Axis_Motor,Tool_select_Motor,Tool_change_motor,Cutting_Operation)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(Time[i],Power[i],OperatingState[i],BasicModule[i],Lights[i],CoolantPump[i],SpindleMotor[i],XAxisMotor[i],YAxisMotor[i],
    ZAxisMotor[i],ToolSelectMotor[i],ToolChangeMotor[i],CuttingOperation[i]))
    cur.execute(*query)
    conn.commit()

cur.close()
conn.close()


