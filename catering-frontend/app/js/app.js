'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers',
  'restangular'
]).
config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
  $routeProvider
      .when('/home', {
          templateUrl: 'partials/home.html',
          controller: 'MyCtrl1'
      })

      .when('/caterer/:catererId', {
          templateUrl: 'partials/caterer.html',
          controller: 'CatererDetailCtrl'
      })

      .when('/caterers', {
          templateUrl: 'partials/caterer-list.html',
          controller: 'CatererListCtrl'
      })

      .when('/menu', {
          templateUrl: 'partials/menu.html',
          controller: 'MenuCtrl'
      })

      .otherwise({
          redirectTo: '/home'
      });
  RestangularProvider.setBaseUrl('http://127.0.0.1:8001');
}]);
