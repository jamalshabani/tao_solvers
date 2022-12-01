import subprocess

program_list = ["rm -rf test11", "rm -rf test12", "rm -rf test13",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 3000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test1' -er 1.0 -es 1.0e-2 -lr 2.0 -ls 0.007 -vr 0.3 -vs 0.5 -k 2.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 3000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test2' -er 1.0 -es 1.0e-2 -lr 2.0 -ls 0.008 -vr 0.3 -vs 0.5 -k 2.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 3000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test3' -er 1.0 -es 1.0e-2 -lr 2.0 -ls 0.006 -vr 0.3 -vs 0.5 -k 2.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 3000 -tao_ls_type more-thuente -m 'motion_mesh2.msh' -o 'test4' -er 1.0 -es 1.0e-2 -lr 2.0 -ls 0.005 -vr 0.3 -vs 0.5 -k 2.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"]





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
