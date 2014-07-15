'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
    .controller('CatererListCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
        Restangular.all('caterers').getList().then(function (blahblahblah) {
            $scope.caterers = blahblahblah;
        });
    }])