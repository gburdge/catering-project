'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('CatererListCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
        Restangular.all('caterers').getList().then(function (blahblahblah) {
            $scope.caterers = blahblahblah;
        });
    }])

    .controller('CatererDetailCtrl', function ($scope, Restangular, $routeParams) {
        $scope.catererId = $routeParams.catererId;

        Restangular.one('recipes', $scope.catererId).customGET().then(function (data) {
            $scope.caterer = data;

        });
    })