import os

def transform_img_to_mov(src, dest):
    
    os.makedirs(os.path.dirname(dest))
    
    cmd = "./ffmpeg -loop 1 -i {} -t 5 -pix_fmt yuv420p {}".format(src, dest)
    
    os.system(cmd)

def transform_img_to_img(src1, src2, dest):
    
    os.makedirs(os.path.dirname(dest))
    
    cmd = "./ffmpeg -loop 1 -i {} -loop 1 -i {} -filter_complex [1:v][0:v]blend=all_expr='A*(if(gte(T,3),1,T/3))+B*(1-(if(gte(T,3),1,T/3)))' -t 5 -c:v -pix_fmt yuv420p {}".format(src1, src2, dest)
    
    os.system(cmd)