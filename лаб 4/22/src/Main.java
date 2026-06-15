public class Main {

    public static void main(String[] args) {
        Point point1 = new Point(1, 3);
        Point point2 = new Point(23, 8);

        Line line1 = new Line(point1, point2);

        Point point3 = new Point(5, 10);
        Point point4 = new Point(25, 10);

        Line line2 = new Line(point3, point4);

        Line line3 = new Line(
                line1.getStart(),
                line2.getEnd()
        );

        System.out.println("Исходные линии:");
        System.out.println(line1);
        System.out.println(line2);
        System.out.println(line3);

        line1.getStart().setX(10);
        line1.getStart().setY(20);

        line2.getEnd().setX(50);
        line2.getEnd().setY(30);

        System.out.println();
        System.out.println("После изменения первой и второй линий:");
        System.out.println(line1);
        System.out.println(line2);
        System.out.println(line3);

        line1.setStart(new Point(100, 100));

        System.out.println();
        System.out.println(
                "После изменения первой линии без изменения третьей:"
        );
        System.out.println(line1);
        System.out.println(line2);
        System.out.println(line3);
    }
}