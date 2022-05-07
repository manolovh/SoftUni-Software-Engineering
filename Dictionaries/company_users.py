command = input()

company_dict = {}
while command != 'End':
    info = command.split(' -> ')
    company_name = info[0]
    employee_id = info[1]
    if company_name not in company_dict:
        company_dict[company_name] = [employee_id]
    else:
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)

    command = input()

for company in company_dict:
    print(company)
    for employee in company_dict[company]:
        print(f"-- {employee}")