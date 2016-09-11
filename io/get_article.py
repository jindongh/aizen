#!/bin/env python
import MySQLdb
import sys

SQL="select doc_id,doc_value from sucker_data_extra where doc_key='article_content' and doc_id in (select doc_id from sucker_data_info where cate_id=26)"


def main():
    ip=sys.argv[1]
    user=sys.argv[2]
    passwd=sys.argv[3]
    db=sys.argv[4]
    output=sys.argv[5]
    conn=MySQLdb.connect(host=ip,user=user,
            passwd=passwd,db=db)
    cursor = conn.cursor()
    cursor.execute(SQL)
    results = cursor.fetchall()
    for row in results:
        doc_id=row[0]
        doc_content = row[1]
        open('%s/%s' % (output, doc_id), 'w').write(doc_content)
    conn.close()

if __name__ == '__main__':
    if len(sys.argv) != 6:
        sys.exit('Usage: %s <ip> <user> <pass> <db> <outputfolder>' % sys.argv[0])
    conn=main()
