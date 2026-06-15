public class Main {

    public static void main(String[] args) {
        System.out.println("Созданные имена:");
        System.out.println();

        Name cleopatra = new Name("Клеопатра");

        Name pushkin = new Name(
                "Пушкин",
                "Александр",
                "Сергеевич"
        );

        Name mayakovsky = new Name(
                "Маяковский",
                "Владимир"
        );

        System.out.println(cleopatra);
        System.out.println(pushkin);
        System.out.println(mayakovsky);
    }
}
