'use strict';

/* Controllers */
var phonecatApp = angular.module('phonecatApp',['angular-loading-bar','ngAnimate'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
      cfpLoadingBarProvider.includeSpinner = false;
      cfpLoadingBarProvider.latencyThreshold = 50;
}]);
  
var bigimg = function(img){
    if(!$(img).attr('src'))return;
    var shape = $(img).attr('shape');
    var re_shape = null;
    if(!shape){
        if($(img).attr('src').indexOf('square')>0&&$(img).attr('src').indexOf('thumbnail')<0){
            $(img).attr('shape' , 'square');
        }else{
            $(img).attr('shape' , 'thumbnail');
        }
        shape = $(img).attr('shape');
    }
    re_shape = new RegExp(shape,'g');

    if($(img).attr('expanded')=='true'){
        $(img).attr('src',$(img).attr('src').replace(/bmiddle/g,shape));
        $(img).attr('expanded',false);
    }else{
        $(img).attr('src',$(img).attr('src').replace(re_shape,'bmiddle'));
        $(img).css({'max-height':'none','max-width':'none','width':'auto','height':'auto'});
        $(img).parent('div').css({'max-height':'none','max-width':'none'});
        $(img).parent('li').css({'max-height':'none','max-width':'none','width':'auto','height':'auto'});
        $(img).parent('li').parent('ul').css({'max-height':'none','max-width':'none','width':'auto','height':'auto'});
        $(img).attr('expanded',true);
    }
};
phonecatApp.controller('PhoneListCtrl', function($scope, $http, $sce) {
    $http.get('data/fav.json').success(function(data) {
        for(var i in data){
            data[i]['user'] = $sce.trustAsHtml(data[i]['user']);
            data[i]['text'] = $sce.trustAsHtml(data[i]['text']);
            if(data[i]['media'])
                data[i]['media'] = $sce.trustAsHtml(data[i]['media'].replace(/bigcursor"/g,'bigcursor" onclick="bigimg(this)"'));
            if(data[i]['forward'])
                data[i]['forward'] = $sce.trustAsHtml(data[i]['forward'].replace(/bigcursor"/g,'bigcursor" onclick="bigimg(this)"'));
        }
        $scope.feeds = data;
    });
  //$scope.orderProp = '-zuone_piao';
});
phonecatApp.directive(
    "bnLazySrc",bnLazySrc
);
