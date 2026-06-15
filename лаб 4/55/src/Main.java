public class Main {

    public static void main(String[] args) {
        Fraction f1 = new Fraction(1, 3);
        Fraction f2 = new Fraction(2, 3);
        Fraction f3 = new Fraction(3, 4);

        System.out.println("Примеры операций с дробями:");
        System.out.println();

        System.out.println(
                f1 + " + " + f2 + " = " + f1.sum(f2)
        );

        System.out.println(
                f1 + " - " + f2 + " = " + f1.minus(f2)
        );

        System.out.println(
                f1 + " * " + f2 + " = " + f1.mult(f2)
        );

        System.out.println(
                f1 + " / " + f2 + " = " + f1.div(f2)
        );

        System.out.println();

        System.out.println(
                f1 + " + 5 = " + f1.sum(5)
        );

        System.out.println(
                f2 + " - 2 = " + f2.minus(2)
        );

        System.out.println(
                f3 + " * 3 = " + f3.mult(3)
        );

        System.out.println(
                f3 + " / 2 = " + f3.div(2)
        );

        System.out.println();

        Fraction result =
                f1.sum(f2)
                        .div(f3)
                        .minus(5);

        System.out.println(
                "f1.sum(f2).div(f3).minus(5) = "
                        + result
        );
    }
}
