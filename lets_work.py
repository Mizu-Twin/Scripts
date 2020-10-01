import datetime, os
        
# Preset file paths for working files
w_dir = os.path.dirname(__file__) + '../'
done_path = w_dir + '_done/'
t_path = 'templates/'
log_file = 'log'

# Files to be copied for work
#appendix = 'Job Card Appendix.xlsx'
#job_card = 'Job Card.doc'
#unresolved = 'Unresolved.xlsx'
template = 'Job Card.xltx'
template2 = 'Troubleshooting.xltx'
files_to_copy = [template]

def copy_work_files(w, t, f2c):
    """Copies templates to working directory"""
    for t_file in f2c:
        with open('../' + (str(today) + ' - ' + t_file), 'wb') as f:
            new_file = f
            with open((w + t + t_file), 'rb') as f_1:
                new_file.write(f_1.read())
                with open(done_path + log_file, 'a') as f_2:
                    log = '[Template] '
                    log += str(today) + ' - ' + t_file + ' copied.\n'
                    f_2.write(log)


# Use today's date in variable & copy work files
today = datetime.date.today()
copy_work_files(w_dir, t_path, files_to_copy)

"""# Before overwriting current work, copying files in temp dir
temp_dir = os.path.join(script_dir, 'temp/')"""


            

        
