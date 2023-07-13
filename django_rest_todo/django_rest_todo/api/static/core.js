var djangoTodo = angular.module('djangoTodo', []);

function mainController($scope, $http) {

    $scope.readTodos = function() {
        $http.get('/api/todos/')
            .success(function(data) {
                $scope.formData = {};
                $scope.todos = data;
                console.log(data);
            })
            .error(function(data) {
                console.log('Error: ' + data);
            });
    };

    $scope.createTodo = function() {
        $http.post('/api/todos/', $scope.formData)
            .success(function(data) {
                console.log(data);
                $scope.readTodos();
            })
            .error(function(data) {
                console.log(`Error: ${data}`);
            });
    };

    $scope.deleteTodo = function(id) {
        var config = {
            headers: {
                'Authorization': 'Bearer ' + authToken
            }
        };
        $http.delete(`/api/todos/${id}`,config)
        .then(function(response) {
            console.log(response.data);
            $scope.readTodos();
        })
            // .catch(function(data) {
            //     console.log(`Error:${data}`);œ
            // });
    };

    $scope.readTodos();

}
