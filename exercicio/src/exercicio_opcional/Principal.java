package exercicio_opcional;

import java.util.Arrays;

public class Principal{
    public static void executar(String[] args) {
        Employee e = new Employee("Funci", 0, 1200, "programador");
        Employee e1 = new Employee("Funci1", 1, 1200, "programador");
        Employee e2 = new Employee("Funci2", 2, 1200, "programador");
        Employee e3 = new Employee("Funci3", 3, 2000, "programador");
        Employee e4 = new Employee("Funci4", 4, 5000, "Senior");
        Employee e5 = new Employee("Funci5", 5, 10000, "lider");
        Employee e6 = new Employee("Funci6", 6, 10000, "lider");

        Department department = new Department("depart1", 1, "SC", 16, 20000.0);
        Department department2 = new Department("depart2", 2, "SP", 11, 50000.0);
        Department department3 = new Department("depart3", 3, "NY", 555, 1000000.0);

        department.addEmployee(e);

        department.listAllEmployees();

        e.getAnnualSalary();

        department.getEmployee(0).printState();
        department.removeEmployee(0);
        department.getEmployee(0).printState();

        System.out.println(department.sizeOfEmployees());
    }

}
