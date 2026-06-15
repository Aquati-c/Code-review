import java.util.Random;

/**
 * Условие задачи:
 * 1. Создать абстрактную сущность Птица (Bird) как корень иерархии.
 * 2. Реализовать подкласс Воробей (Sparrow), поющий "чырык".
 * 3. Реализовать подкласс Кукушка (Cuckoo), поющий "ку-ку" случайное число раз (от 1 до 10).
 * 4. Реализовать подкласс Попугай (Parrot), поющий случайные первые N символов заданного текста.
 */
public class Main {

    /**
     * Точка входа в программу (Аналог if __name__ == "__main__").
     * Отвечает за демонстрацию полиморфного поведения птичьего хора.
     */
    public static void main(String[] args) {
        System.out.println("=== Инициализация птичьего хора ===");

        try {
            // Создаем массив птиц (проявление полиморфизма)
            Bird[] choir = new Bird[] {
                    new Sparrow("Воробей Кеша"),
                    new Cuckoo("Кукушка Марта"),
                    new Parrot("Попугай Рома", "Я умный попугай и умею разговаривать!")
            };

            // Каждая птица поет по-своему в едином цикле
            for (Bird bird : choir) {
                System.out.println("\n--- Поет " + bird.getName() + " ---");
                bird.sing();
            }

            // Демонстрация защиты от некорректного ввода (null или пустой текст у попугая)
            System.out.println("\n--- Проверка защиты от некорректных данных ---");
            Bird brokenParrot = new Parrot("Попугай-молчун", "   ");

        } catch (IllegalArgumentException ex) {
            // Перехватываем конкретное ожидаемое исключение валидации
            System.out.println("[Ошибка инициализации]: " + ex.getMessage());
        }
    }
}

/**
 * Абстрактный класс Птица. 
 * Является корнем иерархии и инкапсулирует общие свойства (имя) и общее поведение (пение).
 */
abstract class Bird {
    protected String name;
    protected Random random; // Общий генератор случайных чисел для подклассов

    /**
     * Конструктор птицы.
     * * Args:
     * name (String): Кличка или вид птицы.
     */
    public Bird(String name) {
        this.name = name;
        this.random = new Random();
    }

    public String getName() {
        return name;
    }

    /**
     * Абстрактный метод пения. Каждая птица обязана реализовать его по-своему.
     */
    public abstract void sing();
}

/**
 * Сущность Воробей.
 */
class Sparrow extends Bird {

    public Sparrow(String name) {
        super(name);
    }

    /**
     * Воробей всегда поет "чырык".
     */
    @Override
    public void sing() {
        System.out.println("чырык");
    }
}

/**
 * Сущность Кукушка.
 */
class Cuckoo extends Bird {

    public Cuckoo(String name) {
        super(name);
    }

    /**
     * Кукушка поет "ку-ку" случайное количество раз в диапазоне от 1 до 10.
     */
    @Override
    public void sing() {
        // nextInt(10) дает 0..9, прибавляем 1 для получения диапазона 1..10
        int count = random.nextInt(10) + 1;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count; i++) {
            sb.append("ку-ку");
            if (i < count - 1) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString() + " (Повторений: " + count + ")");
    }
}

/**
 * Сущность Попугай.
 */
class Parrot extends Bird {
    private final String speechText;

    /**
     * Конструктор попугая с обязательной валидацией текста.
     * * Args:
     * name (String): Кличка попугая.
     * speechText (String): Текст, который попугай запомнил для пения.
     */
    public Parrot(String name, String speechText) {
        super(name);
        if (speechText == null || speechText.strip().isEmpty()) {
            throw new IllegalArgumentException("Попугай не может быть создан без текста для пения!");
        }
        this.speechText = speechText.strip();
    }

    /**
     * Попугай поет первые N символов своего текста, где N определяется случайно.
     * Число N составляет минимум 1 символ и максимум длину всего текста.
     */
    @Override
    public void sing() {
        // Длина текста
        int textLength = speechText.length();

        // По условию: не менее одного и не более всех символов текста.
        // nextInt(textLength) дает диапазон 0 .. (textLength - 1). 
        // Прибавляя 1, получаем строгий диапазон от 1 до textLength включительно.
        int n = random.nextInt(textLength) + 1;

        // Вырезаем подстроку от 0 до N
        String partialSong = speechText.substring(0, n);
        System.out.println('"' + partialSong + "...\" (Спето символов: " + n + " из " + textLength + ")");
    }
}