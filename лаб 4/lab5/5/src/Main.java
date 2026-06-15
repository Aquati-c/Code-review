import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Условие задачи:
 * Реализуйте граф, показанный на рисунке, используя в одной программе
 * сущности односторонней дороги и двусторонней дороги, применяя их там, 
 * где необходимо по схеме.
 * Односторонняя стрелка — перемещение только в одну сторону.
 * Двусторонняя стрелка — перемещение в обоих направлениях.
 */
public class Main {

    /**
     * Точка входа в программу.
     * Отвечает за инициализацию графа согласно схеме и пользовательский интерфейс.
     */
    public static void main(String[] args) {
        // Создаем города, присутствующие на схеме 2.6.9
        City a = new City("A");
        City b = new City("B");
        City c = new City("C");
        City d = new City("D");
        City e = new City("E");

        // Мапа реестра для быстрого поиска по имени при взаимодействии с UI
        Map<String, City> registry = new HashMap<>();
        for (City city : new City[]{a, b, c, d, e}) {
            registry.put(city.getName().toUpperCase(), city);
        }

        // --- Строим граф по рисунку ---

        // 1. Двусторонние дороги (<->)
        new TwoWayRoad(a, b); // A <-> B
        new TwoWayRoad(b, d); // B <-> D

        // 2. Односторонние дороги (->)
        new OneWayRoad(a, c); // A -> C
        new OneWayRoad(b, c); // B -> C
        new OneWayRoad(e, c); // E -> C
        new OneWayRoad(e, d); // E -> D

        System.out.println("=== Граф задачи 2.6.9 успешно инициализирован ===");
        printGraph(registry);

        // Интерактивный блок проверки доступных путей с защитой от дурака
        Scanner scanner = new Scanner(System.in);
        System.out.println("\n=== Интерактивная проверка прямых путей ===");

        try {
            System.out.print("Введите город отправления (A-E): ");
            String fromStr = scanner.nextLine().strip().toUpperCase();

            System.out.print("Введите город назначения (A-E): ");
            String toStr = scanner.nextLine().strip().toUpperCase();

            if (!registry.containsKey(fromStr) || !registry.containsKey(toStr)) {
                throw new IllegalArgumentException("Один или оба указанных города не найдены на карте!");
            }

            City fromCity = registry.get(fromStr);
            City toCity = registry.get(toStr);

            if (fromCity.hasDirectPathTo(toCity)) {
                System.out.printf("[Результат]: Да, существует прямой путь из %s в %s.\n", fromStr, toStr);
                return; // Избегаем избыточного else
            }

            System.out.printf("[Результат]: Прямого пути из %s в %s НЕТ.\n", fromStr, toStr);

        } catch (IllegalArgumentException ex) {
            System.out.println("[Ошибка ввода]: " + ex.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Выводит список всех городов и направления путей из них.
     */
    private static void printGraph(Map<String, City> registry) {
        System.out.println("--------------------------------------------------");
        for (City city : registry.values()) {
            System.out.println(city);
        }
        System.out.println("--------------------------------------------------");
    }
}

/**
 * Сущность Город. Хранит информацию о вершине графа и её исходящих ребрах.
 */
class City {
    private final String name;
    private final List<Edge> outgoingEdges;

    public City(String name) {
        this.name = name;
        this.outgoingEdges = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    /**
     * Регистрация исходящей дороги из данного города.
     */
    public void addEdge(Edge edge) {
        if (edge == null) {
            throw new IllegalArgumentException("Дорога не может быть null.");
        }
        this.outgoingEdges.add(edge);
    }

    /**
     * Проверяет, есть ли прямое ребро из текущего города в целевой.
     */
    public boolean hasDirectPathTo(City target) {
        for (Edge edge : outgoingEdges) {
            if (edge.getTarget().equals(target)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public String toString() {
        if (outgoingEdges.isEmpty()) {
            return name + " -> (нет исходящих путей)";
        }

        StringBuilder sb = new StringBuilder();
        sb.append("Из города ").append(name).append(" можно уехать в: ");

        for (int i = 0; i < outgoingEdges.size(); i++) {
            sb.append(outgoingEdges.get(i).getTarget().getName());
            sb.append(" (").append(outgoingEdges.get(i).getTypeDescription()).append(")");
            if (i < outgoingEdges.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.toString();
    }
}

/**
 * Абстрактный класс Дорога (Ребро графа).
 * Соответствует принципу Open/Closed (SOLID) — готов к расширению новыми типами дорог.
 */
abstract class Edge {
    protected final City source;
    protected final City target;

    public Edge(City source, City target) {
        if (source == null || target == null) {
            throw new IllegalArgumentException("Города отправления и назначения должны быть указаны.");
        }
        if (source.equals(target)) {
            throw new IllegalArgumentException("Дорога не может вести из города в самого себя.");
        }
        this.source = source;
        this.target = target;
    }

    public City getTarget() {
        return target;
    }

    /**
     * Возвращает текстовое описание типа дороги (односторонняя/двусторонняя).
     */
    public abstract String getTypeDescription();
}

/**
 * Сущность Односторонняя дорога.
 */
class OneWayRoad extends Edge {

    public OneWayRoad(City source, City target) {
        super(source, target);
        // Регистрируем дорогу только у города-источника
        source.addEdge(this);
    }

    @Override
    public String getTypeDescription() {
        return "односторонняя";
    }
}

/**
 * Сущность Двусторонняя дорога.
 * Соответствует принципу DRY — избавляет от необходимости вручную прописывать обратный путь.
 */
class TwoWayRoad extends Edge {

    public TwoWayRoad(City source, City target) {
        super(source, target);

        // Регистрируем прямое направление (source -> target)
        source.addEdge(this);

        // Автоматически создаем и регистрируем обратное ребро (target -> source)
        // Чтобы не уходить в бесконечную рекурсию конструкторов, создаем анонимное одностороннее 
        // ребро со специальным описанием, либо просто добавляем объект в списки.
        target.addEdge(new Edge(target, source) {
            @Override
            public String getTypeDescription() {
                return "двусторонняя, обратное направление";
            }
        });
    }

    @Override
    public String getTypeDescription() {
        return "двусторонняя";
    }
} 