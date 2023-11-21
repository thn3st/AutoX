import sqlite3
import os
from definitions import ROOT_DIR
from models.device import DevicePhone
import threading

lock = threading.Lock()


def get_conn():
    conn = sqlite3.connect(os.path.join(ROOT_DIR, 'data/account.db'))
    return conn


def create_table():
    conn = get_conn()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS DEVICE(
            SERIAL TEXT NOT NULL UNIQUE,
            USER_NAME CHAR(50),
            PASSWORD TEXT,
            TWOFA TEXT,
            MAIL TEXT,
            PASS_MAIL TEXT,
            LAST_STATUS TEXT,
            PROXY TEXT
        );
    ''')

    conn.close()


def update_account(uid: str, category_id: int = None, uid_status: str = None, status: str = None,
                   last_status: str = None, hotmail=None, token=None, cookie=None, two_fa=None, new_password=None,
                   friend=None, friend_request=None, friend_requested=None, friend_suggestion=None,
                   mail=None, pass_mail=None, ua=None, proxy=None, secondary_mail=None):
    lock.acquire()
    conn = None
    result = True
    try:
        conn = get_conn()
        cur = conn.cursor()
        if friend_suggestion is not None:
            cur.execute("UPDATE ACCOUNT SET FRIEND_SUGGESTION = ? WHERE UID = ?", (friend_suggestion, uid))
        if friend_requested is not None:
            cur.execute("UPDATE ACCOUNT SET FRIEND_REQUESTED = ? WHERE UID = ?", (friend_requested, uid))
        if friend is not None:
            cur.execute("UPDATE ACCOUNT SET FRIEND = ? WHERE UID = ?", (friend, uid))
        if friend_request is not None:
            cur.execute("UPDATE ACCOUNT SET FRIEND_REQUEST = ? WHERE UID = ?", (friend_request, uid))
        if category_id is not None:
            cur.execute("UPDATE ACCOUNT SET CATEGORY = ? WHERE UID = ?", (category_id, uid))
        if uid_status is not None:
            cur.execute("UPDATE ACCOUNT SET UID_STATUS = ? WHERE UID = ?", (uid_status, uid))
        if status is not None:
            cur.execute("UPDATE ACCOUNT SET STATUS = ? WHERE UID = ?", (status, uid))
        if last_status is not None:
            cur.execute("UPDATE ACCOUNT SET LAST_STATUS = ? WHERE UID = ?", (last_status, uid))
        if hotmail is not None:
            if hotmail.mail and hotmail.mail.find('@') >= 0:
                cur.execute("UPDATE ACCOUNT SET MAIL = ?, PASS_MAIL = ? WHERE UID = ?",
                            (hotmail.mail, hotmail.password, uid))
        if token is not None:
            cur.execute("UPDATE ACCOUNT SET TOKEN = ? WHERE UID = ?", (token, uid))
        if new_password is not None:
            cur.execute("UPDATE ACCOUNT SET PASSWORD = ? WHERE UID = ?", (new_password, uid))
        if cookie is not None:
            cur.execute("UPDATE ACCOUNT SET COOKIE = ? WHERE UID = ?", (cookie, uid))
        if two_fa is not None:
            cur.execute("UPDATE ACCOUNT SET TWOFA = ? WHERE UID = ?", (two_fa, uid))
        if secondary_mail is not None:
            cur.execute("UPDATE ACCOUNT SET SECONDARY_MAIL = ? WHERE UID = ?", (secondary_mail, uid))
        if mail is not None:
            cur.execute("UPDATE ACCOUNT SET MAIL = ? WHERE UID = ?", (mail, uid))
        if pass_mail is not None:
            cur.execute("UPDATE ACCOUNT SET PASS_MAIL = ? WHERE UID = ?", (pass_mail, uid))
        if ua is not None:
            cur.execute("UPDATE ACCOUNT SET UA = ? WHERE UID = ?", (ua, uid))
        if proxy is not None:
            cur.execute("UPDATE ACCOUNT SET PROXY = ? WHERE UID = ?", (proxy, uid))
        conn.commit()
    except Exception as e:
        print(e)
        result = False
    finally:
        if conn is not None:
            conn.close()
    lock.release()
    return result


def save_devices(devices: []):
    conn = None
    success_count = 0
    fail_count = 0
    try:
        conn = get_conn()
        cur = conn.cursor()
        for device in devices:
            cur.execute("""
                INSERT INTO DEVICE (SERIAL, USER_NAME, PASSWORD, TWOFA, MAIL, PASS_MAIL, PROXY)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (device.serial, device.user_name, device.password, device.two_fa, device.mail, device.pass_mail,
                  device.proxy))
        conn.commit()
    except Exception as e:
        print(e)
    if conn is not None:
        conn.close()
    return {'success_count': success_count, 'fail_count': fail_count}


def update_device(device: DevicePhone):
    conn = None
    result = False
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
        UPDATE DEVICE SET USER_NAME = ?, PASSWORD = ?, TWOFA = ?, MAIL = ?, PASS_MAIL = ?, PROXY = ? WHERE SERIAL = ?
        """, (
        device.user_name, device.password, device.two_fa, device.mail, device.pass_mail, device.proxy, device.serial))
        conn.commit()
        result = True
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    return result


def delete_device_by_serials(serials: []):
    conn = None
    result = True
    try:
        conn = get_conn()
        cur = conn.cursor()
        for serial in serials:
            cur.execute("DELETE FROM DEVICE WHERE SERIAL=?", (serial,))
        conn.commit()
    except Exception as e:
        print(e)
        result = False
    finally:
        if conn is not None:
            conn.close()
    return result


def find_device_by_serial(serial: str):
    conn = None
    row = None
    device = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cursor = cur.execute("""
        SELECT SERIAL, USER_NAME, PASSWORD, TWOFA, MAIL, PASS_MAIL, PROXY
        FROM DEVICE 
        WHERE 
        (? IS NULL OR ? LIKE '' OR DEVICE.SERIAL LIKE ?)
        """, (serial, serial, '%' + serial + '%'))
        row = cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    if row:
        device = DevicePhone()
        device.serial = row[0]
        device.user_name = row[1]
        device.password = row[2]
        device.two_fa = row[3]
        device.mail = row[4]
        device.pass_mail = row[5]
        device.proxy = row[6]
    return device


def find_all_devices():
    conn = None
    rows = None
    list_device = []
    try:
        conn = get_conn()
        cur = conn.cursor()
        cursor = cur.execute("""
            SELECT SERIAL, USER_NAME, PASSWORD, TWOFA, MAIL, PASS_MAIL, PROXY
            from DEVICE 
        """)
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    if rows is None:
        return []
    for row in rows:
        device = DevicePhone()
        device.serial = row[0]
        device.user_name = row[1]
        device.password = row[2]
        device.two_fa = row[3]
        device.mail = row[4]
        device.pass_mail = row[5]
        device.proxy = row[6]
        list_device.append(device)
    return list_device


def get_account_to_models(list_serial: []):
    conn = None
    rows = None
    list_device = []
    try:
        conn = get_conn()
        cur = conn.cursor()
        cursor = cur.execute(f"""
        SELECT SERIAL, USER_NAME, PASSWORD, TWOFA, MAIL, PASS_MAIL, PROXY
        from DEVICE 
        where DEVICE.SERIAL IN ({','.join(['?'] * len(list_serial))})
        """, list_serial)
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    for row in rows:
        device = DevicePhone()
        device.serial = row[0]
        device.user_name = row[1]
        device.password = row[2]
        device.two_fa = row[3]
        device.mail = row[4]
        device.pass_mail = row[5]
        device.proxy = row[6]
        list_device.append(device)
    return list_device


def get_account_to_save(serial):
    conn = None
    row = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cursor = cur.execute("""
        SELECT USER_NAME, PASSWORD, TWOFA, MAIL, PASS_MAIL, PROXY
        from DEVICE 
        where DEVICE.SERIAL = ?
        """, (serial,))
        row = cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    return row


def update_last_status(serial, last_status):
    conn = None
    result = False
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            UPDATE DEVICE SET LAST_STATUS = ? WHERE SERIAL = ?
            """, (last_status, serial))
        conn.commit()
        result = True
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
    return result
