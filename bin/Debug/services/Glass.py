import Acuity
import IPD

a = Acuity.main()
ip = IPD.main()

f = open("services\\acuity.txt", encoding="utf-8")
s = f.read()
f.close()

agnez, val = s.split()

f = open("services\\ipd.txt", encoding="utf-8")
ipd = f.read()
f.close()

f = open("services\\GlassStore.txt", "w", encoding="utf-8")
f.write(f"требуются очки для агнезии =  {agnez} со значением (диоптрии) =  {1/float(val)} и с межзрачковым расстоянием = {ipd}")
f.close()

print("записано в GlassStore.txt")