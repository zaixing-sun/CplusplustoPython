#!/bin/sh
#
#Force Bourne Shell if not Sun Grid Engine default shell (you never know!)
#
#$ -S /bin/sh
#$ -r y
#
# I know I have a directory here so I'll use it as my initial working directory
#
#$ -wd /vol/grid-solar/sgeusers/zhangyuye
#
# End of the setup directives
#
# Now let's do something useful, but first change into the job-specific
# directory that should have been created for us
#
# Check we have somewhere to work now and if we don't, exit nicely.
#

mkdir -p /local/tmp/zhangyuye/$JOB_ID

if [ -d /local/tmp/zhangyuye/$JOB_ID ]; then
        cd /local/tmp/zhangyuye/$JOB_ID
else
        echo "Uh oh ! There's no job directory to change into "
        echo "Something is broken. I should inform the programmers"
        echo "Save some information that may be of use to them"
        echo "Here's LOCAL TMP "
        ls -la /local/tmp
        echo "AND LOCAL TMP zhangyuye "
        ls -la /local/tmp/zhangyuye
        echo "Exiting"
        exit 1
fi

#
# Mail me at the b(eginning) and e(nd) of the job
#
# $ -M zhangyuye@ecs.vuw.ac.nz
# $ -m be
#
#
# Now we are in the job-specific directory so now can do something useful
#
# Stdout from programs and shell echos will go into the file
#    scriptname.o$JOB_ID
#  so we'll put a few things in there to help us see what went on
#
# Copy the input file to the local directory
#
cp -r /vol/grid-solar/sgeusers/zhangyuye/CplusplustoPython .
sleep 25


cd CplusplustoPython
g++ -o libpycallC_replace.so -shared -fPIC pycallC_replace.cpp

python pyCallCpp.py

# # cp -arv /vol/grid-solar/sgeusers/zhangyuye/test/* .
# # # go to the directory of your python program
# # #runing your program with $1 which is the random seed
# # python test.py $1


#copy the results to your result directory
# cp -r TrainingResult/CCGP/TestResult/*  /vol/grid-solar/sgeusers/zhangyuye/MDWS-CoCFog/TrainingResult/CCGP/TestResult
echo "Ran through OK"

