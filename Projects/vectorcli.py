import os
import subprocess
import random
def runncu_vector(size,thread,operation):
    cmd='"C:/Program Files/NVIDIA Corporation/Nsight Compute 2019.5.0/target/windows-desktop-win7-x64/nv-nsight-cu-cli.exe" --force-overwrite --target-processes all --kernel-regex-base function --launch-skip-before-match 0 --page details --metrics smsp__average_inst_executed_per_warp.ratio,smsp__sass_thread_inst_executed_op_memory_pred_on.sum,smsp__sass_thread_inst_executed_op_control_pred_on.sum,smsp__inst_executed.sum,smsp__sass_thread_inst_executed_op_integer_pred_on.sum,smsp__sass_thread_inst_executed_op_fp32_pred_on.sum,smsp__inst_executed_op_global_st.sum,smsp__sass_thread_inst_executed_op_misc_pred_on.sum,smsp__inst_executed_op_shared_ld.sum,smsp__inst_executed_op_shared_st.sum,smsp__inst_executed_op_global_ld.sum,l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum,l1tex__data_pipe_lsu_wavefronts_mem_shared_op_st.sum --sampling-interval auto --sampling-max-passes 5 --sampling-buffer-size 33554432 --profile-from-start 1 --cache-control all --clock-control base --apply-rules "C:/Users/nithy/OneDrive/Desktop/CUDA/intrinsic_int.exe"'
    param=' -size=' + str(size)+" "+'-threads='+str(thread)+" "+'-op='+str(operation)
    with open("C:/Users/nithy/OneDrive/Desktop/CUDA/vector/"+str(size)+"_"+str(thread)+".txt","w+") as file:
        subprocess.run(cmd+param,shell=True,stdout=file)

def runcu_vector(size,thread,operation):
    cmd='nvcc -I "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc" "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc/intrinsic_int.cu" -ccbin "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64" -o C:/Users/nithy/OneDrive/Desktop/CUDA/intrinsic_int -run -run-args'
    param=' -size=' + str(size)+","+'-threads='+str(thread)+","+'-op='+str(operation)
    subprocess.run(cmd+param,shell=True)

def main():
    sizes=[126*n+256  for n in range(10,1000+1)]
    t=[2*n+2 for n in range(32,1024)]
    threads=[16*n for n in range(32,1024)]
    op=[0,1,2,3,4]
    i=201
    c=0
    for s in sizes:
        size=s*1000
        thread=t[i]
        if(i>200):
            dimension=113400*100
            break
        if(c<=4):
            operation=op[c]
        else:
            c=0
            operation=op[c]
        runncu_vector(size,thread,operation)
        runcu_vector(size,thread,operation)
        newname="C:/Users/nithy/OneDrive/Desktop/CUDA/time/intrinsic_int" + str(size) +"_"+str(thread)+".txt"
        os.rename('C:/Users/nithy/OneDrive/Desktop/intrinsic_int.txt', newname)
        c+=1
        i+=1
    #dimension=dimension*2
    for i in range(0,5):
        for thread in threads:
            operation=op[i]
            runncu_vector(dimension,thread,operation)
            runcu_vector(dimension,thread,operation)
            newname="C:/Users/nithy/OneDrive/Desktop/CUDA/time/intrinsic_int" + str(dimension) +"_"+str(thread)+".txt"
            os.rename('C:/Users/nithy/OneDrive/Desktop/intrinsic_int.txt', newname)
main()
