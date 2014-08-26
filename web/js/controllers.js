'use strict';

/* Controllers */

var sort_by = function(field, reverse, primer){ 
				reverse = (reverse) ? -1 : 1; 
				return function(a,b){ 
				    a = a[field]; 
				    b = b[field]; 
				    if (typeof(primer) != 'undefined'){ 
					a = primer(a); 
					b = primer(b); 
				    } 
				    if (a<b) return reverse * -1; 
				    if (a>b) return reverse * 1; 
				    return 0; 
				}   
};

var phonecatApp = angular.module('phonecatApp',['angular-loading-bar','ngAnimate'])
  .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
      cfpLoadingBarProvider.includeSpinner = false;
      cfpLoadingBarProvider.latencyThreshold = 50;

  }]);
  
phonecatApp.controller('PhoneListCtrl', function($scope, $http) {
  $http.get('data/winner.json').success(function(data) {
    var authors = {};
    var res = [];
    for(var i in data){
            data[i]['zuone_piao'] = Number(data[i]['zuone_piao'])
    }
      
    data.sort(sort_by('zuone_piao',true ,parseInt));
    var multi_zuone = {};
    for(var i in data){
        //if((res.length < 200 && authors[data[i]['zuone_author_name']] == undefined)||data[i]['zuone_piao']=='37'){
        //if(res.length < 200 && authors[data[i]['zuone_author_name']] == undefined){
        if(authors[data[i]['zuone_author_name']] == 1){
            if(multi_zuone[data[i]['zuone_author_name']] == undefined){
            	multi_zuone[data[i]['zuone_author_name']] = [];
            }
            multi_zuone[data[i]['zuone_author_name']].push(data[i]);
        }
        
        if(authors[data[i]['zuone_author_name']] == undefined){
            //data[i]['sort'] = res.length+1;
	    	res.push(data[i]);
        }
        authors[data[i]['zuone_author_name']] = 1;

		//}
    }

      
    $scope.winners = res;
    $scope.multi_zuone = multi_zuone;
    //console.log(multi_zuone);
    //console.log(data.length);
    //console.log(res.length);
  });

  $scope.orderProp = '-zuone_piao';
    
});
function getDocHeight() {
    return Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight, document.documentElement.offsetHeight,
        document.body.clientHeight, document.documentElement.clientHeight
    );
}
phonecatApp.directive(
	"bnLazySrc",bnLazySrc
	
);
