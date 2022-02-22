from utility.db import execute,execute_fetchall


def select_Hour_Wise():
    rows=execute_fetchall("""SELECT row_to_json(row) FROM
                            (SELECT extract(Hour FROM time) AS
                            time_per_hour,AVG(consumption),device FROM usecase
                            GROUP BY device,time_per_hour
                            ORDER BY time_per_hour) row """)
    return rows

def peak(date1,date2,device):
    rows=execute_fetchall("""SELECT row_to_json(row) FROM
                            (SELECT MAX(consumption) AS
                            peak_consumption,device FROM usecase
                            WHERE device='{}' AND time between '{}' AND '{}' 
                            GROUP BY device) row""".format(device,date1,date2))
    return rows

    
def selectAll():
    query = """SELECT row_to_json(row)
                FROM (SELECT * FROM usecase)row"""
    result = execute_fetchall(query)
    return result

def missing_Data(device):
    query = """SELECT c.* FROM (
                (SELECT device FROM usecase WHERE device='{}') a
				CROSS JOIN 
                (SELECT generate_series('2020-01-01 00:00'::timestamp,'2020-01-01 23:59'::timestamp,'1 minute') AS
				missingTimestamps) b) c 
				LEFT JOIN 
                (SELECT device,time FROM usecase) d
				ON c.device=d.device AND c.missingTimestamps=d.time
				WHERE d.time IS null""".format(device)

    query_data = execute_fetchall(query)
    return query_data

def checking_credential(email,password_md5):
    count=execute_fetchall("select * from empuser where email='{}'and password_md5='{}'".format(email,password_md5))
    if len(count)==1:
        return True
    return False
