public class Name {

    private final String surname;
    private final String firstName;
    private final String patronymic;

    public Name(String firstName) {
        this(null, firstName, null);
    }

    public Name(String surname, String firstName) {
        this(surname, firstName, null);
    }

    public Name(
            String surname,
            String firstName,
            String patronymic
    ) {
        this.surname = surname;
        this.firstName = firstName;
        this.patronymic = patronymic;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();

        if (surname != null) {
            result.append(surname);
        }

        if (firstName != null) {
            if (!result.isEmpty()) {
                result.append(" ");
            }

            result.append(firstName);
        }

        if (patronymic != null) {
            if (!result.isEmpty()) {
                result.append(" ");
            }

            result.append(patronymic);
        }

        return result.toString();
    }
}
