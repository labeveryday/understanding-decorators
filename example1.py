"""Decorators to add routes to a routing table"""
routing_table = []

def routes(func):
    """Decorator that adds routes to routing table and return function"""
    def wrapper(route):
        route_entry = func(route)
        routing_table.append(route_entry)
        return route_entry
    return wrapper

@routes
def add_static_route(route):
    """Add a static route"""
    print("Adding static route.....")
    return f"s: {route}"

@routes
def add_bgp_route(route):
    """Add bgp route"""
    print("Adding bgp route.....")
    return f"b: {route}"

if __name__ == "__main__":
    add_static_route("192.168.1.0 255.255.255.0 10.1.1.1")
    add_bgp_route("172.16.31.16 255.255.255.240 10.1.2.1")
    print("\nCurrent routing table entries.")
    for route in routing_table: 
        print(route)
