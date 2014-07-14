'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers'
]).
config(['$routeProvider', function($routeProvider, RestangularProvider) {
  $routeProvider
      .when('/company/:companyId', {
          templateUrl: 'partials/company.html',
          controller: 'MyCtrl1'
      })

      .when('/companies', {
          templateUrl: 'partials/partial2.html',
          controller: 'CompanyList'
      })

      .otherwise({
          redirectTo: '/view1'
      });
  RestangularProvider.setBaseUrl('http://localhost:8001');
}]);
