import subprocess
from .input_handling.logger import Logger

class ScriptQueue:

    def __init__(self, script_names: list):
        self.scripts = script_names
        self.logger = Logger('script_queue', 'critical')

    def run(self):
        for script in self.scripts:
            script += '.py'
            self.logger.info(f'Starting script {script}')
            p = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

            exit_code = p.wait()
            if exit_code != 0:
                p.terminate()
                self.logger.critical(f'Process terminated with errors: {script}')
                exit(1)