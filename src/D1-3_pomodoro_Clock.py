# Pomodoro Clock

import time

def countdown(type, user_time):
    log_file_path = "D:\\Devlopment_Workspace\\100DoC_in_Py\\src\\D1-3_pomodoro_log.txt"
    log_file = open(log_file_path, "a")
    for x in range(user_time, 0, -1):
        seconds = x % 60
        minutes = int((x/60)%60)
        hours = int(x/3600)
        print(f"{type} : {hours:02}:{minutes:02}:{seconds:02}")
        log_file.write(f"{type} : {hours:02}:{minutes:02}:{seconds:02}\n")
        time.sleep(1)
    log_file.close()

def main():
    work_sessions = 5
    short_break_sessions = work_sessions - 1
    work_time = 1500
    short_break_time = 300
    long_break_time = 900
    work_session_counter = 0
    short_break_counter = 0
    long_break_counter = 0

    # added to truncate the file (clear the file) before we start a new run.
    log_file_path = "D:\\Devlopment_Workspace\\100DoC_in_Py\\src\\D1-3_pomodoro_log.txt"
    with open(log_file_path, "r+") as file:
        file.truncate(0)

    while work_sessions > 0:
        countdown(f"WORK {work_session_counter+1}", work_time)
        work_sessions -= 1
        work_session_counter += 1
        # checks for short break - 
        # 1. short_break_sessions > 0 ==> if short break counter is greater than 0 
        # AND
        # 2. work_sessions != 0 ==> is the work session that ran before the last work sesson. If yes then there should be no breaks.
        # AND
        # 3. work_session_counter % 4 != 0 ==> check for long break (should there be a long break ?)
        if short_break_sessions > 0 and work_sessions != 0 and work_session_counter % 4 != 0:
            print(str(work_sessions) + " : "+ str(work_session_counter))
            countdown(f"SHORT BREAK {short_break_counter+1}", short_break_time)
            short_break_sessions -= 1
            short_break_counter += 1
        # check for long break - long break after every 4th work session
        # work_session_counter % 4 == 0 (was the last worksession the 4th (8/12/16...) one)
        if work_session_counter % 4 == 0:
            countdown(f"LONG BREAK {long_break_counter+1}", long_break_time)
            long_break_counter += 1
    
    print(work_session_counter)
    print(short_break_counter)
    print(long_break_counter)











if __name__ == "__main__":
    main()