
import subprocess

program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3",
                "python3 3_mat_compliance_responsive.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 10000 -tao_ls_type more-thuente -m '1_to_3_mesh.msh' -o 'test3' -er 10.0 -es 10.0 -lr 1.5 -ls 0.5 -vr 0.5 -vs 0.5 -k 2.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"]


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