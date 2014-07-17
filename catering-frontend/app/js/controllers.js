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


        $scope.increment_Qty= function(food_item) {

           food_item.quantity += 1;

        }
        $scope.decrease_Qty= function(food_item){

            if (food_item.quantity > 0){
                    food_item.quantity -= 1;
            }

        }

        $scope.calculatePrice= function(food_item){

            var price =  food_item.price * food_item.quantity;

            return "$"+price.toFixed(2);

        }

    })

    .controller('FoodItemCtrl', function ($scope, Restangular, $routeParams) {
        $scope.catererId = $routeParams.catererId;

        Restangular.one('caterer', $scope.FoodItem).customGET().then(function (data) {
            $scope.caterer = data;
        });
    });



