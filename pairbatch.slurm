#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 22:00:00
#SBATCH -o  donnew.out
#SBATCH	--mem-per-cpu=200000M
#SBATCH -p largemem
#SBATCH -A biocomplexity

#grbgetkey 36598a1e-50ff-11e9-8236-02e454ff9c50
#grbgetkey 5de5055c-5115-11e9-82f3-02e454ff9c50

#grbgetkey aa2c8ad4-5115-11e9-8bf5-02e454ff9c50
#grbgetkey 03159ccc-53e0-11e9-b214-02e454ff9c50

#grbgetkey 5de5055c-5115-11e9-82f3-02e454ff9c50

python ThetaGenerator.py 3168 52 20 2

#python lp_ilp_icml.py 10 30 70 Philosopher_dataset_india_ancient_pairs.csv Philosopher_dataset_india_ancient.csv 50

#python lp_ilp_icml.py 20 30 30 all_gt_table_expanded_pairs.csv all_gt_table_expanded.csv 20
#python ReadFile1.py datasets/syn6 10000 syn6_10 1
#python ReadFile1.py datasets/syn6 9000 syn6_9 1


#python ReadFile.py datasets/movielens20M/movielensM5-T10.csv 9500 mov_95 1
#python ReadFile.py datasets/movielens20M/movielensM5-T10.csv 8500 mov_85 1
#python ReadFile.py datasets/movielens20M/movielensM5-T10.csv 7500 mov_75 1

#python ReadFile4.py datasets/Donald-Tweets\!/Donald-TweetsT2-H10.csv 200 don_new 1

#python ReadFile.py datasets/movielens20M/movielensM5-T10.csv 6500 mov_65_1 1
#python ReadFile.py datasets/movielens20M/movielensM5-T10.csv 5500 mov_55_1 1


