import subprocess

#"python3 3_mat_compliance.py -tao_type bncg -tao_monitor -tao_max_it 200 -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'test1' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.4 -k 2.2e-3 -e 1.0e-3 -p 2.0 -q 1.0"
program_list = ["rm -rf bncg", "rm -rf bqnls", "rm -rf blmvm",
                "python3 3_mat_compliance.py -tao_type bncg  -tao_monitor -tao_max_it 200 -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'bncg' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.4 -k 2.2e-3 -e 4.0e-3 -p 2.0 -q 2.0",
                "python3 3_mat_compliance.py -tao_type bqnls -tao_monitor -tao_max_it 200 -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'bqnls' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.4 -k 2.2e-3 -e 4.0e-3 -p 2.0 -q 1.0",
                "python3 3_mat_compliance.py -tao_type blmvm -tao_monitor -tao_max_it 200 -tao_gatol 1e-7 -m '1_to_3_mesh.msh' -o 'blmvm' -er 1.0 -es 1.0e-2 -vr 0.3 -vs 0.4 -k 2.2e-3 -e 4.0e-3 -p 2.0 -q 1.0"]


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
