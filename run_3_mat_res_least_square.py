import subprocess

program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3",
                "python3 3_mat_res_least_square.py -tao_bncg_type ssml_brdn -tao_converged_reason -tao_bncg_alpha 1.0 -tao_monitor -tao_max_it 500 -tao_ls_type unit -tao_gatol 1e-7 -m 'motion_mesh1.msh' -o 'test1' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.3 -k 3.0e-3 -e 2.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_res_least_square.py -tao_bncg_type ssml_bfgs -tao_converged_reason -tao_bncg_alpha 1.0 -tao_monitor -tao_max_it 500 -tao_ls_type unit -tao_gatol 1e-7 -m 'motion_mesh1.msh' -o 'test2' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.3 -k 3.0e-3 -e 2.0e-3 -p 2.0 -q 1.0"]


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
