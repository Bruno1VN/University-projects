package exercicio_opcional;

import java.util.Arrays;
import java.util.Optional;

public class Department {
    private String name;
    private int code;
    private String location;
    private int phoneExtension;
    private Double budget;
    private Employee[] staff;
    private Employee chief;
    private int i = 0;
    public void addEmployee(Employee e){
        this.staff[this.i] = e;
        this.i++;
    }
    public void removeEmployee(Employee e){

    }
    public void removeEmployee(long id){
        System.out.println("---------------------------");
        System.out.println("Removendo o funcionario de id: "+ id);
        for (int i = 0; i < this.i; i++) {
            Employee currentEmployee = this.staff[i];
            long employeeId = currentEmployee.getId();
            if (id == employeeId) {
                this.staff[i] = null;
            }
        }
    }
    public void listAllEmployees(){
        System.out.println("Os funcionarios sao: ");
        for (int i = 0; i < this.i; i++){
            this.staff[i].printState();
        }
    }
    public int sizeOfEmployees(){
        System.out.println("O tamanho do departamento e: ");
        int size = 0;
        for (int i = 0; i < this.i; i++){
            Employee currentEmployee = this.staff[i];
            if (null != currentEmployee) {
                long employeeId = currentEmployee.getId();
                if (employeeId > -1){
                    size++;
                }
            }

        }
        return size;
    }
    public Employee getEmployee(long id){
        System.out.println("Buscando funcionario pelo ID: " + id);
        Employee employee = new Employee(null,-1,-1,null);
        for (int i = 0; i < this.i; i++){
            Employee currentEmployee = this.staff[i];
            long employeeId = currentEmployee.getId();
            if (id == employeeId){
                employee = currentEmployee;

            }else
                System.out.println("não existe");
        }
        return employee;
    }

    public Department(String name, int code, String location, int phoneExtension, Double budget) {
        this.name = name;
        this.code = code;
        this.location = location;
        this.phoneExtension = phoneExtension;
        this.budget = budget;
        this.staff = new Employee[100];
    }
}
