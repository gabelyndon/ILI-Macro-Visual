#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys
import matplotlib.pyplot as plt


# In[2]:


input_file = 'ili_run_sheet.csv'
output_file = 'conditions_r_met.csv'

x= 0
fn= 1
fd = 2
mdp = 3
ya = 4


# In[3]:


with open(input_file,'r',newline='') as f:
    with open(output_file,'w',newline='')as o:
        
        reader = csv.reader(f)
        writer = csv.writer(o)
        header_row = next(reader)
        writer.writerow(header_row)
        print("Column Header Index:")
        
        for index,column_header in enumerate(header_row):
            print(index,column_header)
            
        #I will grab all anomalies to scatter plot from run data and set up 3 list
        ili_data,         descript_data, descript, descript_y, descript_descript,         agm,agm_label,agm_data,         weld, weld_pipe, weld_data,         gweq,gweq_pipe,gweq_data,         tap,tap_data,tap_pipe,         tee, tee_pipe, tee_data,         valve, valve_pipe,valve_data,         sleeve,sleeve_pipe,sleeve_data,         anomaly, anomaly_pipe, anomaly_data,         dp_anomaly,dp_anomaly_pipe,dp_anomaly_data,         flange, flange_pipe, flange_data,         composite,composite_pipe,composite_data,         patch,patch_pipe,patch_data,         magnet,magnet_pipe,magnet_data,         casing,casing_pipe,casing_data,         install,install_pipe,install_data,         attach,attach_pipe,attach_data,         trap,trap_pipe,trap_data,         lbend,lbend_pipe,lbend_data,         rbend,rbend_pipe,rbend_data,         ubend,ubend_pipe,ubend_data,         dbend,dbend_pipe,dbend_data,         deform,deform_pipe,deform_data,         = [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         [],[],[],[],[],[],[],[],[],[],         []

        for row in reader:
            odometers = float(row[x])
            feature_number = int(row[fn])
            description = str(row[fd])
            depth_percent = float(row[mdp])
            y_axis = int(row[ya])
            run_data = row[:]
        
            ili_data.append(run_data)
            
            #insert up index description in row[7]
            descript_data.append(row)
            descript.append(odometers)
            descript_y.append(y_axis)
            descript_descript.append(description)

            def feature_setup(feature,feature_odo,feature_data,feature_pipe):
                if description == feature:
                    feature_odo.append(odometers)
                    feature_pipe.append(y_axis)
                    feature_data.append(row)
                    writer.writerow(row)

            feature_setup('Tap',tap,tap_data,tap_pipe)

            feature_setup('Tee',tee,tee_data,tee_pipe)

            feature_setup('Valve',valve,valve_data,valve_pipe)

            feature_setup('Girth Weld',weld,weld_data,weld_pipe)

            feature_setup('Sleeve Begin',sleeve,sleeve_data,sleeve_pipe)
            feature_setup('Sleeve End ',sleeve,sleeve_data,sleeve_pipe)

            feature_setup('Flange',flange,flange_data,flange_pipe)

            feature_setup('Magnet',magnet,magnet_data,magnet_pipe)

            feature_setup('Casing End',casing,casing_data,casing_pipe)
            feature_setup('Casing Begin',casing,casing_data,casing_pipe)

            feature_setup('Area Launcher',trap,trap_data,trap_pipe)
            feature_setup('Start Launcher',trap,trap_data,trap_pipe)

            feature_setup('Deformation Anomaly',deform,deform_data,deform_pipe)
            
            feature_setup('AGM',agm,agm_label,agm_data)
            
            feature_setup('Metal Loss Anomaly',anomaly,anomaly_pipe,anomaly_data)
            
            feature_setup('Bend Left',lbend,lbend_data,lbend_pipe)
            feature_setup('Bend Right',rbend,rbend_data,rbend_pipe)
            feature_setup('Bend up',ubend,ubend_data,ubend_pipe)
            feature_setup('Bend down',dbend,dbend_data,dbend_pipe)
            


# In[4]:


print("\n")
print(lbend_data)
for index,description in enumerate(set(descript_descript)):
    print(index,description)


# In[5]:



print("\n")
print("there are " + str(len(tap))+ " taps in this section of pipeline.")
print("there are " + str(len(tee))+ " tee's in this section of pipeline.")
print("there are " + str(len(valve))+ " valves in this section of pipeline.")
print("there are " + str(len(flange))+ " flanges in this section of pipeline.")
print("there are " + str(len(anomaly))+ " metal loss anomalies in this section of pipeline.")
print("there are " + str(len(sleeve))+ " sleeve hotends in this section of pipeline")
print("there are " + str(len(casing)) + " casing ends in this section of pipeline")
print("there are " + str(len(lbend)) + " left bends in this section of pipeline")
print("there are " + str(len(rbend)) + " right bends in this section of pipeline")
print("there are " + str(len(ubend)) + " up bends in this section of pipeline")
print("there are " + str(len(deform)) + " deformations in this section of pipeline")
   


# In[6]:


fig = plt.figure(dpi = 128, figsize=(11.3,5.75))
plt.scatter(weld,weld_pipe,s=5000,color='grey',marker='|')
plt.scatter(anomaly,anomaly_data,s=45,color='lightcoral',marker='*')
plt.scatter(tap,tap_pipe,s=100,color='turquoise',marker='o')
plt.scatter(tap,tap_pipe,s=100,color='darkblue',marker='+')
plt.scatter(tee,tee_pipe,s=200,color='limegreen',marker='o')
plt.scatter(tee,tee_pipe,s=200,color='darkblue',marker='+')
plt.scatter(sleeve,sleeve_pipe,s=6000,color='red',marker='|')
plt.scatter(sleeve,sleeve_pipe,s=3000,color='crimson',marker='|')
plt.scatter(flange,flange_pipe,s=2200,color='gold',marker='|')
plt.scatter(agm,agm_data,s=200,color='red',marker='o')
plt.scatter(agm,agm_data,s=150,color='navy',marker='P')
plt.scatter(agm,agm_data,s=100,color='w',marker='+')
plt.scatter(casing,casing_pipe,s=9000,color='indigo',marker='|')
plt.scatter(valve,valve_pipe,s=100,color='lightsteelblue',marker='X')
plt.scatter(valve,valve_pipe,s=1000,color='blue',marker='x')
plt.scatter(lbend,lbend_pipe,s=100,color='blue',marker='<')
plt.scatter(rbend,rbend_pipe,s=100,color='blue',marker='>')
plt.scatter(ubend,ubend_pipe,s=100,color='blue',marker='^')
plt.scatter(dbend,dbend_pipe,s=100,color='blue',marker='v')
plt.scatter(deform,deform_pipe,s=500,color='green',marker='*')

#set chart title and label axes.
plt.title("ILI Macro Visual", fontsize=26)
plt.xlabel("Odometer Readings (ft)",fontsize=20)
#plt.ylabel("Pipeline Depth of Cover",fontsize=20)

plt.tick_params(labelleft='off')
plt.axis([-277,1000, -5,5])

plt.show()

