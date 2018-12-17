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
	Power.append(sheet.cell_value(i,1))
	Energy.append(sheet.cell_value(i,2))
	OperatingState.append(sheet.cell_value(i,3))
	BasicModule.append(sheet.cell_value(i,4))
	Lights.append(sheet.cell_value(i,5))
	CoolantPump.append(sheet.cell_value(i,6))
	SpindleMotor.append(sheet.cell_value(i,7))
	XAxisMotor.append(sheet.cell_value(i,8))
	YAxisMotor.append(sheet.cell_value(i,9))
	ZAxisMotor.append(sheet.cell_value(i,10))
	ToolSelectMotor.append(sheet.cell_value(i,11))
	ToolChangeMotor.append(sheet.cell_value(i,12))
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


