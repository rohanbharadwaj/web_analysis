__author__ = 'rohan'
import sys
import os
import subprocess,threading

home_dir = '/home/rohan/git/'
input_path = home_dir + 'wprof-mobile/dependency-analysis-tools/analysis_t/'
input_file = 'fixed_top200sites.txt'
result_path = home_dir + 'wprof-mobile/data/laptop_eth/logs/'
final_res = home_dir + 'results/'


class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            print 'Thread finished'

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode




for run_no in range(5):
    print "Removing Files"
    os.system("rm -rf temp_files/* dep_logs/* data/* graphs/* logs/* logs_pro")
    print "Copyting",str(run_no)
    os.system("cp "+result_path + input_file.split('.')[0] +"_run" + str(run_no) + "_log.txt logs")
    print "Running slice.pl"
    os.system("perl slice.pl logs")
    print "move from logs_pro"
    os.system("mv logs_pro data/wprof_300_5_pro_1")
    print "running analyze.pl"
    a = input('Do you want to continue : ')
    if(a=="y"):
        os.system("perl analyze.pl")
        # command = Command("perl analyze.pl")
        # command.run(timeout=30)
        print "removing temp files"
        os.system("rm -rf temp_files/wprof_300_5_pro_1/*")
        print "Running post analyze"
        os.system("py post_analyze.py")
        new_dir = final_res+str(run_no)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        os.system("cp -rf temp_files/wprof_300_5_pro_1/* "+new_dir)



