import subprocess

program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3", "rm -rf test4",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 1000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test1' -er 1.0e1 -es 1.0e1 -lr 0.1 -ls 0.03 -vr 0.3 -vs 0.5 -k 2.0e-4 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 1000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test2' -er 1.1e1 -es 1.1e1 -lr 0.1 -ls 0.03 -vr 0.3 -vs 0.5 -k 2.0e-4 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 1000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test3' -er 1.2e1 -es 1.2e1 -lr 0.1 -ls 0.03 -vr 0.3 -vs 0.5 -k 2.0e-4 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 1000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test4' -er 1.3e1 -es 1.3e1 -lr 0.1 -ls 0.03 -vr 0.3 -vs 0.5 -k 2.0e-4 -e 4.0e-3 -p 2.0 -q 1.0"]





i = 1
for program in program_list:
    print("------------------------------------------------------------------------------")
    print("")
    print("Running test #{}".format(i))
    print("")
    print(program)
    print("")
    subprocess.run(program, shell = True)
    i = i + 1


# ErEs=1.0
#"python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 1500 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test1' -er 1.6 -es 1.6 -lr 0.4 -ls 0.2 -vr 0.3 -vs 0.5 -k 5.0e-4 -e 4.0e-3 -p 2.0 -q 1.0"]
