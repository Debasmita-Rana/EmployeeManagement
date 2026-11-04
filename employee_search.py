def search_employee(employees, search_name):
    results = []

    for employee in employees:
        if search_name.lower() in employee["name"].lower():
            results.append(employee)

    return results
