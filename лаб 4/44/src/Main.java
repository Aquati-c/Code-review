public class Main {

    public static void main(String[] args) {
        City c = new City("C");

        City d = new City(
                "D",
                new Route(c, 4)
        );

        City e = new City(
                "E",
                new Route(d, 2)
        );

        City b = new City(
                "B",
                new Route(c, 3)
        );

        City f = new City(
                "F",
                new Route(b, 1),
                new Route(e, 2)
        );

        City a = new City(
                "A",
                new Route(b, 5),
                new Route(f, 1),
                new Route(d, 6)
        );

        System.out.println("Города и пути между ними:");
        System.out.println();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
    }
}