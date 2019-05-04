import sys, time, csv, uuid
from workflow import Workflow3

def save_data(message):
    path = "logger/" + time.strftime("%Y-%m-%d",time.localtime()) + ".csv"
    with open(path, 'a+') as csvfile:
        csv.writer(csvfile).writerow(message)


def generate():

    wf = Workflow3()
    using_time = wf.args[0]
    today = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    unique_id = uuid.uuid1()
    message = [unique_id, today, using_time]
    save_data(message)
    query = "/*/*/ Using {} min work on {}".format(using_time, unique_id)
    print query

if __name__ == u'__main__':
    generate()
