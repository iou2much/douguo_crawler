'use strict';

/* Controllers */

var phonecatApp = angular.module('phonecatApp',[]);
  
phonecatApp.controller('MaterialCtrl', function($scope, $http) {
    $scope.desc = true;
    //$scope.perPage= 16;
    //$scope.perPagePresets = [16,24,32];
    //$scope.myPerPageSets= [16,24,32];
    $scope.orderProp = '-zuone_piao';
});

function getDocHeight() {
    return Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );
}
