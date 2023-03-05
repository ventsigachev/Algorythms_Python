"""
    We have a hierarchy between the employees in a company.Employees can have one or several direct managers.
    People who manage nobody are called regular employees and their salaries are 1.
    People who manage at least one employee are called managers.
    Each manager takes a salary which is equal to the sum of the salaries of their directly managed employees.
    Managers cannot manage directly or indirectly themselves. Some employees might have no manager.
    The goal is to calculate the final budget.

    To solve the problem we will use list, as data structure, and Depth_First Search, to calculate salaries.
    The graph will be a list of lists, where index of the graph will represent the employee and the sub-list of the
    given index represents the managed employees, if any.
    If we have N employees, they will be indexed from 0 to N – 1. For each employee, you will be given a string with N
    symbols. The symbols are either 'Y' or 'N', showing all employees that are managed by the current employee.
    The managers are the rows in the graph, and the managed employees are the colons.
"""


def company_representation(employees, graph):
    if employees == 1:
        print("The company has only one employee.")
        return

    managers = {m: graph[m] for m in range(len(graph)) if len(graph[m])}

    print(f"Company has {employees} workers, {len(managers)} of them are managers.\n")

    for manager, employees in managers.items():
        print(f"Manager {manager} manages employee {''.join([str(x) for x in employees])}" if len(employees) == 1
              else f"Manager {manager} manages {' and '.join([str(x) for x in employees])} employees")


def main():
    employees = int(input())
    graph = []

    for _ in range(employees):
        string = input()
        
        managed_employees = [managed_employee for managed_employee, symbol in enumerate(string) if symbol == "Y"]

        graph.append(managed_employees)

    company_representation(employees, graph)


if __name__ == "__main__":
    main()


"""
    Possible Inputs:

1
N

4
NNYN
NNYN
NNNN
NYYN

6
NNNNNN
YNYNNY
YNNNNY
NNNNNN
YNYNNN
YNNYNN

"""
