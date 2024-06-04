import re


def extract_qsub_commands(text):
    # 使用正则表达式提取所有 script_file 和 job_args
    script_file_pattern = r'script_file:\s*([^\s]+)'
    job_args_pattern = r'job_args:\s*([^\s]+)'

    script_files = re.findall(script_file_pattern, text)
    job_args_list = re.findall(job_args_pattern, text)

    if script_files and job_args_list and len(script_files) == len(job_args_list):
        qsub_commands = [f"qsub {script_file} {job_args}" for script_file, job_args in zip(script_files, job_args_list)]
        return qsub_commands
    else:
        return "Required parameters not found or mismatch in counts in the text."
    
# text = ""
with open("seed.txt","r") as f:
    text = f.read()

output = extract_qsub_commands(text)

with open("output.txt","w") as f:
    f.write("\n".join(output))

print(output)
