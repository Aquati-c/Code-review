import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.TreeMap;

/**
 * Условие задачи:
 * Переопределить метод сравнения объектов по состоянию (equals) так,
 * чтобы два Города считались одинаковыми тогда, когда у них одинаковый
 * набор путей в другие города[cite: 106]. Подвид Города должен быть сравним
 * с базовым Городом[cite: 106]. Исправлено: защита от StackOverflowError.
 */
public class Main {

    /**
     * Точка входа в программу.
     * Демонстрирует корректность работы сравнения и отсутствие рекурсии[cite: 25].
     */
    public static void main(String[] args) {
        // Создаем вспомогательные города-ориентиры
        City targetX = new City("X");
        City targetY = new City("Y");

        System.out.println("=== 1. Тестирование базовых городов (задача 2.1.10) ===");
        City alpha = new City("Альфа");
        City beta = new City("Бета");

        // Имена разные, путей нет -> они должны быть равны
        System.out.println("Альфа равен Бета (без дорог)? " + alpha.equals(beta)); // true

        // Добавляем одинаковые дороги в оба города
        alpha.addRoad(targetX, 10);
        alpha.addRoad(targetY, 5);

        beta.addRoad(targetX, 10);
        beta.addRoad(targetY, 5);

        System.out.println("Альфа равен Бета (одинаковые дороги)? " + alpha.equals(beta)); // true

        System.out.println("\n=== 2. Тестирование с подвидом города (задача 2.3.3) ===");
        // Создаем подкласс (двусторонний город), который вызывал ошибку StackOverflowError
        TwoWayCity gamma = new TwoWayCity("Гамма");

        // Гамма автоматически свяжется с X и Y, а они свяжутся с Гаммой в ответ
        gamma.addRoad(targetX, 10);
        gamma.addRoad(targetY, 5);

        // ТЕПЕРЬ ОШИБКИ НЕТ: Безопасное полиморфное сравнение (Liskov Substitution) [cite: 77]
        System.out.println("Базовый 'Альфа' равен подвиду 'Гамма'? " + alpha.equals(gamma)); // true
        System.out.println("Подвид 'Гамма' равен базовому 'Альфа'? " + gamma.equals(alpha)); // true

        // Проверяем, что хэш-коды также абсолютно одинаковы
        System.out.println("Хэш-код Альфа: " + alpha.hashCode());
        System.out.println("Хэш-код Гамма: " + gamma.hashCode());
    }
}

/**
 * Базовая сущность Город (из задачи 2.1.10).
 */
class City {
    protected final String name;
    protected final Map<City, Integer> roads;

    /**
     * Конструктор города[cite: 4].
     * Args:
     * name (String): Название города[cite: 8].
     */
    public City(String name) {
        this.name = name;
        this.roads = new HashMap<>();
    }

    public String getName() {
        return name;
    }

    public Map<City, Integer> getRoads() {
        return roads;
    }

    /**
     * Добавляет или изменяет дорогу до целевого города.
     */
    public void addRoad(City targetCity, int cost) {
        if (targetCity == this) {
            throw new IllegalArgumentException("Нельзя построить дорогу в самого себя.");
        }
        this.roads.put(targetCity, cost);
    }

    /**
     * Преобразует карту дорог в плоскую отсортированную структуру {Имя_Города: Стоимость}.
     * Это разрывает циклическую связь ссылок объектов при расчете equals/hashCode (KISS).
     */
    private Map<String, Integer> getFlatRoadsMap() {
        Map<String, Integer> flatMap = new TreeMap<>();
        for (Map.Entry<City, Integer> entry : this.roads.entrySet()) {
            flatMap.put(entry.getKey().getName(), entry.getValue());
        }
        return flatMap;
    }

    /**
     * Переопределенный метод сравнения по состоянию дорог.
     * Защищен от бесконечной рекурсии (StackOverflowError).
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (!(obj instanceof City)) {
            return false; // Убираем лишний else по кодстайлу [cite: 26]
        }

        City other = (City) obj;

        // Сравниваем плоские карты "Имя_Соседа -> Стоимость" вместо сравнения самих объектов
        return Objects.equals(this.getFlatRoadsMap(), other.getFlatRoadsMap());
    }

    /**
     * Хэш-код генерируется на основе плоской карты путей.
     */
    @Override
    public int hashCode() {
        return Objects.hash(this.getFlatRoadsMap());
    }

    @Override
    public String toString() {
        return "Город " + name + " (Дорог: " + roads.size() + ")";
    }
}

/**
 * Подвид сущности Город (из задачи 2.3.3)[cite: 77].
 */
class TwoWayCity extends City {

    public TwoWayCity(String name) {
        super(name);
    }

    @Override
    public void addRoad(City targetCity, int cost) {
        super.addRoad(targetCity, cost);

        // Автоматический обратный путь (DRY) [cite: 32]
        if (!targetCity.getRoads().containsKey(this) || targetCity.getRoads().get(this) != cost) {
            targetCity.getRoads().put(this, cost);
        }
    }
}