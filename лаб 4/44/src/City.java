import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class City {

    private final String name;
    private final List<Route> routes;

    public City(String name) {
        this.name = name;
        this.routes = new ArrayList<>();
    }

    public City(String name, Route... routes) {
        this.name = name;
        this.routes = new ArrayList<>(Arrays.asList(routes));
    }

    public String getName() {
        return name;
    }

    public List<Route> getRoutes() {
        return routes;
    }

    public void addRoute(City city, int cost) {
        routes.add(new Route(city, cost));
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();

        result.append(name).append(": ");

        for (int i = 0; i < routes.size(); i++) {
            result.append(routes.get(i));

            if (i < routes.size() - 1) {
                result.append(", ");
            }
        }

        return result.toString();
    }
}