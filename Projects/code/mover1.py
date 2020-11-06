import os,fnmatch
from argparse import ArgumentParser
import shutil
from mpi4py import MPI

comm=MPI.COMM_WORLD

def move(size, source, destination,s=0):
    m=[]
    files=fnmatch.filter(os.listdir(source),'*rank_'+str(comm.rank))
    for f in files:
        s+=os.path.getsize(source+"/"+f)
        m.append(f)
        if(s>=size):
           break
    for f in m:
        shutil.move(source+"/"+f ,destination+"/"+f)

if __name__ == "__main__":

 parser = ArgumentParser()
 parser.add_argument('-m', '--movesize',type=int, help="Sets the amount of data to be moved",default=8)
 parser.add_argument('-s', '--source', type=str, help="specifies a source tier")
 parser.add_argument('-d', '--dest', type=str, help="specifies a destination tier")
 args = parser.parse_args()
 s=0
 move(args.movesize, args.source,args.dest,s)
