import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

/**
 * Условие задачи:
 * 1. Модернизировать класс Город (City): поддержка создания только по имени, 
 * а также по имени и готовому набору путей.
 * 2. Создать класс Маршрут (Route):
 * - Инициализация и изменение точек начала/конца строго не null и за O(1).
 * - Метод получения массива (или списка) городов, составляющих последовательный путь.
 * - Текстовое представление маршрута.
 * 3. Построить граф из Рис. 2 и вывести маршрут из F в D.
 */
public class Main {

    /**
     * Точка входа в программу (Аналог if __name__ == "__main__").
     */
    public static void main(String[] args) {
        // Тестирование требования 1: Создание городов разными способами
        City a = new City("A");
        City b = new City("B");
        City c = new City("C");
        City d = new City("D");
        City e = new City("E");

        // Город F создаем сразу со списком связанных городов (связываем с B, стоимость 1)
        Map<City, Integer> initialRoadsForF = new HashMap<>();
        initialRoadsForF.put(b, 1);
        City f = new City("F", initialRoadsForF);

        // Достраиваем остальную конфигурацию карты с Рисунка 2
        a.addRoad(f, 1);
        a.addRoad(d, 6);
        b.addRoad(a, 5);
        b.addRoad(c, 3);
        c.addRoad(d, 4);
        d.addRoad(e, 2);
        d.addRoad(b, 3);
        e.addRoad(f, 2);

        System.out.println("=== Карта городов успешно инициализирована ===");

        try {
            // Тестирование требования 2: Инициализация маршрута из F в D
            System.out.println("\n--- Создание маршрута F -> D ---");
            Route route = new Route(f, d);

            // Вывод строкового представления
            System.out.println("Текстовый вид маршрута: " + route);

            // Получение маршрута в виде массива
            City[] pathArray = route.getPathAsArray();
            System.out.print("Элементы массива городов: ");
            for (City city : pathArray) {
                System.out.print(city.getName() + " ");
            }
            System.out.println();

            // Демонстрация динамического изменения точек за O(1)
            System.out.println("\n--- Смена начальной точки маршрута на 'E' (Маршрут E -> D) ---");
            route.setStart(e);
            System.out.println("Новый маршрут: " + route);

            // Проверка защиты от некорректного ввода (null)
            System.out.println("\n--- Проверка защиты от null ---");
            route.setEnd(null);

        } catch (IllegalArgumentException ex) {
            // Конкретная обработка ошибок валидации
            System.out.println("[Перехвачена ошибка]: " + ex.getMessage());
        }
    }
}

/**
 * Сущность Город (Узел направленного взвешенного графа).
 */
class City {
    private final String name;
    private final Map<City, Integer> roads;

    /**
     * Конструктор: Создание города только по названию.
     * Args:
     * name (String): Название города.
     */
    public City(String name) {
        this.name = name;
        this.roads = new HashMap<>();
    }

    /**
     * Конструктор: Создание города с названием и готовым набором путей.
     * Args:
     * name (String): Название города.
     * initialRoads (Map): Карта путей {Город-назначения: Стоимость}.
     */
    public City(String name, Map<City, Integer> initialRoads) {
        this.name = name;
        this.roads = new HashMap<>();
        if (initialRoads != null) {
            this.roads.putAll(initialRoads);
        }
    }

    public String getName() {
        return name;
    }

    public Map<City, Integer> getRoads() {
        return roads;
    }

    /**
     * Добавляет или изменяет прямую дорогу до целевого города.
     */
    public void addRoad(City targetCity, int cost) {
        if (targetCity == this) {
            throw new IllegalArgumentException("Нельзя построить дорогу в самого себя.");
        }
        this.roads.put(targetCity, cost);
    }
}

/**
 * Сущность Маршрут между двумя городами.
 */
class Route {
    private City start;
    private City end;

    /**
     * Конструктор маршрута. Гарантирует создание за O(1).
     */
    public Route(City start, City end) {
        if (start == null || end == null) {
            throw new IllegalArgumentException("Точки начала и конца пути не могут быть null!");
        }
        this.start = start;
        this.end = end;
    }

    /**
     * Изменение точки старта. Выполняется за константное время O(1).
     */
    public void setStart(City start) {
        if (start == null) {
            throw new IllegalArgumentException("Точка начала пути не может быть null!");
        }
        this.start = start;
    }

    /**
     * Изменение точки финиша. Выполняется за константное время O(1).
     */
    public void setEnd(City end) {
        if (end == null) {
            throw new IllegalArgumentException("Точка конца пути не может быть null!");
        }
        this.end = end;
    }

    public City getStart() {
        return start;
    }

    public City getEnd() {
        return end;
    }

    /**
     * Находит кратчайший по количеству городов путь (BFS) и возвращает его в виде массива.
     * Returns:
     * City[]: Массив городов от start до end включительно. Пустой массив, если путь не найден.
     */
    public City[] getPathAsArray() {
        if (start == end) {
            return new City[]{start};
        }

        // Очередь для BFS обхода
        Queue<City> queue = new LinkedList<>();
        // Мапа для отслеживания предков: {город: откуда мы в него пришли}
        Map<City, City> parentMap = new HashMap<>();
        Set<City> visited = new HashSet<>();

        queue.add(start);
        visited.add(start);

        boolean pathFound = false;

        while (!queue.isEmpty()) {
            City current = queue.poll();

            if (current == end) {
                pathFound = true;
                break;
            }

            for (City neighbor : current.getRoads().keySet()) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    parentMap.put(neighbor, current);
                    queue.add(neighbor);
                }
            }
        }

        if (!pathFound) {
            return new City[0]; // Возвращаем пустой массив, если путь отсутствует
        }

        // Восстанавливаем путь с конца в начало
        List<City> pathList = new ArrayList<>();
        City curr = end;
        while (curr != null) {
            pathList.add(curr);
            curr = parentMap.get(curr);
        }

        // Разворачиваем, чтобы порядок стал от Старта к Финишу
        Collections.reverse(pathList);
        return pathList.toArray(new City[0]);
    }

    /**
     * Приведение маршрута к строке.
     * Возвращает названия всех городов по порядку.
     */
    @Override
    public String toString() {
        City[] path = getPathAsArray();
        if (path.length == 0) {
            return "Маршрут невозможен (путь между " + start.getName() + " и " + end.getName() + " отсутствует)";
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < path.length; i++) {
            sb.append(path[i].getName());
            if (i < path.length - 1) {
                sb.append(" -> ");
            }
        }
        return sb.toString();
    }
}