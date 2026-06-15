import java.util.Scanner;

/**
 * Условие задачи:
 * 1. Создать сущность Точка (Point2D) на двумерной плоскости с координатами X, Y
 * и текстовым представлением "{X;Y}". Создать три разные точки.
 * 2. Создать подвид сущности Точка — Трехмерная точка (Point3D), которая
 * добавляет координату Z и корректно расширяет функционал базового класса.
 */
public class Main {

    /**
     * Точка входа в программу (Аналог if __name__ == "__main__").
     * Отвечает за демонстрацию работы сущностей и пользовательский интерфейс.
     */
    public static void main(String[] args) {
        System.out.println("=== Часть 1: Двумерные точки ===");

        // Создаем три точки с разными координатами
        Point2D p1 = new Point2D(1.5, 3.0);
        Point2D p2 = new Point2D(-4.0, 0.0);
        Point2D p3 = new Point2D(7.2, -12.8);

        // Выводим их текстовое представление
        System.out.println("Точка 1: " + p1);
        System.out.println("Точка 2: " + p2);
        System.out.println("Точка 3: " + p3);

        System.out.println("\n=== Часть 2: Трехмерная точка ===");

        // Создаем трехмерную точку, используя наследование
        Point3D p3d = new Point3D(5.0, 2.3, -9.1);
        System.out.println("Трехмерная точка: " + p3d);

        // Интерактивный блок с защитой от некорректного ввода
        System.out.println("\n=== Интерактивное создание двумерной точки ===");
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Введите координату X: ");
            double userX = Double.parseDouble(scanner.nextLine().strip());

            System.out.print("Введите координату Y: ");
            double userY = Double.parseDouble(scanner.nextLine().strip());

            Point2D userPoint = new Point2D(userX, userY);
            System.out.println("[Успех] Ваша точка создана: " + userPoint);

        } catch (NumberFormatException ex) {
            // Перехватываем конкретную ошибку парсинга чисел (Защита от некорректного ввода)
            System.out.println("[Ошибка ввода]: Координаты должны быть вещественными или целыми числами!");
        } finally {
            scanner.close();
        }
    }
}

/**
 * Сущность двумерной точки на плоскости.
 * Отвечает принципу Single Responsibility (SOLID).
 */
class Point2D {
    // Поля защищены (protected), чтобы наследники имели к ним прямой доступ
    protected double x;
    protected double y;

    /**
     * Конструктор двумерной точки.
     * * Args:
     * x (double): Координата Х.
     * y (double): Координата Y.
     */
    public Point2D(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    /**
     * Возвращает текстовое представление в формате "{X;Y}".
     */
    @Override
    public String toString() {
        return "{" + x + ";" + y + "}";
    }
}

/**
 * Подвид сущности Точка, представляющий точку в трехмерном пространстве.
 * Пример правильного наследования и расширения функционала (Open/Closed Principle).
 */
class Point3D extends Point2D {
    private double z;

    /**
     * Конструктор трехмерной точки.
     * * Args:
     * x (double): Координата Х (передается в базовый класс).
     * y (double): Координата Y (передается в базовый класс).
     * z (double): Координата Z.
     */
    public Point3D(double x, double y, double z) {
        // Переиспользуем конструктор родительского класса (DRY)
        super(x, y);
        this.z = z;
    }

    public double getZ() {
        return z;
    }

    /**
     * Переопределение текстового представления для трех координат.
     * Формат: "{X;Y;Z}"
     */
    @Override
    public String toString() {
        // Избавляемся от дублирования кода форматирования скобок, аккуратно внедряя Z
        return "{" + x + ";" + y + ";" + z + "}";
    }
}