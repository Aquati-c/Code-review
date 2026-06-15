import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * Условие задачи:
 * Создайте сущность Город, которая будет представлять собой точку на карте.
 * Характеристики: Название города, Набор путей к следующим городам (Город + стоимость).
 * Город возвращает текстовое представление вида "название (сосед:стоимость)".
 * Гарантируйте, что между двумя городами может быть только одна прямая дорога 
 * в одном направлении. Дороги можно добавлять и удалять в любой момент времени.
 * Реализуйте схему, представленную на рисунке 2.
 */
public class Main {

    /**
     * Точка входа в программу (Аналог if __name__ == "__main__").
     * Отвечает за построение графа и дружественный интерфейс.
     */
    public static void main(String[] args) {
        // Инициализируем города согласно Рис. 2
        City a = new City("A");
        City b = new City("B");
        City c = new City("C");
        City d = new City("D");
        City e = new City("E");
        City f = new City("F");

        // Строим исходную конфигурацию дорог (Рис. 2)
        a.addRoad(f, 1);
        a.addRoad(d, 6);
        b.addRoad(a, 5);
        b.addRoad(c, 3);
        c.addRoad(d, 4);
        d.addRoad(e, 2);
        d.addRoad(b, 3);
        e.addRoad(f, 2);
        f.addRoad(b, 1);

        // Мапа для удобного поиска объектов городов по имени при вводе пользователем
        Map<String, City> registry = new HashMap<>();
        for (City city : new City[]{a, b, c, d, e, f}) {
            registry.put(city.getName().toUpperCase(), city);
        }

        Scanner scanner = new Scanner(System.in);
        System.out.println("=== Текущее состояние транспортной сети (Рис. 2) ===");
        printGraph(registry);

        // Интерактивный цикл с защитой от некорректного ввода
        while (true) {
            System.out.println("\nДоступные действия:");
            System.out.println("1. Посмотреть карту дорог");
            System.out.println("2. Добавить / изменить дорогу");
            System.out.println("3. Удалить дорогу");
            System.out.println("4. Выйти");
            System.out.print("Выберите пункт меню: ");

            String choice = scanner.nextLine().strip();

            if (choice.equals("4")) {
                System.out.println("Программа завершена. Счастливого пути!");
                break;
            }

            try {
                switch (choice) {
                    case "1":
                        printGraph(registry);
                        break;
                    case "2":
                        handleChooseRoad(scanner, registry, true);
                        break;
                    case "3":
                        handleChooseRoad(scanner, registry, false);
                        break;
                    default:
                        System.out.println("[Ошибка]: Неверный пункт меню. Введите число от 1 до 4.");
                }
            } catch (IllegalArgumentException ex) {
                // Ловим конкретное ожидаемое исключение с пояснением причины пользователю
                System.out.println("[Ошибка ввода]: " + ex.getMessage());
            } catch (Exception ex) {
                // Глобальный перехват непредвиденных ситуаций для стабильности UI
                System.out.println("[Критическая ошибка]: Что-то пошло не так. Попробуйте снова.");
            }
        }
        scanner.close();
    }

    /**
     * Выводит всю карту городов в консоль.
     */
    private static void printGraph(Map<String, City> registry) {
        System.out.println("--------------------------------------------------");
        for (City city : registry.values()) {
            System.out.println(city);
        }
        System.out.println("--------------------------------------------------");
    }

    /**
     * Обработчик UI для добавления или удаления дорог с валидацией данных.
     *
     * Args:
     * scanner (Scanner): Поток ввода.
     * registry (Map): Зарегистрированные города.
     * isAddMode (boolean): true для добавления/изменения, false для удаления.
     */
    private static void handleChooseRoad(Scanner scanner, Map<String, City> registry, boolean isAddMode) {
        System.out.print("Введите имя исходного города (А-F): ");
        String fromStr = scanner.nextLine().strip().toUpperCase();
        System.out.print("Введите имя целевого города (A-F): ");
        String toStr = scanner.nextLine().strip().toUpperCase();

        if (!registry.containsKey(fromStr) || !registry.containsKey(toStr)) {
            throw new IllegalArgumentException("Один или оба указанных города не существуют на карте!");
        }

        City fromCity = registry.get(fromStr);
        City toCity = registry.get(toStr);

        if (isAddMode) {
            System.out.print("Введите стоимость поездки (целое положительное число): ");
            String costStr = scanner.nextLine().strip();
            int cost;
            try {
                cost = Integer.parseInt(costStr);
                if (cost <= 0) {
                    throw new IllegalArgumentException();
                }
            } catch (Exception e) {
                // Локальная валидация парсинга числа
                throw new IllegalArgumentException("Стоимость должна быть целым числом больше нуля!");
            }

            fromCity.addRoad(toCity, cost);
            System.out.printf("[Успех]: Дорога %s -> %s со стоимостью %d обновлена/создана.\n", fromStr, toStr, cost);
            return; // Избегаем лишних else
        }

        // Режим удаления
        fromCity.removeRoad(toCity);
    }
}

/**
 * Сущность, представляющая город (Узел направленного взвешенного графа).
 * Отвечает принципу Single Responsibility (только хранение и атомарное изменение связей).
 */
class City {
    private final String name;

    // Использование HashMap гарантирует strict-ограничение: 1 ключ (City) = 1 ребро.
    // Никакие дубликаты путей между парой А -> Б физически не запишутся.
    private final Map<City, Integer> roads;

    /**
     * Конструктор города.
     * * Args:
     * name (String): Название города.
     */
    public City(String name) {
        this.name = name;
        this.roads = new HashMap<>();
    }

    public String getName() {
        return name;
    }

    /**
     * Добавляет прямую направленную дорогу или перезаписывает её стоимость,
     * если она уже существовала. Обеспечивает выполнение правила единственности дороги.
     */
    public void addRoad(City targetCity, int cost) {
        if (targetCity == this) {
            throw new IllegalArgumentException("Нельзя построить дорогу из города в самого себя.");
        }
        this.roads.put(targetCity, cost);
    }

    /**
     * Удаляет прямую дорогу в указанный город.
     */
    public void removeRoad(City targetCity) {
        if (!this.roads.containsKey(targetCity)) {
            throw new IllegalArgumentException("Прямого пути из " + this.name + " в " + targetCity.getName() + " не существует.");
        }
        this.roads.remove(targetCity);
        System.out.printf("[Успех]: Прямая дорога из %s в %s удалена.\n", this.name, targetCity.getName());
    }

    /**
     * Возвращает текстовое представление согласно требованиям задачи.
     * Сортирует связанные города по алфавиту для предсказуемости отображения.
     */
    @Override
    public String toString() {
        if (this.roads.isEmpty()) {
            return this.name + ": нет исходящих путей";
        }

        // TreeMap используется исключительно для автоматической сортировки по имени соседа при выводе
        Map<String, Integer> sortedMap = new TreeMap<>();
        for (Map.Entry<City, Integer> entry : this.roads.entrySet()) {
            sortedMap.put(entry.getKey().getName(), entry.getValue());
        }

        StringBuilder sb = new StringBuilder();
        sb.append(this.name).append(" (");

        boolean isFirst = true;
        for (Map.Entry<String, Integer> entry : sortedMap.entrySet()) {
            if (!isFirst) {
                sb.append(", ");
            }
            sb.append(entry.getKey()).append(":").append(entry.getValue());
            isFirst = false;
        }
        sb.append(")");

        return sb.toString();
    }
}