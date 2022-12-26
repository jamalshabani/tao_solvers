
import subprocess

program_list = ["rm -rf test1", "rm -rf test2", "rm -rf test3", "rm -rf test4", "rm -rf test5",
                "python3 haha.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m '1_to_3_mesh.msh' -o 'test1' -es 100 -r 0.01 -lr 2.0 -ls 1.0 -vr 0.4 -vs 0.4 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 haha.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m '1_to_3_mesh.msh' -o 'test2' -es 100 -r 0.01 -lr 2.0 -ls 1.0 -vr 0.4 -vs 0.4 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 haha.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m '1_to_3_mesh.msh' -o 'test3' -es 100 -r 0.01 -lr 2.0 -ls 1.0 -vr 0.4 -vs 0.4 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 haha.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m '1_to_3_mesh.msh' -o 'test4' -es 100 -r 0.01 -lr 2.0 -ls 1.0 -vr 0.4 -vs 0.4 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 haha.py -tao_type bncg -tao_max_funcs 10000 -tao_gatol 1.0e-7 -tao_grtol 1.0e-7 -tao_gttol 1.0e-7 -tao_converged_reason -tao_monitor -tao_max_it 100 -tao_ls_type armijo -m '1_to_3_mesh.msh' -o 'test5' -es 100 -r 0.01 -lr 2.0 -ls 1.0 -vr 0.4 -vs 0.4 -k 5.0e-3 -e 4.0e-3 -p 2.0 -q 1.0"]



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
