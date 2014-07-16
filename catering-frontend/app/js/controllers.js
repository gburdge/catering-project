'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('CatererListCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
        Restangular.all('caterers').getList().then(function (data) {
            $scope.caterers = data;
        });
    }])

    .controller('CatererDetailCtrl', function ($scope, Restangular, $routeParams) {
        $scope.catererId = $routeParams.catererId;

        Restangular.one('caterer', $scope.catererId).customGET().then(function (data) {
            $scope.caterer = data;
        });
    })

    .controller('FoodItemCtrl', function ($scope, Restangular, $routeParams) {
        $scope.catererId = $routeParams.catererId;

        Restangular.one('caterer', $scope.FoodItem).customGET().then(function (data) {
            $scope.caterer = data;
        });
    });



