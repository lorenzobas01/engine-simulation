import numpy as np

#This code aims at simulating what happens inside in a turbojet engine
#Inlet parameter will be asked as input, as well as crucial design parameter like pressure ratio, inlet mass flow, flow properties and combustion efficiency
#The temperature after the combustion will be assumed as known as it usually it depends from material and the cooling

#The system is made of compressor+combustion chamber+ turbine with the possibility to have bleeding from compressor air to reduce Tt before turbine
#The aim is to compute: fuel mass flow and net work

Tt2=float(input('inlet total temperature: '))
cp0=float(input('cp before combustion: '))
combustion_efficiency=float(input('combustion efficiency: '))
opr=float(input('overall pressure ratio: '))
mdot=float(input('inlet mass flow: '))
cp9=float(input('cp after combustion: '))
k0=1.4
Tt4=1500
H=44000000 #heating value of kerosene

eta_comp=float(input('isentropic compressor efficiency: '))

input_1=int(input('is there bleeding(1=yes, 0=no)?: '))

if input_1==1:
    beta=float(input('percentage of bleed air: '))
elif input_1==0:
    beta=0

Tt4=1000
H=44000000000


Tt3_is=Tt2*np.power(opr,(k0-1)/k0)
Tt3=Tt2+(Tt3_is-Tt2)/eta_comp

m31dot=(100-beta)*mdot/100
cp_avg=(cp0+cp9)/2

fuel_mass_flow=m31dot*cp_avg*(Tt4-Tt3)/(H*combustion_efficiency-cp_avg*Tt4)

#After combustion chamber we have three flows mixing, hot flow from cc, cool flow from bleeding and an intermediate temperature flow, i assume this cp =cp after cc


Tt41=((m31dot+fuel_mass_flow)*Tt4+mdot*beta*Tt3/100)/(mdot+fuel_mass_flow)

#I assume mechanical efficiency
eta_mech=0.99
#Tt5 is derived from the shaft balance, by assuming that the turbine only feeds the compressor
Tt5=Tt41-mdot*cp0*(Tt3-Tt2)/(eta_mech*cp9*(mdot+fuel_mass_flow))

turbine_work=np.abs(Tt5-Tt41)*cp9
compressor_work=(Tt3-Tt2)*cp0
net_work=turbine_work-compressor_work

print("fuel mass flow is: " +str(fuel_mass_flow) + " kg/s")
print('net work is: '+str(net_work)+' J/Kg')






