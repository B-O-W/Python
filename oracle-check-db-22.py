#Author Mammadov Elbrus 11.23.2021 
import cx_Oracle
#Oracle-Client
cx_Oracle.init_oracle_client(config_dir=r"/opt/instantclient_21_4")
#vars for connection 
dsn_tns = cx_Oracle.makedsn(' ip ', '1521', service_name=' ')
conn = cx_Oracle.connect(user=r' ', password=" ", dsn=dsn_tns) 
#From outpout set conn in c variable
c = conn.cursor()
c.execute('SELECT count(*) from cms12s.v_KAPS_ONLINE_MO_QUEUE') # the command that runs inside the base
for rows in c:
    if rows <= (200,):
        print('OK: ' +str(rows))
        exit(0)
    if rows >= (210,):
        print('Warning: ' +str(rows))
        exit(1)
    if rows >= (500,):
        print('Critical: ' +str(rows))
        exit(2)
