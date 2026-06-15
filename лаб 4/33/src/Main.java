public class Main {

    public static void main(String[] args) {
        City a = new City("A");
        City b = new City("B");
        City c = new City("C");
        City d = new City("D");
        City e = new City("E");
        City f = new City("F");

        a.addRoute(b, 5);
        a.addRoute(f, 1);
        a.addRoute(d, 6);

        f.addRoute(b, 1);
        f.addRoute(e, 2);

        b.addRoute(c, 3);

        e.addRoute(d, 2);

        d.addRoute(c, 4);

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