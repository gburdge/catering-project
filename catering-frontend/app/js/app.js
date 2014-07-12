'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers',
])
    .config(['$routeProvider', function($routeProvider, RestangularProvider) {
  $routeProvider
      .when('/home', {
          templateUrl: 'partials/home.html',
          controller: 'MyCtrl1'
      })
      .when('/menu', {
          templateUrl: 'partials/menu.html',
          controller: 'MyCtrl1'
      })
      .otherwise({
          redirectTo: '/home'
      });
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);
