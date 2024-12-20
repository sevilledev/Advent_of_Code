reports_list = open("puzzle.txt", "r").read().splitlines()
safe_count = 0


def check(report_list):
    report_type = 'asc' if report_list[1] - report_list[0] > 0 else 'desc'
    
    for i in range(len(report_list) - 1):
        diff = report_list[i + 1] - report_list[i]
        
        if (report_type == 'asc' and (diff > 3 or diff < 1)):
            return False
        elif (report_type == 'desc' and (diff < -3 or diff > -1)):
            return False
    return True
        
        
for report in reports_list:
    report_list = [int(n) for n in report.split()]
    is_safe = check(report_list)
    if(is_safe): safe_count += 1


print(safe_count)