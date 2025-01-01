from datetime import datetime as clc
import math as m

init_act_x_seri = 37950 #kBk
init_act_og3_seri = 162300 #kBk

time_sep = clc.strptime("11:13", "%H:%M") 
time_start = clc.strptime("17:15","%H:%M") 

og_start_date = clc.strptime("22 November 2024", "%d %B %Y")
x_start_date = clc.strptime("03 September 2024", "%d %B %Y")

seri = {'Х-серия': [init_act_x_seri, x_start_date], "ОГ3-серия": [init_act_og3_seri, og_start_date]} # первое занчение активность, второе дата запуска
geom = {'250 mm':[-0.826, 15.74], 'TOP':[-0.821, 14.22], 'low':[-0.856, 18.12], 'голова':[-0.866, 19.92]}

def measurment_act(N, exp, cousen_geom):
    geom = {'250mm':[-0.826, 15.74], 'TOP':[-0.821, 14.22], 'low':[-0.856, 18.12], 'голова':[-0.866, 19.92]}
    Netal = m.exp(geom.get(cousen_geom)[0]*m.log(1077.34, m.e) + geom.get(cousen_geom)[1])
    dat=[]
    for i in N:
        val = ((i*1000)/exp)*(100/3.22)
        dat.append((val/Netal)*100)
    return dat #возвращает активность на момент измерения в кБк
    

def statistic(dat):
    mean_val = sum(dat)/len(dat)
    sum_diff = 0
    for i in dat:
        dif = (i - mean_val)**2
        sum_diff += dif
    s = m.sqrt(sum_diff/(len(dat) -1))
    sx = s/m.sqrt(len(dat))
    if len(dat) == 3:
        return ((sx*4.3)/mean_val)*100
    elif len(dat) == 4:
        return ((sx*3.182)/mean_val)*100
    elif len(dat) == 5:
        return ((sx*2.77)/mean_val)*100 #возвращает погрешность для входного ряда значений в процентах

def dt_calc(dt, expos, data):
    exp_1 = 0
    res_dt=[]
    for i in range (0, len(data)):
        if i >= 1:
            exp_1+=expos
        res_dt.append((dt*m.exp(-0.693*exp_1/67.71))/100)
    
    return res_dt

def output(time_sep, time_start, dt, dat, seria, date, expos):
    time_start = clc.strptime(time_start, "%H:%M") 
    time_sep = clc.strptime(time_sep, "%H:%M")
    date = clc.strptime(date, "%d.%m.%Y")
    seri = {'Х-серия': [init_act_x_seri, x_start_date], "ОГ3-серия": [init_act_og3_seri, og_start_date]} # первое занчение активность, второе дата запуска
    dt_other = dt_calc(dt, expos, dat)
    Tge = 270.93 
    Tga = 67.71
    first_deltatime = (time_start - time_sep).total_seconds()
    result_a0 = [dat[0]/m.exp((-0.693*(first_deltatime/60))/Tga)]


    for i in range(1, len(dat)):
        first_deltatime += expos + expos*dt_other[i]
        result_a0.append(dat[i]/m.exp((-0.693*(first_deltatime/60))/Tga))
    first_deltatime = 0
    mean_a0 = sum(result_a0)/len(result_a0)
    max_act_today = seri.get(seria)[0] * m.exp(-0.693*((date - seri.get(seria)[1]).total_seconds())/(3600*24)/ Tge)
    outp = [round(mean_a0, 3), round(statistic(result_a0), 3), round((mean_a0/max_act_today)*100, 3)]
    return outp


def activity_calculation(data, exp, time_separation, time_start_meas, ser, geo, deadtime, date_of_measurment):
    act = measurment_act(data, exp, geo)
    result = output(time_separation, time_start_meas, deadtime, act, ser, date_of_measurment, exp)
    return result

def output_dz(time_sep, time_start, dat, date, expos):
    date = clc.strptime(date, "%d.%m.%Y")
    time_start = clc.strptime(time_start, "%H:%M") 
    time_sep = clc.strptime(time_sep, "%H:%M")
    expos = (clc.strptime(expos, "%H:%M")-clc.strptime("00:00", "%H:%M")).total_seconds()
    Tga = 67.71
    first_deltatime = (time_start - time_sep).total_seconds()
    result_a0 = [dat[0]/m.exp((-0.693*(first_deltatime/60))/Tga)]
    for i in range(1, len(dat)):
        first_deltatime += expos
        result_a0.append(dat[i]/m.exp((-0.693*(first_deltatime/60))/Tga))
    first_deltatime = 0
    mean_a0 = sum(result_a0)/len(result_a0)

    outp = [round(mean_a0, 3), round(statistic(result_a0), 3)]
    return outp

    
    

if __name__ == "__main__":
    test_data = [1389, 1310, 1214, 1123]
    date_test = clc.strptime("05 November 2024", "%d %B %Y")
    test_expos = 400
    time_start_test = clc.strptime("14:45","%H:%M") 
    time_sep_test = clc.strptime("11:16","%H:%M")
    seria_test = 'Х-серия'
    test_geo = 'TOP'
    test_result = activity_calculation(test_data, test_expos, time_sep_test, time_start_test, seria_test, test_geo, deadtime= 5, date_of_measurment=date_test)
    print(test_result)
    