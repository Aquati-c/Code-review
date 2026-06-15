import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Создание первой точки");
        System.out.print("Введите координату X: ");
        double x1 = scanner.nextDouble();
        System.out.print("Введите координату Y: ");
        double y1 = scanner.nextDouble();

        Point firstPoint = new Point(x1, y1);

        System.out.println();

        System.out.println("Создание второй точки");
        System.out.print("Введите координату X: ");
        double x2 = scanner.nextDouble();
        System.out.print("Введите координату Y: ");
        double y2 = scanner.nextDouble();

        Point secondPoint = new Point(x2, y2);

        System.out.println();

        System.out.println("Создание третьей точки");
        System.out.print("Введите координату X: ");
        double x3 = scanner.nextDouble();
        System.out.print("Введите координату Y: ");
        double y3 = scanner.nextDouble();

        Point thirdPoint = new Point(x3, y3);

        System.out.println();
        System.out.println("Созданные точки:");
        System.out.println(firstPoint);
        System.out.println(secondPoint);
        System.out.println(thirdPoint);

        scanner.close();
    }
}