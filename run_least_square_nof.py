import subprocess

program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3",
                "python3 least_square_nof.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type unit -m 'motion_nof_mesh2.msh' -o 'test1' -er 160 -es 1.6 -lr 0.1 -ls 0.1 -vr 0.5 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 least_square_nof.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m 'motion_nof_mesh2.msh' -o 'test2' -er 160 -es 1.6 -lr 0.1 -ls 0.1 -vr 0.5 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 least_square_nof.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type more-thuente -m 'motion_nof_mesh2.msh' -o 'test3' -er 160 -es 1.6 -lr 0.1 -ls 0.1 -vr 0.5 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"]






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


