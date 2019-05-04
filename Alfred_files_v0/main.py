import sys
from workflow import Workflow3

def main(wf):
    title = "I just finished a work using {} min.".format(wf.args[0])
    subtitle = "Restore the time and copy an unique id to your clipboard."
    wf.add_item(title=title,subtitle=subtitle,arg=wf.args[0],valid=True)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))
