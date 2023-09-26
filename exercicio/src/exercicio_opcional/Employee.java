package exercicio_opcional;

public class Employee {
    private String name;
    private long id;
    private double salary;
    private String jobTitle;
    private String dept;
    private Department deptInCharge;
    public void printState(){
        System.out.println("---------------------------");
        System.out.println("Funcionario: " + this.name);
        System.out.println("id: " + this.id);
        System.out.println("salary: " + this.salary);
        System.out.println("Cargo: " + this.jobTitle);
        System.out.println("---------------------------");

    }
    public void getAnnualSalary(){
        System.out.println("O salario anual de "+ this.name + " e de : "+ this.salary * 12);
    }

    public void getDept(){

    }
    public long getId(){
        return this.id;
    }
    public Employee(String name, long id, double salary, String jobTitle) {
        this.name = name;
        this.id = id;
        this.salary = salary;
        this.jobTitle = jobTitle;
    }
}
