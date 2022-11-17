import subprocess

# "python3 3_mat_compliance.py -tao_bncg_type ssml_brdn -tao_converged_reason -tao_bncg_alpha 1.0 -tao_monitor -tao_max_it 2000 -tao_ls_type unit -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'test1' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
# "python3 3_mat_compliance.py -tao_bncg_type ssml_bfgs -tao_converged_reason -tao_bncg_alpha 1.0 -tao_monitor -tao_max_it 2000 -tao_ls_type unit -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'test2' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"
program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3",
                "python3 3_mat_least_square.py -tao_type cg -tao_converged_reason -tao_monitor -tao_max_it 2000 -tao_ls_type unit  -m 'motion_mesh.msh' -o 'test1' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square.py -tao_type cg -tao_converged_reason -tao_monitor -tao_max_it 2000 -tao_ls_type armijo  -m 'motion_mesh.msh' -o 'test2' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_least_square.py -tao_type cg -tao_converged_reason -tao_monitor -tao_max_it 2000 -tao_ls_type more-thuente -m 'motion_mesh.msh' -o 'test3' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.5 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"]



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
