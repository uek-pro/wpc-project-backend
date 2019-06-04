import os
import stat

SLIDE_SHOW_PATH = './tmp/slideshow'

# st = os.stat(SLIDE_SHOW_PATH)
# os.chmod(SLIDE_SHOW_PATH, st.st_mode | stat.S_IEXEC)

def create_slide_show(srcs, dest):
    cmd = "{} {} {}".format(SLIDE_SHOW_PATH, dest, " ".join(srcs))
    print(cmd)
    os.system(cmd)