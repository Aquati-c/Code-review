public class Fraction {

    private final int numerator;
    private final int denominator;

    public Fraction(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public Fraction sum(Fraction other) {
        int newNumerator =
                numerator * other.denominator
                        + other.numerator * denominator;

        int newDenominator =
                denominator * other.denominator;

        return new Fraction(newNumerator, newDenominator);
    }

    public Fraction sum(int number) {
        return sum(new Fraction(number, 1));
    }

    public Fraction minus(Fraction other) {
        int newNumerator =
                numerator * other.denominator
                        - other.numerator * denominator;

        int newDenominator =
                denominator * other.denominator;

        return new Fraction(newNumerator, newDenominator);
    }

    public Fraction minus(int number) {
        return minus(new Fraction(number, 1));
    }

    public Fraction mult(Fraction other) {
        return new Fraction(
                numerator * other.numerator,
                denominator * other.denominator
        );
    }

    public Fraction mult(int number) {
        return new Fraction(
                numerator * number,
                denominator
        );
    }

    public Fraction div(Fraction other) {
        return new Fraction(
                numerator * other.denominator,
                denominator * other.numerator
        );
    }

    public Fraction div(int number) {
        return div(new Fraction(number, 1));
    }

    @Override
    public String toString() {
        return numerator + "/" + denominator;
    }
}
