import os
import subprocess
import random
def runncu_matrix(wA,wB,hA,hB):
    cmd='"C:/Program Files/NVIDIA Corporation/Nsight Compute 2019.5.0/target/windows-desktop-win7-x64/nv-nsight-cu-cli.exe" --force-overwrite --target-processes all --kernel-regex-base function --launch-skip-before-match 0 --sampling-interval auto --sampling-max-passes 5 --sampling-buffer-size 33554432 --profile-from-start 1 --cache-control all --clock-control base --page details --metrics smsp__average_inst_executed_per_warp.ratio,smsp__sass_thread_inst_executed_op_memory_pred_on.sum,smsp__sass_thread_inst_executed_op_control_pred_on.sum,smsp__inst_executed.sum,smsp__sass_thread_inst_executed_op_integer_pred_on.sum,smsp__sass_thread_inst_executed_op_fp32_pred_on.sum,smsp__inst_executed_op_global_st.sum,smsp__sass_thread_inst_executed_op_misc_pred_on.sum --apply-rules "C:/Users/nithy/OneDrive/Desktop/CUDA/matrixMul.exe"'
    param=' -wA=' + str(wA) + " " + '-hA='+ str(hA)+" "+ '-wB='+str(wB)+" "+ '-hB='+str(hB)
    size=wA
    with open("C:/Users/nithy/OneDrive/Desktop/CUDA/matmul/"+str(wA)+".txt","w+") as file:
        subprocess.run(cmd+param,shell=True,stdout=file)

def runcu_matrix(wA,wB,hA,hB):
    cmd='nvcc -I "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc" "C:/ProgramData/NVIDIA Corporation/CUDA Samples/v10.2/common/inc/matrixMul.cu" -ccbin "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64" -o C:/Users/nithy/OneDrive/Desktop/CUDA/matrixMul -run -run-args'
    param=' wA='+ str(wA)+','+'hA='+str(hA)+','+'wB='+str(wB)+','+'hB='+str(hB)
    subprocess.run(cmd+param,shell=True)
def main():
    sizes=[32*n+64 for n in range(10,100+1)]
    for s in sizes:
        wA=hA=wB=hB=s
        runcu_matrix(wA,hA,wB,hB)
        runncu_matrix(wA,hA,wB,hB)
        newname="C:/Users/nithy/OneDrive/Desktop/CUDA/matmul_time/" + str(wA) +".txt"
        os.rename('C:/Users/nithy/OneDrive/Desktop/matmul_test.txt', newname)
main()
