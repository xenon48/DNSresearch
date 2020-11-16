import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

h = "192.168.132.250"
u = "vsu2019"
p = "yGt2dA"
db = "telkov_db_dpo"
port = 5432

data, arr, slivki_arr = [], [], []

#get_info() - базовая функция для подключения к БД
def get_info(dbname, user, pwd, host, port, sql_entry):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=pwd, host=host, port=port)
        cursor = conn.cursor()
        cursor.execute(sql_entry)
        row = str(cursor.fetchall())
        if row == "[(None,)]":
           row = str('  0   ')
    except (Exception, psycopg2.Error) as error:
        return "Error while connecting to PostgreSQL:", error
    finally:
        return str(row[1::]) #

#pack_size() на вход требует дату, за которую делаем выборку, возвращает массив средних размеров пакетов
def pack_size(date):
    packs = get_info(db, u, p, h, port, sql_entry="select packets from ipcaddump where ipcdate >= '" + date + "' and destip = '10.227.11.45' and ipctime >= '17:10:00'  and sourceport = '53'").split() #and sourceip = '10.227.11.45'
    bytes = get_info(db, u, p, h, port, sql_entry="select bytes from ipcaddump where ipcdate >= '" + date + "' and destip = '10.227.11.45' and ipctime >= '17:10:00'  and sourceport = '53'").split()
    time = get_info(db, u, p, h, port, sql_entry="select ipctime from ipcaddump where ipcdate >= '" + date + "' and destip = '10.227.11.45' and ipctime >= '17:10:00'  and sourceport = '53'").split()
    new_tb, new_tp, bytes_per_packet = [], [], []
    for i in range(len(packs)):
        packs[i] = float(packs[i][1:-3])
        bytes[i] = float(bytes[i][1:-3])
        #time[i] = float(time[i][28:-4])

    time_bytes = defaultdict(list)
    for a, b in zip(time, bytes):
        time_bytes[a].append(b)

    time_packs = defaultdict(list)
    for a, b in zip(time, packs):
        time_packs[a].append(b)

    for i in range(len(list(time_bytes.values()))-1):
        new_tp.append(sum(list(time_packs.values())[i]))
        new_tb.append(sum(list(time_bytes.values())[i]))
        bytes_per_packet.append(new_tb[i]/new_tp[i])

    np.save('argwin_DST_10_telkov_tun', bytes_per_packet)
    return bytes_per_packet

def hrm_realtime(data):
    frq = 100
#    plt.hist(pack_size(date=date), bins=frq)
   # plt.plot()
    x = [i for i in range(1, len(data))]
    print(x)
    #plt.figure()
    plt.bar(x, data)
    #print('Sampling frequency is', frq)
    plt.savefig('histogram.png', format='png')
    plt.show()

pack_size('20200531')
