public class Route {

    private final City city;
    private final int cost;

    public Route(City city, int cost) {
        this.city = city;
        this.cost = cost;
    }

    public City getCity() {
        return city;
    }

    public int getCost() {
        return cost;
    }

    @Override
    public String toString() {
        return city.getName() + ":" + cost;
    }
}