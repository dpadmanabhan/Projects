import os
import subprocess
import random
def runncu_vector(thread):
    cmd='"C:/Program Files/NVIDIA Corporation/Nsight Compute 2019.5.0/target/windows-desktop-win7-x64/nv-nsight-cu-cli.exe" --force-overwrite --target-processes all --kernel-regex-base function --launch-skip-before-match 0 --page details --metrics smsp__average_inst_executed_per_warp.ratio,smsp__sass_thread_inst_executed_op_memory_pred_on.sum,smsp__sass_thread_inst_executed_op_control_pred_on.sum,smsp__inst_executed.sum,smsp__sass_thread_inst_executed_op_integer_pred_on.sum,smsp__sass_thread_inst_executed_op_fp32_pred_on.sum,smsp__inst_executed_op_global_st.sum,smsp__sass_thread_inst_executed_op_misc_pred_on.sum,smsp__inst_executed_op_shared_ld.sum,smsp__inst_executed_op_shared_st.sum,smsp__inst_executed_op_global_ld.sum,l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum,l1tex__data_pipe_lsu_wavefronts_mem_shared_op_st.sum --sampling-interval auto --sampling-max-passes 5 --sampling-buffer-size 33554432 --profile-from-start 1 --cache-control all --clock-control base --apply-rules "C:/Users/nithy/OneDrive/Desktop/CUDA/vectorDot.exe"'
    param=' -threads='+str(thread)
    with open("C:/Users/nithy/OneDrive/Desktop/CUDA/vdot/"+str(thread)+".txt","w+") as file:
        subprocess.run(cmd+param,shell=True,stdout=file)

def runcu_vector(thread):
    cmd='nvcc -I "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc" "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc/vectorDot.cu" -ccbin "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64" -o C:/Users/nithy/OneDrive/Desktop/CUDA/vectorDot -run -run-args'
    param=' -threads='+str(thread)
    subprocess.run(cmd+param,shell=True)

def main():
    #=[128*n+128  for n in range(10,1000+1)]
    tid=[2*n+2 for n in range(16,1024)]
    for t in tid:
        runncu_vector(t)
        runcu_vector(t)
        newname="C:/Users/nithy/OneDrive/Desktop/CUDA/vdottime/vectorDot" + str(t) +".txt"
        os.rename('C:/Users/nithy/OneDrive/Desktop/vectorDot.txt', newname)
main()
