# SOLID:

- S - Single Responsibility Principle (SRP): A class should have only one reason to change, meaning it should only have one job or responsibility. If a class has multiple responsibilities, it becomes more complex and harder to maintain.
- O - Open-Closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality to a class without changing its existing code, which helps prevent bugs and makes the system more robust.
- L - Liskov Substitution Principle (LSP): Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This means that if you have a class hierarchy, derived classes should be able to be used interchangeably with their parent class.
- I - Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use. This means that it's better to have many specific interfaces rather than a single general-purpose one.
- D - Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle encourages the use of interfaces or abstract classes to reduce dependencies between modules.
## Task 1
### Given Code:
```php
class SomeObject {
    protected $name;
    public function __construct(string $name) { }
    public function getObjectName() { }
}
class SomeObjectsHandler {
    public function __construct() { }
    public function handleObjects(array $objects): array {
        $handlers = [];
        foreach ($objects as $object) {
            if ($object->getObjectName() == 'object_1')
                $handlers[] = 'handle_object_1';
            if ($object->getObjectName() == 'object_2')
                $handlers[] = 'handle_object_2';
        }
        return $handlers;
    }
}
$objects = [
    new SomeObject('object_1'),
    new SomeObject('object_2')
];
$soh = new SomeObjectsHandler();
$soh->handleObjects($objects);
```
handleObjects in SOmeObjectHandler class relies on on the names of each object to decide what handler
to run. This doesn't allow us to add new functionality to handle new objects easily without modifying the
the HandleObjects function.

### Fixed Code:
```php
// Define an interface for handling objects
interface ObjectHandler {
    public function handle(SomeObject $object): string;
    public function supports(SomeObject $object): bool; // New method for checking support
}

// Handler for object_1
class Object1Handler implements ObjectHandler {
    public function handle(SomeObject $object): string {
        return 'handle_object_1';
    }

    public function supports(SomeObject $object): bool {
        return $object->getObjectName() === 'object_1'; // Check if this handler supports the object
    }
}

// Handler for object_2
class Object2Handler implements ObjectHandler {
    public function handle(SomeObject $object): string {
        return 'handle_object_2';
    }

    public function supports(SomeObject $object): bool {
        return $object->getObjectName() === 'object_2'; // Check if this handler supports the object
    }
}

// Update SomeObjectsHandler
class SomeObjectsHandler {
    private $handlers;

    public function __construct(array $handlers) {
        $this->handlers = $handlers;
    }

    public function handleObjects(array $objects): array {
        $results = [];
        foreach ($objects as $object) {
            foreach ($this->handlers as $handler) {
                if ($handler->supports($object)) { // Only call if the handler supports the object
                    $results[] = $handler->handle($object);
                    break; // Stop searching after the first match
                }
            }
        }
        return $results;
    }
}

// Example usage
$objects = [
    new SomeObject('object_1'),
    new SomeObject('object_2')
];

// Instantiate handlers and pass them to the handler manager
$handlers = [new Object1Handler(), new Object2Handler()];
$soh = new SomeObjectsHandler($handlers);
$results = $soh->handleObjects($objects);
print_r($results);
```

## Task 2
### Given Code:
```php
class XMLHttpService extends XMLHTTPRequestService {}
class Http {
    private $service;
    public function __construct(XMLHttpService $xmlHttpService) { }
    public function get(string $url, array $options) {
        $this->service->request($url, 'GET', $options);
    }
    public function post(string $url) {
        $this->service->request($url, 'GET');
    }
}
```
Given code has tight coupling between the Http class and XMLHttpService in violation of DIP. If changes made to XMLHttpService, we have to change Http. So we need to introduce abstractions that will allow Http to take not only XMLHttpService as a parameter. Also, we need to make sure that XMLHttpService will follow the abstruction's structure. Also, there is a typo with the POST method.

### Fixed Code:
```php
//Define an interface for HTTP services
interface HttpServiceInterface {
    public function request(string $url, string $method, array $options = []);
}

//Modify XMLHttpService to implement the interface
class XMLHttpService implements HttpServiceInterface {
    public function request(string $url, string $method, array $options = []) {
        // Implementation for making an XMLHttp request.
        echo "Request made to $url with method $method and options: " . json_encode($options) . "\n";
    }
}

//Refactor the Http class to depend on the interface
class Http {
    private $service;

    // Dependency is now on the interface
    public function __construct(HttpServiceInterface $service) {
        $this->service = $service;
    }

    public function get(string $url, array $options) {
        return $this->service->request($url, 'GET', $options); // Use the interface method
    }

    public function post(string $url, array $options) {
        return $this->service->request($url, 'POST', $options); // Correctly use 'POST' method
    }
}

// Example Usage
$xmlHttpService = new XMLHttpService();
$http = new Http($xmlHttpService);
$responseGet = $http->get('http://example.com/api/getData', ['param1' => 'value1']);
$responsePost = $http->post('http://example.com/api/postData', ['param2' => 'value2']);
```

