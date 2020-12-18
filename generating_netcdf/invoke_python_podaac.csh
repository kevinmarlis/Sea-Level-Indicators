#!/bin/tcsh -fe

# 1 = num jobs
# 2 = job id
# 3 = grouping id
set numjobs  = `printf "%05d" $1`
set job_id   = `printf "%05d" $2`
set gid      = `printf "%05d" $3`
set product_type = $4
set output_freq_code = $5
set output_dir = $6

mkdir -p       run_${product_type}_${output_freq_code}_${numjobs}_${gid}

printenv     > run_${product_type}_${output_freq_code}_${numjobs}_${gid}/env_${job_id}

echo "Executing run $1 $2 $3 $4 $5 $6 on $HOST in $PWD" > run_${product_type}_${output_freq_code}_${numjobs}_${gid}/exec_${numjobs}_${gid}

echo `date` >> run_${product_type}_${output_freq_code}_${numjobs}_${gid}/exec_${numjobs}_${gid}

conda activate ecco

echo "invoking python $1 $2 $3 $4 $5 $6"

python /home5/ifenty/git_repos_others/ECCO-GROUP/ECCO-ACCESS/generating_netcdf/eccov4r4_gen_for_podaac.py --num_jobs=$1 --job_id=$2 --grouping_to_process=$3 --product_type=$4 --output_freq_code=$5 --output_dir=$6 > run_${product_type}_${output_freq_code}_${numjobs}_${gid}/output_${job_id}
