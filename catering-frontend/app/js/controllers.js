'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('CatererListCtrl', ['$scope', function ($scope, Restangular) {
        Restangular.all('caterers').getList().then(function (data) {
            $scope.caterers = data;
        });
    }])